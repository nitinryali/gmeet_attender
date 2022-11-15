from time import sleep
import pyautogui as auto
import schedule, webbrowser
x = int(input("enter how many links you want? "))
print("hi")
for i in range(1,x+1):
         link = input("paste the link:").strip()
         time = input("enter time in 24hrs:").strip()


         def join():
             webbrowser.open_new_tab(link)

             sleep(5)
             auto.hotkey('ctrl', 'e')
             auto.hotkey('ctrl', 'd')
             auto.click(1374, 586)


         schedule.every().day.at(time).do(join)



while True:
    schedule.run_pending()
    sleep(1)