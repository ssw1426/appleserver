
# 아람쓰#5050 또는 아람#5920 : 전체디엠봇 소스
# 영상보고 모르는점 있을시 유튜브 댓글또는 디엠주세요


import discord
import asyncio
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다(24시간 온라인).")
    game = discord.Game('디엠 받기')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 523745826791489547:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="[AppleㆍRP 공지사항]")
                        embed.add_field(name="아래 내용 확인해주세요", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/EpGT7Y8xvG")
                        await i.send(embed=embed)
                except:
                    pass

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
