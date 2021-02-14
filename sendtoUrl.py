import webbrowser
import time
#from pykeyboard import reply_keyboard

count = 0
urls = ['https://joshuasopuru.com/']
#k = reply_keyboard()

while count < 2:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
       #k.press_keys(['Ctrl', 'W'])
        count = count + 1

else:
    pass