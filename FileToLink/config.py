import os


class Config:
    API_ID = '14252054'
    API_HASH = 'd1fe0b5deec9bcac4d8238146b2d9a4c'
    Token = '5625429337:AAHnbwy1Q_oM7qdwL5Mp2ANuH_4Sot70VPs'
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = 'filelink'
    Port = '8080'
    Archive_Channel_ID = '-1001788475665'
    Start_Message = 'Hola'
    Bot_Channel = 'megaspacefiletolink_bot'
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

   # Link_Root = f"https://{App_Name}.herokuapp.com/"
    Link_Root = "https://filelink.onrender.com/"
    Download_Folder = "Files"
    Dev_Channel = "shadow_bots"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 1024 * 1024  # (1MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 1  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 Download LINK"
    st_link = "🎞 Stream LINK"
    generating_link = "**⏳ Generating Link...**"
    bot_channel = "📢 Bot Channel"
    dev_channel = "🤖 Developer"
    fast = "⚡️**The link has been updated to a fast link**"
    update_link = "⚡ Update To Fast Link"
    update_limited = (f"⛔ You can update just {Config.Max_Fast_Processes} link in one time, "
                      "please wait until previous update to complete")
    re_update_link = "🔄 Re-Updating the link"
    already_updated = "The link is already updated"
    wait_update = "⏳ Updating the link..."
    wait = "⏳ Please wait..."
    progress = "⏳ Progress"
    file_not_found = "⚠️File Not Found, Please resend it again"
    delete_manually_button = "⚠️You can delete it"
    delete_forbidden = "The bot can't delete messages older than 48 hours, you can delete this message manually"
    force_join = "⚠ Join Bot Channel to use this Bot"
