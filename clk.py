import time
import os
import sys

# ANSI color codes
COLORS = {
    "-r": "\033[91m",  # Red
    "-g": "\033[92m",  # Green
    "-b": "\033[94m",  # Blue
    "-y": "\033[93m",  # Yellow
    "-m": "\033[95m",  # Magenta
    "-c": "\033[96m",  # Cyan
    "-w": "\033[97m",  # White (default)
    "reset": "\033[0m"  # Reset color
}

# Default color
selected_color = COLORS["-w"]

# Check if a color argument is provided
if len(sys.argv) > 1 and sys.argv[1] in COLORS:
    selected_color = COLORS[sys.argv[1]]

# ASCII art for digits 0-9 and ":"
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
    ],
    ":": [
        "     ",
        "  █  ",
        "     ",
        "  █  ",
        "     "
    ]
}

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        clear_screen()

        lines = ["", "", "", "", ""]
        for digit in current_time:
            for i in range(5):
                lines[i] += digits[digit][i] + "  "

        # Print the colored ASCII clock
        for line in lines:
            print(selected_color + line + COLORS["reset"])

        time.sleep(1)

if __name__ == "__main__":
    display_time()
