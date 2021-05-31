import os, sys, subprocess
from subprocess import call, Popen
import time
import I2C_LCD_driver


# Initialize LCD drivers
mylcd = I2C_LCD_driver.lcd()

try:
    while True:
        text = input("Enter: ")
        process = Popen(["pico2wave","-w","test.wav",text], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        out ,err = process.communicate()
        if os.path.isfile("test.wav"):
            process = Popen(["aplay","test.wav"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            out, err = process.communicate()
            os.remove("test.wav")
        else:
            print('Could not convert text. See error:\n',err)
            continue
        if len(text)<=16:
            mylcd.lcd_clear()
            mylcd.lcd_display_string(text.capitalize(),1)
            time.sleep(0.5)
        elif len(text)<=32:
            mylcd.lcd_clear()
            mylcd.lcd_display_string(text[:16].capitalize(),1)
            mylcd.lcd_display_string(text[16:],2)
            time.sleep(0.8)
        elif len(text)>32:
            mylcd.lcd_clear()
            str_pad = " " * 4
            text = str_pad+text.capitalize()+" "
            for i in range(0,len(text)):
                lcd_text = text[i:i+16]
                mylcd.lcd_display_string(lcd_text,1)
                time.sleep(0.15)
            mylcd.lcd_clear()
except:
    #print(str(e))
    mylcd.lcd_clear()
    sys.exit(0)
