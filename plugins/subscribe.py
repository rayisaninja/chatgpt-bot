from pyrogram import Client, filters, types


@Client.on_message(filters.command("subscribe"))
async def subs_handler(_, m: types.Message):
    return await m.reply("Please press button below to know how to subscribe", reply_markup=types.InlineKeyboardMarkup(
        [
            [
                types.InlineKeyboardButton("Subscribe Channel", url="https://t.me/octopus_chat_subscription")
            ]
        ]
    ))
