from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ {}

ɴᴏᴛᴇ : 
1) ᴊᴀɴɢᴀɴ ʙʟᴏᴄᴋ ʙᴏᴛ ɪɴɪ
2) ᴋᴀʀᴇɴᴀ ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛʀɪɴɢ ᴍᴜ ᴊɪᴋᴀ ᴋᴀᴍᴜ ʙʟᴏᴄᴋ ʙᴏᴛ ɪɴɪ

ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ sᴇssɪᴏɴ sᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ ᴅᴀɴ ᴛᴇʟᴇᴛʜᴏɴ. ɢᴜɴᴀᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴛᴀʜᴜ ʟᴇʙɪʜ ʙᴀɴʏᴀᴋ!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⌬ Start Generating Session ⌬", callback_data="generate")],
        [InlineKeyboardButton(text="⌬ Return Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("⌬ Start Generating Session ⌬", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("⌬ Start Generating Session ⌬", callback_data="generate")],
        [InlineKeyboardButton("⌬ Maintaned By ⌬", url="https://t.me/JustRex")],
        [
            InlineKeyboardButton("How To Use ❔", callback_data="help"),
            InlineKeyboardButton("⋙ About ⋘", callback_data="about")
        ],
        [InlineKeyboardButton("🦖 Xa Support 🦖", url="https://t.me/rexaprivateroom")],
    ]

    # Help Message
    HELP = """
⌨ **Available Commands** ⌨

/about - To Get About This Bot 🤖
/help - Check The Bot Commands 🔧
/start - Start The Bot
/generate - Generate Your String Now 😊
/cancel - Process Cancell 🥺
/restart - Restart And Start Generate String Session 😊
"""

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Generate Pyrogram And Telethon String Session...

Xa Support : [XA SUPPORT](https://t.me/rexaprivateroom)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @JustRex
    """
