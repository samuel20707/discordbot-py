import aiohttp
import discord
import asyncio
import random
import datetime
from datetime import datetime
import os
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.all()
client = discord.Client(intents=intents)


Botname = '이지민'
token = 'MTA3NzE2MjU2MDQ3NTg4OTcyNg.GeSe_1.7i_z_Ygc9pYl0jvZ3yIzB9ka3yXHkGosHqw-vk'

def spechanjae():
    url="https://hangang.ivlis.kr/aapi.php?type=dgr"
    response=requests.get(url)
    return response.text

embed = discord.Embed(title="😎이지민 도움말", description="지민이의 명령어들이 궁금하신가요?", color=0xFF00DD)
embed.add_field(name="💌타이머", value="'지민아 타이머 n'라고 물어보세요!(n=자연수)", inline=False)
embed.add_field(name="💯계산기", value="'지민아 계산기 (i)'라고 물어보세요! i는 수식 입니다!", inline=False)
embed.add_field(name="🍕메뉴추천", value="'지민아 메뉴추천'라고 물어보세요!", inline=False)
embed.add_field(name="✌🏻✊🏻🖐🏻가위바위보", value="'지민아 가위바위보 (i)'라고 물어보세요! i는 가위 or 바위 or 보 입니다!", inline=False)
embed.add_field(name="🎫숫자맞추기", value="'지민아 숫자맞추기'라고 물어보세요!", inline=False)
embed.add_field(name="🎁주사위", value="'지민아 주사위'라고 물어보세요! 1~6까지의 랜덤수를 대답합니다!", inline=False)
embed.add_field(name="⛑한강물온도", value="'지민아 한강물온도'라고 물어보세요!", inline=False)
embed.add_field(name="💝초대링크", value="'지민아 초대링크'라고 물어보세요!", inline=False)
embed.add_field(name="⛔아직 만드는 중이에요...", value="이지민 봇을 이용해주셔서 감사합니다!!!", inline=False)
embed.set_footer(text="감사합니다!")

embed1 = discord.Embed(title="⛔경고⛔", description="이지민 봇이 과부화 되었습니다.", color=0xFF00DD)
embed1.add_field(name="대처법", value="이지민 봇을 1~120초 동안 이용하지 말아주세요!", inline=False)
embed1.add_field(name="죄송합니다", value="이 경고는 이지민 봇의 '운영자'에 의해 발송됩니다.", inline=False)
embed1.add_field(name="아직 문제를 검토중이니 잠시만 기달려주세요!", value="이지민 봇을 이용해주셔서 감사합니다!!!", inline=False)


menu_list = ["짜장면", "피자", "치킨", "초밥", "떡볶이", "삼겹살", "우동", "라면", "물냉면", "비빔밥", "삼겹살", "된장찌개", "불고기", "잡채밥", "김치찌개", "갈비탕", "떡볶이", "소고기볶음밥", "해물파전", "쭈꾸미볶음", "감자탕", "산채비빔밥", "산낙지", "칼국수", "샤브샤브", "육회", "회덮밥", "김밥", "라면", "우동", "초밥", "돈부리", "참치회", "샐러드", "파스타", "스테이크", "그라탕", "치킨스테이크", "수제피자", "중화볶음밥", "탕수육", "짬뽕", "군만두", "삼선짜장", "매운탕", "홍합탕", "카레라이스", "소세지야채볶음", "양념치킨", "베이컨감자튀김", "케이준치킨", "양꼬치", "짜조면", "만두국", "부대찌개", "해물탕", "닭볶음탕", "순대국", "냉모밀", "오므라이스", "햄버거", "산적비빔밥", "오리주물럭", "홍어회", "산낙지숙회", "장어구이", "돼지국밥", "물회", "곰탕", "산채조림", "고등어조림", "황태해장국", "갈비찜", "닭갈비", "산적국수", "해물누룽지탕", "생선구이", "돈까스", "오므라이스", "오코노미야키", "모밀", "팟타이", "빈대떡", "호떡", "삼각김밥", "임실치즈국밥", "두부조림", "양념게장", "매운막창", "돼지껍데기", "곱창구이", "뼈해장국", "감자전", "미역국", "닭볶음", "팔보채", "돼지꽃게탕", "토란국", "계란국", "비빔국수", "팥빙수", "인절미빙수", "팥죽", "녹차빙수", "왕만두", "찹쌀떡", "호박전", "야채전", "해물파스타", "삼겹살김치찜", "등갈비찜", "미나리전", "장어덮밥", "치즈라면", "매운갈비찜", "오리불고기", "동태찌개", "고등어구이", "오꼬노미야끼", "육전", "육개장", "닭곰탕", "북어국", "감자탕", "미역줄기볶음", "목살스테이크", "낙지볶음", "돈코츠라멘", "닭도리탕", "훠궈", "훈제오리", "고추잡채", "보쌈", "전복죽", "해물죽", "콩국수", "참나물고기전", "어묵국", "옛날돈까스", "코다리조림", "부대전골", "쌀국수"]
recommended_menu = random.choice(menu_list)

@ client.event
async def on_ready():
    print(f'{Botname}이 켜졌습니다.')
    print('-----------------------------------------------------------------------')
    print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중")
    print(f"[!] 서버 인원 총합 : {len(client.users)}와 함께하는 중")
    print('-----------------------------------------------------------------------')
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {} / 멤버 수: {}".format(i.id, i.name, i.member_count))
    print('-----------------------------------------------------------------------')
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(f'TIME: [ {now} ] / BOT IS ONLINE')
    while True:
        await asyncio.sleep(600)
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print(f'TIME: [ {now} ] / BOT IS ONLINE')

@ client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content==('지민아'):
        await message.reply('네! 저 여기에 있습니다! "지민아 도움말"로 명령어를 확인하세요!')
    
    if message.content==('지민아 한강물온도'):
         await message.reply(spechanjae())
         
    if message.content==('지민아 현재날짜'):
        await message.reply(datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
        
    if message.content==('지민아 추천서버'):
        await message.reply('디스코드 봇을 만들고 테스트해봐요! https://discord.gg/TKf8EcDW3m')

    if message.content==('지민아 도움말'):
        await message.reply(embed=embed)

    if message.content.startswith('지민아 타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(2, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        sec = int(Text) #!타이머 5 라고입력하면 sec값은 5가됩니다.

        for i in range(sec, 0, -1):
            print(i)
            time.sleep(1)
        else:
            print("땡")
            await message.reply('지민이가 알립니다! 타이머 종료!')
            
    if message.content==('000000000000000000'):
        for i in range(100):
            await message.channel.send(embed=embed1)
            
    if message.content==('rodheuf-wifbeu-20dibv-2947398-fivsbhd+dowfij09=fnwibf97987vj/eoefbiurfb-eovbdjvhj+dkhfjkdddddfhkdj-akfnjsfdjkkkkkfh(dkdjk)'):
         await message.channel.send(embed=embed1)


    if message.content==('지민아 주사위'):
        roll = random.randint(1, 6) # 1과 6 사이의 랜덤한 숫자 생성
        await message.reply(f'주사위를 굴려 {roll}이(가) 나왔습니다!') # 주사위 결과 출력

    if message.content.startswith('지민아 가위바위보'):
        user_choice = message.content.split(' ')[2] # 사용자가 선택한 가위바위보
        bot_choice = random.choice(['가위', '바위', '보']) # 봇이 선택한 가위바위보

        if user_choice == bot_choice:
            result = '비겼습니다!'
        elif (user_choice == '가위' and bot_choice == '보') or \
             (user_choice == '바위' and bot_choice == '가위') or \
             (user_choice == '보' and bot_choice == '바위'):
            result = '이겼습니다!'
        else:
            result = '졌습니다!'

        await message.reply(f'지민이: {bot_choice}\n결과: {result}') # 봇이 선택한 가위바위보와 결과 출력

    if message.author == client.user:
        return

    if message.content == '지민아 숫자맞추기':
        answer = random.randint(1, 100) # 1과 100 사이의 랜덤한 숫자 생성
        await message.reply('1부터 100 사이의 숫자를 맞춰보세요!')

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and msg.content.isdigit()

        try:
            guess = await client.wait_for('message', check=check, timeout=10.0) # 10초 동안 사용자가 입력한 숫자를 기다림
        except:
            await message.channel.send('시간이 초과되었습니다!')
            return

        if int(guess.content) == answer:
            await message.reply('정답입니다!')
        else:
            await message.reply(f'틀렸습니다. 정답은 {answer}입니다.')

    if message.content==('지민아 메뉴추천'):
        recommended_menu = random.choice(menu_list)
        await message.reply('오늘은 {} 어떠세요?'.format(recommended_menu))

    if message.author == client.user:
        return

    if message.content.startswith('지민아 계산기'):
        try:
            expression = message.content[7:]
            result = eval(expression)
            await message.reply(result)
        except:
            await message.reply('잘못된 수식입니다.')

    if message.content == '지민아 초대링크':
        invite_link = await message.channel.create_invite()
        await message.reply(invite_link)


client.run(token)