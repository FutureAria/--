import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='퓨아가 만든 도타 오토체스 !명령어', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('!명령어'):
        await client.send_message(message.channel,"```(!표를 붙여 주셔야 합니다!) 강건함(오크) 교묘함(엘프) 기사 드루이드 마법사 명사수(드워프) 무자비(언데드) 발명가(메카) 비늘가죽(나가) 사냥꾼 악마 악마사냥꾼(동맹= 시너지) 암살자 야생(야수) 용 인간 전사 주술사 태고(엘리멘탈) 투쟁심(고블린) 트롤 피의결속(오거) 흑마법사```")
    if message.content.startswith('!강건함'):
        await client.send_message(message.channel,"```(2) 모든 강건함 유닛의 최대 체력이 200증가 (4) 모든 강건함 유닛의 최대 체력이 500증가```")
    if message.content.startswith('!강건함'):
        await client.send_message(message.channel,"```가면무사 도끼전사 디스럽터 야수지배자```")
    if message.content.startswith('!교묘함'):
        await client.send_message(message.channel,"```(3) 교묘함 유닛이 회피 +20% 획득 (6)교묘함 유닛이 회피 +45% 획득 (9) 교묘함 유닛이 회피 +75% 획득 ```")
    if message.content.startswith('!교묘함'):
        await client.send_message(message.channel,"```나무정령수호자 루나 미라나 바람순찰자 암살기사 유령자객 자연의예언자 퍽 항마사```")
    if message.content.startswith('!기사'):
        await client.send_message(message.channel,"```(2) 다른 기사 근처로부터 1칸 안에 있는 기사 유닛은 받는 물리 및 마법 피해가 25% 감소합니다. (4) 다른 기사 근처로부터 1칸 안에 있는 기사 유닛은 받는 물리 및 마법 피해가 35% 감소합니다. (6) 다른 기사 근처로부터 1칸 안에 있는 기사 유닛은 받는 물리 및 마법 피해가 50% 감소합니다.```")
    if message.content.startswith('!기사'):
        await client.send_message(message.channel,"```루나 박쥐기수 아바돈 용기사 전능기사 혼돈기사```")
    if message.content.startswith('!드루이드'):
        await client.send_message(message.channel,"```(2) 별 등급이 가장 낮은 아군 드루이드가 한 단계 업그레이드 됩니다. (4) 별 등급이 가장 낮은 아군 드루이드 2명이 각각 한 단계 업그레이드 됩니다.```")
    if message.content.startswith('!드루이드'):
        await client.send_message(message.channel,"```고독한 드루이드 / 나무정령 수호자 / 요술사 자연의 예언자/```")
    if message.content.startswith('!마법사'):
        await client.send_message(message.channel,"```(3) 적의 마법 저항력 40% 감소 (6) 적의 마법 저항력 100% 감소```")
    if message.content.startswith('!마법사'):
        await client.send_message(message.channel,"```레이저 리나 리치 / 빛의 수호자 / 오거 마법사 / 수정의 여인 / 퍽```")
    if message.content.startswith('!명사수'):
        await client.send_message(message.channel,"```(2) 명사수 유닛은 체력이 가장 낮은 적을 집중적으로 공격합니다.```")
    if message.content.startswith('!명사수'):
        await client.send_message(message.channel,"```자이로콥터 저격수```")
    if message.content.startswith('!무자비'):
        await client.send_message(message.channel,"```(2) 적의 방어력 5 감소 (4) 적의 방어력 10 감소 (6) 적의 방어력 20 감소```")
    if message.content.startswith('!무자비'):
        await client.send_message(message.channel,"```강령 사제 / 드로우 레인저 / 리치 아바돈 퍼지```")
    if message.content.startswith('!발명가'):
        await client.send_message(message.channel,"```(2) 발명가가 체력 재생 +15 획득 (4) 발명가가 체력 재생 + 40 획득```")
    if message.content.startswith('!발명가'):
        await client.send_message(message.channel,"```기술단 땜장이 벌목꾼 자이로콥터 태엽장이```")
    if message.content.startswith('!비늘가죽'):
        await client.send_message(message.channel,"```(2) 아군이 마법 저항력 +30% 획득 (4) 아군이 마법 저항력 +50% 획득```")
    if message.content.startswith('!비늘가죽'):
        await client.send_message(message.channel,"```메두사 슬라다 슬라크 파도사냥꾼```")
    if message.content.startswith('!사냥꾼'):
        await client.send_message(message.channel,"```(3) 사냥꾼은 20% 확률로 빠르게 두 번 공격합니다. (6) 사냥꾼은 35% 확률로 빠르게 두 번 공격합니다.```")
    if message.content.startswith('!사냥꾼'):
        await client.send_message(message.channel,"```드로우 레인저 / 메두사 미라나 바람순찰자 야수지배자 저격수 파도사냥꾼```")
    if message.content.startswith('!악마'):
        await client.send_message(message.channel,"```악마 유닛이 순수 피해를 50% 더 줍니다.(대전판 위에 악마 유닛이 한 가지만 있을 때 활성화 됩니다.```")
    if message.content.startswith('!악마'):
        await client.send_message(message.channel,"```고통의 여왕 / 그림자 마귀 / 테러블레이드 파멸의 사도 / 혼돈 기사```")
    if message.content.startswith('!악마 사냥꾼'):
        await client.send_message(message.channel,"```(1) 상대의 악마 동맹 무효화 (2) 상대의 악마 동맹을 무효화 합니다. 악마 유닛이 순수 피해를 50% 더 줍니다```")
    if message.content.startswith('!악마 사냥꾼'):
        await client.send_message(message.channel,"```테러블레이드 항마사```")
    if message.content.startswith('!암살자'):
        await client.send_message(message.channel,"```(3) 암살자가 10% 확률로 300%치명타 피해 (6) 암살자가 20% 확률로 400% 치명타 피해 (9) 암살자가 30% 확률로 500% 치명타 피해```")
    if message.content.startswith('!암살자'):
        await client.send_message(message.channel,"```고통의 여왕 / 모래 제왕 / 모플링 바이퍼 슬라크 암살 기사 / 유령 자객 / 현상금 사냥꾼 / 헐귀```")
    if message.content.startswith('!야생'):
        await client.send_message(message.channel,"```(2) 아군의 공격력 +10% 획득 (4) 아군의 공격력 +25% 획득 (6) 아군의 공격력 +45% 획득```")
    if message.content.startswith('!야생'):
        await client.send_message(message.channel,"```고독한 드루이드 / 늑대인간 맹독사 모래 제왕 / 얼음폭군 요술사```")
    if message.content.startswith('!용'):
        await client.send_message(message.channel,"```(1) 용 유닛은 마나가 가득찬 상태로 전투 시작```")
    if message.content.startswith('!용'):
        await client.send_message(message.channel,"```바이퍼 용기사 퍽```")
    if message.content.startswith('!인간'):
        await client.send_message(message.channel,"```(2) 인간 유닛이 공격 시 20% 확률로 대상을 4초 동안 침묵 (4) 인간 유닛 공격 시 44% 확률로 대상을 4초 동안 침묵 (6) 인간 유닛 공격 시 66% 확률로 대상을 4초 동안 침묵```")
    if message.content.startswith('!인간'):
        await client.send_message(message.channel,"```늑대인간 리나 빛의 수호자 / 수정의 여인 / 용기사 전능기사 컨카 헐귀```")
    if message.content.startswith('!전사'):
        await client.send_message(message.channel,"```(3) 전사가 방어력 +10 획득 (6) 전사가 방어력 15% 획득 (9) 전사가 방어력 +25% 획득```")
    if message.content.startswith('!전사'):
        await client.send_message(message.channel,"```가면무사 늑대인간 도끼전사 슬라다 얼음폭군 컨카 타이니 트롤 전쟁군주 / 파멸의 사도 / 퍼지```")
    if message.content.startswith('!주술사'):
        await client.send_message(message.channel,"```(2) 무작위 적 1명이 전투 시작 시 6초 동안 개구리로 변이 ```")
    if message.content.startswith('!주술사'):
        await client.send_message(message.channel,"```그림자 주술사 / 디스럽트 / 번개 감시자 / ```")
    if message.content.startswith('!태고'):
        await client.send_message(message.channel,"```(2) 타격을 받으면, 태고 유닛이 30% 확률로 4초 동안 근접 공격자를 무장 해제합니다.(4) 타격을 받으면, 태고 유닛이 30% 확률로 4초 동안 근접 공격자를 무장 해제합니다.```")
    if message.content.startswith('!태고'):
        await client.send_message(message.channel,"```레이저 모플링 / 번개 감시자 / 에니그마 티아니```")
    if message.content.startswith('!투쟁심'):
        await client.send_message(message.channel,"```(3) 무작위 아군 한명에게 방어력 +15와 체력 재생 +10 부여 (6) 아군의 방어력 +15 및 체력 재생 +10 획득```")
    if message.content.startswith('!투쟁심'):
        await client.send_message(message.channel,"```기술단 땜장이 벌목꾼 연금술사 태엽장인 /현상금 사냥꾼```")
    if message.content.startswith('!트롤'):
        await client.send_message(message.channel,"```(2) 트롤 유닛이 공격속도 +35 획득 (4) 트롤 유닛이 공격속도 +65 획득 및 다른 아군의 공격 속도 +30 획득```")
    if message.content.startswith('!트롤'):
        await client.send_message(message.channel,"```그림자 주술사 / 박쥐기사 저주술사 / 트롤 전쟁군주```")
    if message.content.startswith('!피의 결속'):
        await client.send_message(message.channel,"```(2) 피의 결속 유닛 하나가 죽으면, 남은 전투에서 다른 모든 피의 결속 유닛이 공격 시 주는 피해가 100% 증가```")
    if message.content.startswith('!피의 결속'):
        await client.send_message(message.channel,"```오거 마법사 / 흑마법사```")
    if message.content.startswith('!흑마법사'):
        await client.send_message(message.channel,"```(2) 아군이 흡혈 +15% 획득 (4) 아군이 흡혈 +30% 획득 (6) 아군이 흡혈 +50% 획득```")
    if message.content.startswith('!흑마법사'):
        await client.send_message(message.channel,"```강령사제 / 그림자 마귀 / 맹독사 에니그마 연금술사 저주술사 흑마법사 ```")

access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
