from asyncio.windows_events import NULL
from http import client
from msilib.schema import Component
import sys
import asyncio
from traceback import print_tb
from turtle import title
import discord
from requests import post, get
import requests
import discord_ui
from os import name as os_name, system
from discord_ui import UI, LinkButton, Button
from discord import Webhook, RequestsWebhookAdapter, embeds, Embed
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
from discord.ext import commands
from unblacklister import uniqueId, referentt, assetId, scriptguilz
import os
import secrets
import random
from ad import advertise
from keep_alive import keep_alive
import codecs
import lxml.etree
from xml.dom import minidom
from xml.etree import ElementTree as etree
import discord_buttons_plugin
from discord_buttons_plugin import *
from time import sleep
import requests, base64, random, string
import itertools
bot = commands.Bot(command_prefix=".") #prefix for command

buttons = ButtonsClient(bot)
gamenames = [
  '[2x🍀+HEROES]Anime Warriors Simulator',
  'Sword Factory X⚔️ [x3 LUCK! 🎉]',
  '[🔥 🔵 UPDATE]Blox Fruits',
  '[🥚 EVENT!] Pet SimulatorX! 🐾',
  '☣️ Hospital Roleplay ☣️',
  '[UPD] ⚡Clicker Simulator!',
  '[UPD 9.5 + x2💎+ x3🗡️] Slashing Simulator🗡️',
  '[🌊 Second Sea]A 0ne Piece Game',
  '[📈TRADE UPDATE]Grand Piece Online',
  '💥 Super Power Training Simulator 💥',
  '[🔥ASCEND!]Lifting Gods 2 💪',
  '[✨UPDATE!✨ ]Super Tappers!',
  '[🌟Free x999,999,999T+ Pet🌟]Secret Hatching Sim',
  '[x2💰] ⚽Goal Kick Simulator',
  '💎+100%💥 Bot Clash!',
  '⚔️ Warriors Army Simulator!',
  '🌸 Vibe Place (ORIGINAL)',
  '[🔊 Voice Chat] Vibe Hugs 💙',
]
"""
  ____                          _     _      
 |  _ \                        | |   | |     
 | |_) | __ _ _ __  _ __   __ _| |__ | | ___ 
 |  _ < / _` | '_ \| '_ \ / _` | '_ \| |/ _ \
 | |_) | (_| | | | | | | | (_| | |_) | |  __/
 |____/ \__,_|_| |_|_| |_|\__,_|_.__/|_|\___|
                                             
    Powering Roblox Condos I guess idk.

    Credits: 
    Roblox Thot#0001 - Doing the captcha token thing
    Bannable#4229 - Making the full source of the bot
    
    Many people wonder who tf is AsyncRef, well basically that was me (Bannable) all I did was change my indentity in order
    to save my reputation on the condo community. But that's it, you'll see that it will be credited seperately but i'm actually async.
    lol. Proof if you check my discord account Bannable#4229 you'll see my github AsyncRef.

"""
hereweare = [
  'fdsakjsafdkjafsdkj',
  'Sdsfjksadfkjkjdsafkjsadfkj899889skjdf',
  'jfskdksdfakjfadskjsd94893494',
  '[67898765tyghjhuyghj',
  '67yujkjiuy7t6789',
  'mamamsmmsamksaksa9sa98as98s9a8',
  'asjkaskjasjkkjaskjaskji92949294942',
  'asklsalk9as98sa98sa8989as89s8a9',
  'sa989sa89sa89as99sa9as9sa989as',
  'mamamams98as8989s89sa89as98s9a',
  'bananblexdandxaviontopnmfmfmfmff8489498489',
  'fckworldhistorybrooooooooooooooooo',
  'ihaterobloxadminsxdsocooccclcllcocolcoclccococlclclclcl',
]
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Lust Condos', url='https://www.twitch.tv/'))

def webhook(gameident):
    print("Starting Webhook")



fila = 'Module.rbxmx'

doc = lxml.etree.parse(fila)
def UIZ():
    print('UniqueId Unpatched')
    for el in doc.xpath("//UniqueId[@name='UniqueId']"):
        el.text = f'F9FDF9DGJFGIFDIifdgifdgifdghfd80fdgh0gfdhfdg0ofdghfdgofhdguo4g3huo43hofglhol93prewewriewroptretirpe{secrets.token_hex(random.randrange(200, 500))}'
    doc.write(fila)
def REF():
    print('Referent Unpatched')
    for el in doc.xpath("//Item[@referent]"):
        string = ''.join(random.choice('LOL') for i in range(random.randrange(15, 30)))
        el.attrib['referent'] = f'ewrewrewruerwewropiewyrpoewre08ryr803h34fsuhdsfudsfdfsjbjfdg540345y8034hdsogfikhgfndjk435453{string}'
    doc.write(fila)
def AI():
    print('AssetId Unpatched')
    for el in doc.xpath("//int64[@name='SourceAssetId']"):
        el.text = f'432j43erwujewhewuoerhoeuwhreoudfofdghofdghgfdolfdgjnehewrohdfsoohfgoddhfosdhodufhdf8043h05hodhfdoghnjlk{secrets.token_hex(random.randrange(100, 200))}'
    doc.write(fila)
def SG(): 
    print('ok')
    for el in doc.xpath("//string[@name='ScriptGuid']"):
        el.text = '{'f'{random.choice(hereweare)}''-fdggfduofhdgfgodhfgdohdfgo0h4reoretotreoutrewqepfgdjnbmcvcxnvcxucoivuioboubcvxkjbcxvoucxvhvc09x7cvxdfvbiebwpjbpdfpijdfsp654-'f'{random.choice(hereweare)}''-sunshindlaskadskldasklslaade5995}'
    doc.write(fila)


def main(cookie):
   # fp = open('og.rbxlx', 't')
   # fp.write('ok')
  #  fp.close()
    
    AI()
    SG()
    REF()
    UIZ()
    
    uniqueId()
    referentt()
    assetId()
    scriptguilz()
    
    token = post("https://auth.roblox.com/v2/logout", 
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["id"]
    print(f" [DATA] {userId} - UserID")
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(f" [DATA] {gameId} - GameID")
    
    N = 2
    for i in itertools.repeat(None, 2):
     model = open("Module.rbxmx", "rb").read()
    uploadmodel = post("https://data.roblox.com/Data/Upload.ashx?assetid=0&type=Model&name=debugroblocksxd&description=supxd&genreTypeId=4&ispublic=false&allowcomments=true", 
 
                 headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox', 
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie}, 
                  data=model)

    print(f" [DATA] {uploadmodel.status_code} - Success uploading assset model.")  
    
    modelid = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/10?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(f"The Model ID = {modelid}")
    with open("og.rbxlx",'r') as f:
     get_all=f.readlines()
    with open("og.rbxlx",'w') as f:
     for i,line in enumerate(get_all,1):            
        if i == 861:                             
            f.writelines(f'                    <double name="Value">{modelid}</double>                                                                                                                                                                                                                                               ')
        else:
            f.writelines(line)
    
    myfiles = open("og.rbxlx", "rb").read()
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print(f" [DATA] {unvid} - UniverseID")
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    avatartype = "MorphToR6"
    allowprivateservers = True

    gamedatao = {
        "name": random.choice(gamenames) ,
        "description": """Where has my master gone? I am a good dog, so I must find him. 

Doggy doesn't mean any trouble, but sometimes he accidentally breaks things.

🔔🔔🔔 Make sure to hit the FOLLOW button to get notified when more stuff is added 🔔🔔🔔

--- Updates ---

🔮 MARBLE level (April 2022)
😴 NAP and DROPPER levels

They should call this Epic Shiba Simulator -Snowi Fox,""",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "maxPlayerCount": 50,
        "allowPrivateServers": allowprivateservers,
        "privateServerPrice": 0,
        "permissions": {
            "IsThirdPartyTeleportAllowed": True,
            "IsThirdPartyPurchaseAllowed": True
        }
    }
    gameDump = json.dumps(gamedatao)
    gamestats = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameDump)
    gameData2 = {
        "maxPlayerCount": 55,
    }
    gamestat = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameData2)
    print(f" [DATA] {gamestat.status_code} - Successfull upload")
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox', 
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)  
    if upload.status_code == 400:
       print("works")
       webhook(gameId)

    global link
    link =  gameId
def captchatoken(token):
    print("Starting.")
    headers = {
    'authority': 'auth.roblox.com',
    'dnt': '1',
    'x-csrf-token': requests.post("https://auth.roblox.com/v2/login").headers["x-csrf-token"],
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    }

    username = 'q'.join(random.choice(string.ascii_letters) for i in range(8))
    
    tokens = base64.b64decode(token).decode('utf-8').split(',')
    data = {
    "username":username,
    "password":"122121212ddd", #doesnt even matter lol?
    "birthday":"01 Oct 1999",
    "gender":2,
    "isTosAgreementBoxChecked":True,
    "context":"MultiverseSignupForm",
    "referralData":None,
    "displayAvatarV2":False,
    "displayContextV2":False,
    "captchaId":tokens[0],
    "captchaToken":tokens[1],
    "captchaProvider":"PROVIDER_ARKOSE_LABS",
    "agreementIds":['54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3','848d8d8f-0e33-4176-bcd9-aa4e22ae7905']
  
    }

    response = requests.post('https://auth.roblox.com/v2/signup', headers=headers, json=data)
    print(response)
    print(username)
    try:
       cookiez = response.cookies[".ROBLOSECURITY"]
       print()
      # print(f'login: {username}:{username[::-1]}')
       print(f'\nCookie:\n{cookiez}')
       main(cookiez)
    except:
       print("Failed to create account.")
       pass
@bot.command()
@commands.has_permissions(administrator=True) 
async def file(ctx):
    if ctx.author == bot.user: 
        return
    print("File Upload Mode Initiated")
    embed = discord.Embed(
            title = "Please Insert a Valid File",
        )
    embed.set_footer(text='Created by Bannable#4229')
    sent = await ctx.send(embed=embed) 
    #discontinued0
@bot.command()
@commands.has_permissions(administrator=True) 
async def upload(ctx):
    if ctx.author == bot.user: 
        return
    await ctx.send("Insert a valid captcha token to upload.")
    tokenz = await bot.wait_for("message")
    captchatoken(tokenz.content)
@bot.command()
@commands.has_permissions(administrator=True) 
async def condo(ctx):
  if ctx.author == bot.user:
    return
  embed = discord.Embed(
            title = "Please Insert a Valid Cookie",
        )
  embed.set_footer(text='Created by Bannable#4229')

  sent = await ctx.send(embed=embed)  
  cookieinput = await bot.wait_for("message")
  if '_|WARNING' in cookieinput.content:
         embed = discord.Embed(
            title = "Valid Cookie...",
        )
         embed.set_footer(text='Created by Bannable#4229')

  else:
     await ctx.send("Invalid Cookie")
     return
  sent = await ctx.send(embed=embed) 
  await ctx.send("Successfully Uploaded Game")
  main(cookieinput.content)
  await buttons.send(
		content = "Game-Link Below",
		embed = None,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Game-Link",
					url = f"https://www.roblox.com/games/{link}/"
				)
			])
		]
	)
  
@bot.command()
@commands.has_permissions(administrator=True) 
async def ad(ctx):
   await ctx.send("Advertising game...")
   advertise(link)
   await ctx.send("sucessfully advertised the game!")


@bot.command()
@commands.has_permissions(administrator=True) 
async def a(ctx):
    embed = discord.Embed(title="New Condo Uploaded.", color=0xdd1c1c, description="Click the game-link button below in order to have access to play our condos.")
    embed.set_footer(text="Made by Bannable#4229 | Lust Condos")
    await buttons.send(
		content = " ",
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Game-Link",
					url = f"https://www.roblox.com/games/{link}/"
				)
			])
		]
	)
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True) 
async def invite(ctx):
	embed = discord.Embed(title=f"Invite {bot.user.name}", color=0xff0000, description=f"Wanna invite {bot.user.name}, then [click here](https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot)")
	await buttons.send(
		content = None,
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Invite",
					url = f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
				)
			])
        ]
    )
keep_alive()
bot.run('OTY2ODIwNDAwMDI3ODI0MjI4.YmHTqg.u_VJHfDYwdEAqoMd6Kvy2l0Qcgo')

