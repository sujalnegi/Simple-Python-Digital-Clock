import os
import time

while True:   
    t = time.strftime("%Y/%B/%d %A %H:%M:%S")
    # print("YYYY/MM/DD Day HH:MM:SS Time Zone")
    # print("|||| || || ||| |||||||| |||| ||||")
    print(t) #Printing Real time
    time.sleep(1) 
    os.system("cls")
