from core.open_ai import chatgpt
from models import User
import tiktoken

class ChatGPT:
    def __init__(self, user: User):
        self.user = user
        self.user_id = user.id
        self.history = []
        self.messages = [{"role": "system", "content": "You will be a helpful assistant!"}]

    async def __call__(self, prompt: str):
        self.messages.append({"role": "user", "content": prompt})
        first_token = self.count_token()
        if first_token > self.user.token_limit:
            return f"Your tokens are not enough to generate answer from ChatGPT. You have {self.user.token_limit} tokens left\nTry to use /new command to reset the converationn\nChatGPT needs minimum of {first_token} tokens to generate answer\n\nPlease Subscribe or renew your subscription"
        response = await chatgpt.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            max_tokens=1000,
            messages=self.messages
        )
        usage = response["usage"]["total_tokens"]
        if usage > self.user.token_limit:
            return "You have no more tokens"
        self.user.token_limit -= usage
        await self.user.save()
        responses = response["choices"][0]["message"]
        self.messages.append(responses)
        return responses["content"]

    def count_token(self):
        encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = 0
        token_per_msg = 3
        for message in self.messages:
            num_tokens += token_per_msg
            for _, val in message.items():
                num_tokens += len(encoding.encode(val))
        num_tokens += 3
        return num_tokens
