from core import db
from pyrogram import idle
from core.bot import bot, generate_commands
from controllers.scheduler import scheduler
from utils import refresh_token

async def main():
    await bot.start()
    await generate_commands()
    me = bot.me
    print(f"Bot started as {me.username}({me.id})")
    await db.init_db()
    # print("Starting Refresh Token Schedule Every one day")
    # scheduler.add_job(refresh_token, "interval", days=1)
    # scheduler.start()
    print("Idling Now...")
    await idle()


if __name__ == '__main__':
    bot.run(main())
