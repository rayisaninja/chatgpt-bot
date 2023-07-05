from pyrogram import Client, types, filters
from controllers import user
from utils import is_banned


@Client.on_message(filters.command("start"))
@Client.on_message(filters.command("help"))
async def start_handle(c: Client, m: types.Message):
    usr = m.from_user
    if not (usrr := await user.Get(usr.id)):
        usrr = await user.Create(usr.id, usr.first_name, usr.last_name)
    if not await is_banned(c, m):
        usrr.subscribed = True
        if not usrr.subscribe_checked:
            usrr.token_limit = 10000
            usrr.subscribe_checked = True
    else:
        usrr.subscribed = False
    await usrr.save()
    return await m.reply(
        """Hello! I'm ChatGPT Bot that Implemented with OpenAI API
Commands:
- /start - Start the bot
- /new - Start new dialog
- /tokens - Show Tokens
- /help - Show Help Message
- /subscribe - Show Message to Subscribe Channel"""
    )
