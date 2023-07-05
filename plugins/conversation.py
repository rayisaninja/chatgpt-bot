from pyrogram import Client, filters, types, enums
from controllers import user, open_ai
from controllers.conversation import conversation, get_conv, command_list


info = {}

@Client.on_message(
    filters.text & filters.private &
    ~get_conv("chat") & ~filters.command(command_list)
)
async def conversation_handler(c: Client, m: types.Message):
    prompt = m.text
    user_id = m.from_user.id
    if not (usr := await user.Get(user_id)):
        await user.Create(user_id, m.from_user.first_name, m.from_user.last_name)
    conversation[user_id] = "chat"
    chatbot = open_ai.ChatGPT(usr)
    info[user_id] = {"chatbot": chatbot, "user": usr}
    await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
    answer = await chatbot(prompt)
    if answer.startswith("Your tokens are not enough to generate answer from ChatGPT"):
        info.pop(user_id)
        conversation.pop(user_id)
        return await m.reply(answer, quote=True, reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton("Subscribe Channel", url="https://t.me/octopus_chat_subscription")
                ]
            ]
        ))
    return await m.reply(answer, quote=True)


@Client.on_message(
    get_conv("chat") & ~filters.command(command_list) & filters.private
)
async def chat_handler(_, m: types.Message):
    user_id = m.from_user.id
    data = info[user_id]
    chatbot = data["chatbot"]
    prompt = m.text
    m = await m.reply("...")
    answer = await chatbot(prompt)
    if answer.startswith("Your tokens are not enough to generate answer from ChatGPT"):
        await m.delete()
        return await m.reply(answer, quote=True, reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton("Subscribe Channel", url="https://t.me/octopus_chat_subscription")
                ]
            ]
        ))
    return await m.edit(answer)


@Client.on_message(filters.command("new") & filters.private)
async def new_dialog(_, m: types.Message):
    user_id = m.from_user.id
    conversation[user_id] = "chat"
    data = info[user_id]
    chatbot = data["chatbot"]
    chatbot.messages = [{"role": "system", "content": "You will be a helpful assistant!"}]
    return await m.reply("New Dialog Started")