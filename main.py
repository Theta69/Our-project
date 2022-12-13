try:
    import os,sys,requests,json,readchar,PyQt5;from pystyle import Colorate,Colors,Center;from colorama import Fore;from PyQt5.QtWidgets import *
except ImportError:
    print('stop crying python fr abeisneveid wazavazenei') # what no icea 🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊

try:
    print(2 + 'lol' + False + 0.5) #ohio code fr
except:
    print('fatal error i cant live without this code working i 🤯need ice!!§§§🧊🧊🧊🧊🧊🧊😱😱')#LMAO THE SHOCKED EMOJI ALWAYS MAKE ME LAUGH SO HARD LMAo ☠️☠️☠️ fr # i think i have homework for tmr i have to do it L:( holy shit well go do it then lmfao ok imma close this bye bye :pensive: cya tlomormrowao😱😱😱😱😱😱😱 what is that word it's ohioish it means "tomorrow" i guess
    pass

version = 0.1 #float 😎 fr
App = QApplication(sys.argv)
def rgb_to_dec(r, g, b):
  return (r * 256 * 256) + (g * 256) + b
def PickColor():
    return QColorDialog.getColor()
def clear():os.system('cls' if os.name=='nt' else 'clear')
title='''
██████╗░░█████╗░██████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗████╗░██║
██████╔╝██║░░██║██████╔╝██╔██╗██║
██╔═══╝░██║░░██║██╔══██╗██║╚████║
██║░░░░░╚█████╔╝██║░░██║██║░╚███║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝'''
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(title))+"\n\n")
def ourInput(text:str):return input(text) #hehe what does it do? no idea LMFAO it just copies input() nice LMAO ☭LMFAO
usercontent = ourInput("what should be the contnet fr: ")
if usercontent == "devmode":
    ourInput("congratulations you found the developer mode and won absolutely nothing, you are a disgrace 👍🏼") #lmao
username = ourInput("whayt about the usnername then.?,,§§§: ")
av = ourInput("and the avatar? ('' for default): ") # i have an image checker dw oh okay so should i remove this line? nice
col=PickColor()
ourColor = rgb_to_dec(col.getRgb()[0], col.getRgb()[1], col.getRgb()[2])
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False
if av.replace(" ", "") !="":
    if is_url_image(av):img=av.replace(" ", "")
    else: img=""
else:img=""
embedtitle = ourInput("custom embed title?: ")
embeddesc = ourInput("embed description: ") #wait wait weait wai https://gist.github.com/Birdie0/78ee79402a4301b1faf412ab5f1cdcf9 so what do i do with the description
def SendToWebhook():
    jsn = {
        'content': usercontent,
        'username': f"PornHub: {username} | Version {version}", #it should still be pornhub tho
        'avatar_url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/591b4730-4d50-4925-a14d-0676b95bfbd5/de0703b-a98dd548-f300-49ec-b4a5-d8b23ab208a0.jpg',
        'embeds': [
            {
                'title': f'Pornhub - {embedtitle}',
                'description': f'{embeddesc}\n\n*-sent by PornHub Webhook*',
                'thumbnail': {
                    'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/591b4730-4d50-4925-a14d-0676b95bfbd5/de0703b-a98dd548-f300-49ec-b4a5-d8b23ab208a0.jpg'
                },
                'color': ourColor
            }
        ],
    }
    requests.post('https://discord.com/api/webhooks/1052351803494236331/f-MetzLWunvMf_Aof_H9YsiNUUTO9M0Y951iP6INtCGndMFye5M0jRS6TD-38sCpCmgu', json=jsn)
    pass

# clear()
# startMenu()
SendToWebhook()