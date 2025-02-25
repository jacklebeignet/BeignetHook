from colorama import init
from termcolor import colored
import os
import shutil
import requests
import threading

# Initialize colorama for Windows compatibility
init()

# Define the ASCII art
ascii_art = """    
    ____       _                  __  __  __            __  
   / __ )___  (_)___ _____  ___  / /_/ / / /___  ____  / /__
  / __  / _ \/ / __ `/ __ \/ _ \/ __/ /_/ / __ \/ __ \/ //_/
 / /_/ /  __/ / /_/ / / / /  __/ /_/ __  / /_/ / /_/ / ,<   
/_____/\___/_/\__, /_/ /_/\___/\__/_/ /_/\____/\____/_/|_|  
             /____/                                          
"""

# Define the red-to-yellow gradient
colors = ["red", "yellow"]

# Apply the gradient to the ASCII art
colored_ascii = ""
lines = ascii_art.split("\n")
for i, line in enumerate(lines):
    color = colors[i % len(colors)]  # Alternate between red and yellow
    colored_ascii += colored(line, color) + "\n"

# Get terminal width safely
def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except OSError:
        return 80  # Default width

# Print centered text
def print_centered(text):
    print(text.center(get_terminal_width()))

# Spam function using threads (logs status codes)
def spam_webhook(webhook_url, message):
    def send_message():
        for _ in range(25):
            response = requests.post(webhook_url, json={"content": message})
            status_message = f"> {response.status_code} | "
            if response.status_code == 204:
                status_message += "SUCCESS"
            else:
                status_message += "FAILED"
            print_centered(status_message)

    thread = threading.Thread(target=send_message)
    thread.start()
    print_centered("Spamming started...")

# Delete Webhook function (logs status code)
def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    status_message = f"> {response.status_code} | "
    if response.status_code == 204:
        status_message += "SUCCESS"
    else:
        status_message += "FAILED"
    print_centered(status_message)

# Main menu
def main_menu():
    while True:
        
        print(colored_ascii)  # Print centered colored ASCII art
        print_centered("Made by Jack le Beignet on iPad")
        print("=" * get_terminal_width())  

        options = ["1. Spam Webhook", "2. Delete Webhook", "3. Exit"]
        for option in options:
            print_centered(option)

        print("\n")
        choice = input("> Enter your choice: ").strip()

        if choice == "1":
            webhook_url = input("> Enter your Discord Webhook URL: ").strip()
            message = input("> Enter the message to spam: ").strip()
            spam_webhook(webhook_url, message)
        elif choice == "2":
            webhook_url = input("> Enter your Discord Webhook URL: ").strip()
            delete_webhook(webhook_url)
        elif choice == "3":
            print_centered("Exiting...")
            break
        else:
            print_centered("Invalid choice, please try again.")
        
        input("\nPress Enter to continue...")  # Pause before refreshing

main_menu()