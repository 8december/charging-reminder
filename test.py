import psutil
import time
import ctypes

swi = True

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, title, text, style)


while swi:                                  #infinit while loop to keep the program running                     
    battery = psutil.sensors_battery()      
    percent = battery.percent		        #obtaining battery %	 

    time.sleep(1)

    if percent == 21 :
        Mbox("Your batter is "+ str(battery.percent) +" %  plugin the charging !", "HAHAHA !", 4096)   #pop up box

    # print('running')
  
