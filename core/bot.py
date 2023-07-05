from pyrogram import Client, types
from configs import configs


bot = Client(
    "bot",
    api_id=configs.api_id,
    api_hash=configs.api_hash,
    bot_token=configs.bot_token,
    plugins=dict(root="plugins"),
    in_memory=True,
)


async def generate_commands():
    await bot.set_bot_commands(
        commands=[
            types.BotCommand("start", "Start the bot"),
            types.BotCommand("new", "Start new dialog"),
            types.BotCommand("tokens", "Show Tokens"),
            types.BotCommand("help", "Show Help Message"),
            types.BotCommand("subscribe", "Show Message to Subscribe Channel"),
        ]
    )
