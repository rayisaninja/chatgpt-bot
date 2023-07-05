from pyrogram import filters


conversation = {}


def get_conv(conv_level: str):
    def conv_filter(_, __, m):
        if m.from_user:
            return conversation.get(m.from_user.id) == conv_level

    return filters.create(conv_filter, "Conversation Filter")


command_list = [
    "start",
    "help",
    "new",
    "tokens",
    "subscribe"
]