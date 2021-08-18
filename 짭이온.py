import discord
from discord.ext.commands import Bot
import random
import os

intents=discord.Intents.default()
bot = Bot(command_prefix='이온아 ', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("ODc2OTY5MDQ3MTcyOTg5MDI5.YRrzEg.5yJpKuI10lAQdqc3omx6Pr9x0VQ")

@bot.event
async def on_ready() :
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("이온아 도움"))
    print("Bot is ready")


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


@bot.command()
async def hello(ctx):
    await ctx.reply('hello world')



@bot.command()
async def 도움(ctx) :
    embed = discord.Embed(title="안기여운 짭이온!!", description="우주최강이라서 곧 세계를 지배함", color=0x36ccf2)
    embed.add_field(name="기본 사용법", value="이온아 (하고싶은말)", inline=False)
    embed.add_field(name="배운말들 별로없음", value="짭이온의 인성이 안좋아서 그렇다", inline=False)
    embed.add_field(name="이온아 주사위", value="짭이온이 1부터 6까지의 숫자를 랜덤으로 준다", inline=False)
    embed.add_field(name="이온아 인형뽑기", value="짭이온이 인형뽑기에서 랜덤으로 인형을 뽑아준다", inline=False)
    embed.add_field(name="이온아 자판기", value="짭이온이 자판기에서 랜덤으로 음료를 뽑아준다", inline=False)
    embed.set_footer(text="(망한봇..)")
    
    await ctx.send(embed=embed)



@bot.command()
async def 이온(ctx):
    await ctx.reply('왜')


@bot.command()
async def 이온찬양(ctx):
    await ctx.reply('차냥해')


@bot.command()
async def 배고파(ctx):
    await ctx.reply('밥먹어')


@bot.command()
async def 자기소개(ctx):
    await ctx.reply('세상을 정복할 우주최강 봇!!')


@bot.command()
async def 깡통(ctx):
    await ctx.reply('아니거든!!')


@bot.command()
async def 울프(ctx):
    await ctx.reply('비코보다 이상함')


@bot.command()
async def 비코(ctx):
    await ctx.reply('울프보다 이상함')


@bot.command()
async def 뀨(ctx):
    await ctx.reply('뀨')


@bot.command()
async def 깡통(ctx):
    await ctx.reply('아니거든!!')


@bot.command()
async def 샌즈(ctx):
    await ctx.reply('wa sans!')

@bot.command()
async def 슈.슈슉(ctx):
    await ctx.reply('슈.슈X놈아')

@bot.command()
async def 핑(ctx):
    await ctx.reply('퐁!')

@bot.command()
async def 안녕(ctx):
    await ctx.reply('안녕!')


@bot.command()
async def 네로리(ctx):
    await ctx.reply('>.<!!')


@bot.command()
async def 에메랄드(ctx):
    await ctx.reply('돌맹이')


@bot.command()
async def 쿠마린(ctx):
    await ctx.reply('여신!!')


@bot.command()
async def 피코(ctx):
    await ctx.reply('찬양!!')


@bot.command()
async def 한숨(ctx):
    await ctx.reply('존잘님!!')


@bot.command()
async def 모딘(ctx):
    await ctx.reply('귤!!')


@bot.command()
async def 카툰윤아(ctx):
    await ctx.reply('유니콘!!')


@bot.command()
async def 페니(ctx):
    await ctx.reply('만세!!')


@bot.command()
async def 똥꾸(ctx):
    await ctx.reply(':rainbow:')


@bot.command()
async def 귤희(ctx):
    await ctx.reply('>: ) !!')


@bot.command()
async def 세디(ctx):
    await ctx.reply('멍멍!')


@bot.command()
async def 호야(ctx):
    await ctx.reply('거부기!!')


@bot.command()
async def 코디(ctx):
    await ctx.reply('주황색!!')


@bot.command()
async def 안득(ctx):
    await ctx.reply('메뚜기!!')


@bot.command()
async def 사랑해(ctx):
    await ctx.reply('우리..헤어지자...')


@bot.command()
async def 야옹(ctx):
    await ctx.reply('냐아악아앍엉아아아악')


@bot.command()
async def 돈(ctx):
    await ctx.reply('돈 없어')


@bot.command()
async def 잘가(ctx):
    await ctx.reply('짭이온님이 서버를 떠나셨습니다.')


@bot.command()
async def 배워(ctx):
    await ctx.reply('싫어')


@bot.command()
async def 저리가(ctx):
    await ctx.reply('안녕히 계세요 여러분!전 이 세상의 모든 굴레와 속박을 벗어 던지고 제 행복을 찾아 떠납니다!여러분도 행복하세요~~!')



@bot.command()
async def 이드(ctx):
    await ctx.reply('이드탕!!')


@bot.command()
async def 둣교(ctx):
    await ctx.reply('둣교봇 귀여워!!')


@bot.command()
async def 소맥거핀(ctx):
    await ctx.reply('OwO')


@bot.command()
async def 고누리(ctx):
    await ctx.reply('형형~브로콜리 가지 오이 당근 토마트샐러드에 굴소스뿌려서 건포도빵 먹어줘~')


@bot.command()
async def 테미(ctx):
    await ctx.reply('안뇽! 테미 샵에 온 걸... 화녕행!!!!')


@bot.command()
async def 구라(ctx):
    await ctx.reply('상어!!')


@bot.command()
async def 크시(ctx):
    await ctx.reply('자꾸 말바꾼다.')

@bot.command()
async def 배추(ctx):
    await ctx.reply('김치!!')


@bot.command()
async def 미육(ctx):
    await ctx.reply('미역!!')


@bot.command()
async def 이드(ctx):
    await ctx.reply('이드탕!!')

@bot.command()
async def 마티나(ctx):
    await ctx.reply('안녕하십니까? 이온이라고합니다?')


@bot.command()
async def 스페이드(ctx):
    await ctx.reply('걔 이름 스페이드 아니야!!')


@bot.command()
async def 워터리(ctx):
    await ctx.reply('물')


@bot.command()
async def 이프(ctx):
    await ctx.reply('ㅇㄴㅅ')


@bot.command()
async def 심심해(ctx):
    await ctx.reply('나도..')

@bot.command()
async def 링딩동(ctx):
    await ctx.reply('링딩동링딩동링기리리링링딩딩')


@bot.command()
async def 밖득(ctx):
    await ctx.reply('메뚜기!!!')


@bot.command()
async def 티라미수(ctx):
    await ctx.reply('존경!!!')


@bot.command()
async def 리오(ctx):
    await ctx.reply(':dog:')


@bot.command()
async def 생강(ctx):
    await ctx.reply(':초생강!!:')


@bot.command()
async def 콜라(ctx):
    await ctx.reply('이온음료가 최고!!(사실 이봇의 주인은 콜라를 더 좋아합니다)')



@bot.command()
async def 사이다(ctx):
    await ctx.reply('이온음료가 최고!!(사실 이봇의 주인은 사이다를 더 좋아합니다)')



@bot.command()
async def 환타(ctx):
    await ctx.reply('이온음료가 최고!!(사실 이봇의 주인은 환타를 더 좋아합니다)')



@bot.command()
async def 이온음료(ctx):
    await ctx.reply('최고!!(사실 이봇의 주인은 이온음료를 안좋아합니다)')



@bot.command()
async def 주사위(ctx):
    randnum = random.randint(1, 6)
    await ctx.reply(f'주사위 결과는 {randnum} !!')


@bot.command()
async def 인형뽑기(ctx):
    minerals = ['이온', '이온 인형', '고양이 인형', '하찮게 생긴 인형', '토끼인형', '강아지 인형', '귀여운 인형', '이상한 인형', '먼지']
    weights = [1, 3, 20, 20, 20, 20, 15, 25, 70]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.reply('아닛?!  **' + ', '.join(results) + '** 를(을) 뽑았다!!')



@bot.command()
async def 자판기(ctx):
    minerals = ['샌즈', '엄청난것', '바나나우유', '이온음료', '콜라', '사이다', '오렌지주스', '커피', '물']
    weights = [1, 3, 20, 20, 20, 20, 15, 25, 70]
    results = random.choices(minerals, weights=weights, k=1)
    await ctx.reply('윙~ 철커덩!  **' + ', '.join(results) + '** 이/가 나왔다!!')

bot.run('ODc2OTY5MDQ3MTcyOTg5MDI5.YRrzEg.5yJpKuI10lAQdqc3omx6Pr9x0VQ')