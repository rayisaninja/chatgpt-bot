import asyncio

from pyrogram import Client, types, errors
from pyrogram.enums import ChatMemberStatus
from configs import configs
from models import User


async def is_banned(c: Client, m: types.Message):
    channel_id = configs.channel_id
    try:
        x = await c.get_chat_member(channel_id, m.from_user.id)
    except errors.UserNotParticipant:
        return True
    return x.status in {ChatMemberStatus.LEFT, ChatMemberStatus.BANNED}


async def refresh_token():
    all_user = await User.all().to_list()
    for user in all_user:
        user.token_limit = 10000 if user.subscribed else 500
        await user.save()
        await asyncio.sleep(1.5)
