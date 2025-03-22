import time
import sys
import curses

# Define color mappings for curses
COLOR_MAPPING = {
    "-r": curses.COLOR_RED,
    "-g": curses.COLOR_GREEN,
    "-b": curses.COLOR_BLUE,
    "-y": curses.COLOR_YELLOW,
    "-m": curses.COLOR_MAGENTA,
    "-c": curses.COLOR_CYAN,
    "-w": curses.COLOR_WHITE
}

# Default color
selected_color = "-w"  # White

# Color argument handling
if len(sys.argv) > 1 and sys.argv[1] in COLOR_MAPPING:
    selected_color = sys.argv[1]

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
        "  █   ",
        " ██   ",
        "  █   ",
        "  █   ",
        " ███  "
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
    curses.start_color()
    curses.init_pair(1, COLOR_MAPPING[selected_color], curses.COLOR_BLACK)  # Set text color
    color_pair = curses.color_pair(1)

    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100)  # Refresh rate (100ms for smoothness)
    
    last_time = ""

    while True:
        height, width = stdscr.getmaxyx()  # Get screen size
        current_time = time.strftime("%H:%M:%S")

        if current_time != last_time:  # Update only if time has changed
            stdscr.clear()
            lines = ["", "", "", "", ""]
            
            for digit in current_time:
                for i in range(5):
                    lines[i] += digits[digit][i] + "  "
            
            # Calculate center position
            clock_width = len(lines[0])
            start_x = (width - clock_width) // 2
            start_y = (height - 5) // 2
            
            for i, line in enumerate(lines):
                stdscr.addstr(start_y + i, start_x, line, color_pair)  # Apply color
            
            stdscr.refresh()
            last_time = current_time  # Store last displayed time

        if stdscr.getch() == ord('q'):  # Allow quitting with 'q'
            break

def main():
    curses.wrapper(display_time)

if __name__ == "__main__":
    main()
