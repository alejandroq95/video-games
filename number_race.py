from random import randint
import os
import time

#Functions
def loading_dots(duration, interval):
    start_time = time.time()
    print("Loading Number Race")
    while time.time() - start_time < duration:
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(interval)

def main_menu():
    menu_status = True
    opt_status = True

    while menu_status:
       
        os.system('clear')
        print(":::::::::::::::::")
        print("::: MAIN MENU :::")
        print(":::::::::::::::::")
        print("[1]. Play")
        print("[2]. Help")
        print("[3]. About us")
        print("[4]. Exit")
        
        while opt_status:
            opt = int(input(".::: Press any option: "))
            if opt < 1 or opt > 4:
                print("::: Invalid option, try again :::")
            else:
                opt_status = False

        if opt == 4:
            break
#Main
os.system('clear')
loading_dots(5, 0.5)
main_menu()