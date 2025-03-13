# Dynamic ASCII Clock

This is a Python-based dynamic ASCII clock that displays the current system time in a visually appealing format using ASCII characters. It updates smoothly without flashing and supports color customization.

## Features
- Displays the current time in a large ASCII format.
- Uses `curses` for smooth updates without screen flickering.
- Supports multiple color options
- Non-blocking execution with a refresh rate for smooth transitions.
- Press `q` to exit the clock.

## Prerequisites

Ensure you have Python installed on your system.  
If you're using **Windows**, install the `windows-curses` package:

```sh
pip install windows-curses
```

## Usage

Run the script with an optional color argument:

```sh
python clock.py [-r | -g | -b | -y | -m | -c | -w]
```

## Color Options:
- `-r` → Red
- `-g` → Green
- `-b` → Blue
- `-y` → Yellow
- `-m` → Magenta
- `-c` → Cyan
- `-w` → White (default)
