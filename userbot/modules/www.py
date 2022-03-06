# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.utils import edit_delete, edit_or_reply, reply_id
from userbot.events import register

def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

@register(outgoing=True, pattern="^.speed$")
@register(
    pattern="speedtest(?:\s|$)([\s\S]*)",
    command=("speedtest"),
    info={
        "header": "Botserver's speedtest by ookla.",
        "options": {
            "text": "will give output as text",
            "image": (
                "Will give output as image this is default option if "
                "no input is given."
            ),
            "file": "will give output as png file.",
        },
        "usage": ["{tr}speedtest <option>", "{tr}speedtest"],
    },
)
async def speedtst(spd):
    "Botserver's speedtest by ookla."
    input_str = speed.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    spd = await edit_or_reply(
        spd, "`Calculating my internet speed. Please wait!`"
    )
    start = datetime()
    test = speedtest.Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    end = datetime()
    ms = round(end - start, 2)
    response = test.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(spd)
    try:
        response = test.results.share()
        speedtest_image = response
        if as_text:
            await spd.edit(
                """`SpeedTest completed in {} seconds`

`Download: {} (or) {} MB/s`
`Upload: {} (or) {} MB/s`
`Ping: {} ms`
`Internet Service Provider: {}`
`ISP Rating: {}`""".format(
                    ms,
                    speed_convert(download_speed),
                    round(download_speed / 8e6, 2),
                    speed_convert(upload_speed),
                    round(upload_speed / 8e6, 2),
                    ping_time,
                    i_s_p,
                    i_s_p_rating,
                )
            )
        else:
            await spd.client.send_file(
                spd.chat_id,
                speedtest_image,
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False,
            )
            await spd.delete()
    except Exception as exc:
        await spd.edit(
            """**SpeedTest** completed in {} seconds
Download: {} (or) {} MB/s
Upload: {} (or) {} MB/s
Ping: {} ms

__With the Following ERRORs__
{}""".format(
                ms,
                speed_convert(download_speed),
                round(download_speed / 8e6, 2),
                speed_convert(upload_speed),
                round(upload_speed / 8e6, 2),
                ping_time,
                str(exc),
            )
        )
  

@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`pooong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping`\
    \nUsage: Shows how long it takes to ping your bot.\
    \n\n`.speed`\
    \nUsage: Does a speedtest and shows the results."
})
