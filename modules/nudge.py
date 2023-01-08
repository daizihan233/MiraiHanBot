#  本项目遵守 AGPL-3.0 协议，项目地址：https://github.com/daizihan233/MiraiHanBot

from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, At
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from loguru import logger

import botfunc

channel = Channel.current()
channel.name("Nudge")
channel.description("你戳你妈呢？")
channel.author("HanTools")


@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def getup(app: Ariadne, event: NudgeEvent):
    if event.target == botfunc.get_config('qq'):
        if event.context_type == "group":
            logger.info(f"{event.supplicant} 在群 {event.group_id} 戳了戳 Bot")
            await app.send_group_message(
                event.group_id,
                MessageChain(MessageChain(At(event.supplicant), Plain(" 你在戳什么？！")))
            )
        elif event.context_type == "friend":
            logger.info(f'{event.supplicant} 在私聊中戳了戳 Bot')
            await app.send_friend_message(
                event.friend_id,
                MessageChain("别戳我，好痒！")
            )
        else:
            return
