import requests
import time
import os
def advertise(gameId):
    link222 = f'https://www.roblox.com/games/{gameId}/'
    messageE = f'''
    :heart_on_fire: | Lust Games | :heart_on_fire:
     {link222}
  '''
    jsonn = {
        'content': f'{messageE}',
        'tts': 'false'
    }

    headers = {
        'authorization': 'OTQ5ODIwNTEyNDkyNzQwNjY5.Yl1Cfw.x-0EWXkMl8oxFX-mx30iEDH63A8'
    }
    #UKIYOTHING
    r5 = requests.post('https://discord.com/api/v9/channels/959220260572123167/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r5.status_code == 429:
        sheesh = r5.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r5.status_code == 200:
        print("   Success sent message ")
    else:
        print(r5.status_code)
        #Black
    r6 = requests.post('https://discord.com/api/v9/channels/927360422707867658/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r6.status_code == 429:
        sheesh = r6.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r6.status_code == 200:
        print("  Success sent message ")
    else:
        #CONDO LINKS
        print(r6.status_code)
    r7 = requests.post('https://discord.com/api/v9/channels/967976916927807529/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r7.status_code == 429:
        sheesh = r7.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r7.status_code == 200:
        print("  Success sent message ")
    else:
        #LUST
        print(r7.status_code)
    r8 = requests.post('https://discord.com/api/v9/channels/970858540996628500/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r8.status_code == 429:
        sheesh = r8.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r8.status_code == 200:
        print("  Success sent message ")
    else:
        print(r8.status_code)
        #p.wiwat
    r9 = requests.post('https://discord.com/api/v9/channels/934536493077241876/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r9.status_code == 429:
        sheesh = r9.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r9.status_code == 200:
        print("  Success sent message ")
    else:
        print(r9.status_code)
    #POKEY
    r10 = requests.post('https://discord.com/api/v9/channels/953398140931801088/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r10.status_code == 429:
        sheesh = r10.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r10.status_code == 200:
        print("  Success sent message ")
    else:
        print(r10.status_code)
     #C00LKIDD CONDOS
    r11 = requests.post('https://discord.com/api/v9/channels/960899659549794334/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r11.status_code == 429:
        sheesh = r11.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r11.status_code == 200:
        print("  Success sent message ")
    else:
        print(r10.status_code)
        #R CONDO
    r12 = requests.post('https://discord.com/api/v9/channels/948023982777565214/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r12.status_code == 429:
        sheesh = r12.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r12.status_code == 200:
        print("  Success sent message ")
    else:
        print(r12.status_code)
        #HENTAI SOCIETY
    r13 = requests.post('https://discord.com/api/v9/channels/954474950910164992/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r13.status_code == 429:
        sheesh = r13.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r13.status_code == 200:
        print("  Success sent message ")
    else:
        print(r13.status_code)
        #CONDOHUB
    r14 = requests.post('https://discord.com/api/v9/channels/957113159284576286/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r14.status_code == 429:
        sheesh = r14.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r14.status_code == 200:
        print("  Success sent message ")
    else:
        print(r14.status_code)
#XHUB
    r1000 = requests.post('https://discord.com/api/v9/channels/908880597915676702/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r1000.status_code == 429:
        sheesh = r1000.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r1000.status_code == 200:
        print("  Success sent message ")
    else:
        print(r1000.status_code)
