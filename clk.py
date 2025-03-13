import time
import os

# ASCII art for digits 0-9, each 5 lines high
digits = {
    "0": [
        " ███  ",
        "█   █ ",
        "█   █ ",
        "█   █ ",
        " ███  "
    ],
    "1": [
        "  ██  ",
        " ███  ",
        "   █  ",
        "   █  ",
        "  ███ "
    ],
    "2": [
        " ███  ",
        "█   █ ",
        "   █  ",
        " ██   ",
        "█████ "
    ],
    "3": [
        " ███  ",
        "█   █ ",
        "   ██ ",
        "█   █ ",
        " ███  "
    ],
    "4": [
        "█   █ ",
        "█   █ ",
        "█████ ",
        "    █ ",
        "    █ "
    ],
    "5": [
        "█████ ",
        "█     ",
        "█████ ",
        "    █ ",
        "█████ "
    ],
    "6": [
        " ███  ",
        "█     ",
        "█████ ",
        "█   █ ",
        " ███  "
    ],
    "7": [
        "█████ ",
        "    █ ",
        "   █  ",
        "  █   ",
        "  █   "
    ],
    "8": [
        " ███  ",
        "█   █ ",
        " ███  ",
        "█   █ ",
        " ███  "
    ],
    "9": [
        " ███  ",
        "█   █ ",
        " ████ ",
        "    █ ",
        " ███  "
    ]
}

def clear_screen():
    # Clear the screen (works on both Windows and Unix-like systems)
    os.system('cls' if os.name == 'nt' else 'clear')

def display_time():
    while True:
        # Get the current time
        current_time = time.strftime("%H%M%S")
        clear_screen()

        # Create the ASCII art for the current time
        lines = ["", "", "", "", ""]
        for digit in current_time:
            for i in range(5):
                lines[i] += digits[digit][i] + "  "

        # Print the ASCII clock
        for line in lines:
            print(line)

        # Wait for a second before updating the time
        time.sleep(1)

if __name__ == "__main__":
    display_time()