from pyrogram import Client, filters, types
from controllers import user


@Client.on_message(filters.command("tokens"))
async def token_check(_, m: types.Message):
    usr = m.from_user
    if not await user.Get(usr.id):
        await user.Create(usr.id, usr.first_name, usr.last_name)
    usr = await user.Get(usr.id)
    return await m.reply(
        f"""You have {usr.token_limit} tokens left.
Joined to Private Channel: {'Yes' if usr.subscribed else 'No'}""",
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton("Subscribe Channel", url="https://t.me/octopus_chat_subscription")
                ]
            ]
        )
    )
