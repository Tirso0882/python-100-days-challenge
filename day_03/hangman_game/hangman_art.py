# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"

# Colorful hangman stages (0 = dead, 6 = safe)
stages = [
# 0 lives - DEAD (all red)
f"""{RED}{BOLD}
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========={RESET}
""",
# 1 life
f"""{RED}
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========={RESET}
""",
# 2 lives
f"""{RED}
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========={RESET}
""",
# 3 lives
f"""{YELLOW}
  +---+
  |   |
  O   |
 /|   |
      |
      |
========={RESET}
""",
# 4 lives
f"""{YELLOW}
  +---+
  |   |
  O   |
  |   |
      |
      |
========={RESET}
""",
# 5 lives
f"""{GREEN}
  +---+
  |   |
  O   |
      |
      |
      |
========={RESET}
""",
# 6 lives - SAFE (all green)
f"""{GREEN}
  +---+
  |   |
      |
      |
      |
      |
========={RESET}
""",
]

logo = f"""{BOLD}{CYAN}
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    {RESET}
"""

win_art = f"""{GREEN}{BOLD}
  *   *   *   *   *
 ***  YOU WIN!  ***
  *   *   *   *   *
{RESET}"""

lose_art = f"""{RED}{BOLD}
  +-----------+
  | GAME OVER |
  +-----------+
{RESET}"""

heart_full = f"{RED}♥{RESET}"
heart_empty = f"{DIM}♡{RESET}"