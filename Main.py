from time import sleep
import os
student = {
    "change program": "To change program, please contact our staff via the",
    "discplinary office": "",
    "discplinary room": "",
    "discpline": ""
}

operating_hours = {
    "admission": "The operating hours of the admission is between 10:00 AM to 4:00 PM",
    "cashier": "The operating hours of the cashier is between 8:00 AM to 5:00 PM",
    "registrar": "The operating hours of the registrar is between 8:00 AM to 6:00 PM"
}

program = {
    "courses": "> Bachelor in  Tourism Management\n> Bachelor in Information Technology\n> Bachelor in Hospitality Management",
    "program": "> Bachelor in  Tourism Management\n> Bachelor in Information Technology\n> Bachelor in Hospitality Management"
}

fees = {
    
}

def main() -> None:
    attempts = 0
    os.system('cls')
    while attempts != 3:
        print_dialogue('Greetings, I am BOT Mika. Are you a new user? Or are you an old student?')
        user_type = input()
        if ('new' in user_type):
            new_user()
        elif ('student' in user_type or 'old' in user_type):
            student()
        else:
            print_dialogue('Sorry I did not understand what you said. Can you please repeat it for me?')
            attempts += 1
            continue
    print_dialogue('It seems that you are having a hard time, please type in "user" if you are a new user.')
    attempts = 0


def student() -> None:
    while True:
        os.system('cls')
        print('old student mode')

def new_user() -> None:
    while True:
        os.system('cls')
        print("new user mode")

def print_dialogue(text) -> None:
    for char in text:
        print(char, end="", flush=True)
        sleep(0.05)

if __name__ == "__main__":
    main()