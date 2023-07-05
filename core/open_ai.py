import openai
from configs import configs


chatgpt = openai
chatgpt.api_key = configs.openai_api_key
