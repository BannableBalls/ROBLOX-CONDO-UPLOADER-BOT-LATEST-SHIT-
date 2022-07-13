import random
import secrets

import lxml.etree
fila = 'og.rbxlx'
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
doc = lxml.etree.parse(fila)
def uniqueId():
    print('UniqueId Unpatched')
    for el in doc.xpath("//UniqueId[@name='UniqueId']"):
        el.text = f'38hreouewr089erw80h3408h230h3240834h08h80eh8ds0fg0fgdh0dgfhfdg0fdg8hfg08sddf80hdfs08dshf0ds8h408h085h30854ig{secrets.token_hex(random.randrange(150, 300))}'
    doc.write(fila)
def referentt():
    print('Referent Unpatched')
    for el in doc.xpath("//Item[@referent]"):
        string = ''.join(random.choice('XSASASASASA') for i in range(random.randrange(10, 20)))
        el.attrib['referent'] = f'ds8dfifdsidfdnjfsidfsifdjnfdihdjfsidfshdouisdhoduoufgdhcv80vc0x0vbbvc80v08nbopiewhjeoprhvuovcb{string}'
    doc.write(fila)
def assetId():
    print('AssetId Unpatched')
    for el in doc.xpath("//int64[@name='SourceAssetId']"):
        el.text = f'fdggfd-fgdgf9ddfgrturteorthfdbnovjbvvcopvhbbvuycouvcbhgvobcuhbvoubvchovcbho4urhreuhwoeruhfdosghfdgohgfdofdsouhfdgohsdogs{secrets.token_hex(random.randrange(200, 500))}'
    doc.write(fila)
def scriptguilz(): 
    print(
    """
          SCRIPT GUILD
    ----MADE BY BANNABLE----
    """
    )
    for el in doc.xpath("//string[@name='ScriptGuid']"):
        el.text = '{'f'{random.choice(hereweare)}''-DFFDSGUOHSDFOUDSFHOUSDHFUSODHFODGHFGGFHDUOFDHOUHSDFOUFGDHBDSIHIFHDGIFGDOGFDOVBHUDOFUSHSDFSDFOUHFSDOHDFSOUGFHOFDHUVBCOUVCBHVCB80VBVC80804800858043580FDHUO-'f'{random.choice(hereweare)}''-bluadsadskldaslkdaskllkdasescreentatsme}'
    doc.write(fila)

