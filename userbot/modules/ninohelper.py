""" Userbot module for other small commands. """
import sys
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern="^.ninohelp(?: |$)(.*)")
async def usit(e):
    await e.edit(
        f"Here's something for {DEFAULTUSER} to use it for help_on_update on **Nino - Project**:\n"
        "\n[Windows Method](https://telegra.ph/How-to-keep-repo-updated-while-keeping-your-changes-through-windows-cmd-method-04-01)"
        "\n[Termux Method](https://telegra.ph/How-to-keep-oub-remix-repo-updated-while-keeping-your-changes-through-Termux--kali-linux-06-02)"
        "\n[Kali Linux Method](https://telegra.ph/How-to-keep-OpenUserBot-repo-updated-while-keeping-your-changes-through-Termux-method-04-01)"
        "\n[Ubuntu Linux Method](https://telegra.ph/How-to-keep-OUB-repo-updated-while-keeping-your-changes-through-Ubuntu-Terminal-method-04-01-2)"
        "\n[Gdrive Tutorial](https://telegra.ph/How-To-Setup-Google-Drive-04-03)"
        "\n[video-tutorial](https://youtu.be/us1O-AnWmHA)")
    
@register(outgoing=True, pattern="^.setvar(?: |$)(.*)")
async def var(m):
    await m.edit(
        f"Here's a list of VARS for {DEFAULTUSER} on **oub-remix**:\n"
        "\n[HEROKU VARS](https://raw.githubusercontent.com/langramadhan/nino-project/ninouserbot/setvars.txt)")
    
    
CMD_HELP.update({
    "ninohelper":
    "`.ninohelp`\
\nUsage: Provide links to update repo guides while you keep your changes on the floor.\
\n`.setvar`\
\nUsage: Provide vars to cross check for you."
})
