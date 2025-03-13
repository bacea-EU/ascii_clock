import time
import os
import sys
import curses

# !!! pip install windows-curses !!!

# ANSI color codes
COLORS = {
    "-r": "\033[91m",  # Red
    "-g": "\033[92m",  # Green
    "-b": "\033[94m",  # Blue
    "-y": "\033[93m",  # Yellow
    "-m": "\033[95m",  # Magenta
    "-c": "\033[96m",  # Cyan
    "-w": "\033[97m",  # White
    "reset": "\033[0m"  # Reset color
}

# Default color
selected_color = COLORS["-w"]

# Color argument
if len(sys.argv) > 1 and sys.argv[1] in COLORS:
    selected_color = COLORS[sys.argv[1]]

# Digit representation
digits = {
    "0": [
        " ███  ",
        "█   █ ",
        "█   █ ",
        "█   █ ",
        " ███  "
    ],
    "1": [
        "   █  ",
        "  ██  ",
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

def display_time(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate (100ms for smoothness)
    last_time = ""
    while True:
        current_time = time.strftime("%H:%M:%S")
        
        if current_time != last_time:  # Update only if time has changed
            stdscr.clear()
            lines = ["", "", "", "", ""]
            
            for digit in current_time:
                for i in range(5):
                    lines[i] += digits[digit][i] + "  "
            
            for i, line in enumerate(lines):
                stdscr.addstr(i + 2, 5, line)  # Positioning on screen
            
            stdscr.refresh()
            last_time = current_time  # Store last displayed time

        if stdscr.getch() == ord('q'):  # Allow quitting with 'q'
            break

def main():
    curses.wrapper(display_time)

if __name__ == "__main__":
    main()
