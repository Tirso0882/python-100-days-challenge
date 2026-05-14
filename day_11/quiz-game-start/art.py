# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

LOGO = f"""
{CYAN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  {YELLOW}{BOLD}  ██████╗ ██╗   ██╗██╗███████╗██╗   ██╗██╗██╗██╗██╗  {RESET}{CYAN}║
║  {YELLOW}{BOLD} ██╔═══██╗██║   ██║██║╚══███╔╝╚██╗ ██╔╝██║██║██║██║  {RESET}{CYAN}║
║  {YELLOW}{BOLD} ██║   ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║██║██║██║  {RESET}{CYAN}║
║  {YELLOW}{BOLD} ██║▄▄ ██║██║   ██║██║ ███╔╝    ╚██╔╝  ╚═╝╚═╝╚═╝╚═╝  {RESET}{CYAN}║
║  {YELLOW}{BOLD} ╚██████╔╝╚██████╔╝██║███████╗   ██║   ██╗██╗██╗██╗  {RESET}{CYAN}║
║  {YELLOW}{BOLD}  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝╚═╝╚═╝  {RESET}{CYAN}║
║                                                               ║
║  {MAGENTA}{BOLD}    🧠  "Quizzy McBrainrot" — The Brain Buster! 🧠   {RESET}{CYAN}  ║
║  {WHITE}      Are you smarter than a confused goldfish? 🐟       {RESET}{CYAN}║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{RESET}
"""

CORRECT_ART = f"""{GREEN}{BOLD}
    ✓✓✓   CORRECT!   ✓✓✓
    🎉  Big brain energy!  🎉
{RESET}"""

WRONG_ART = f"""{RED}{BOLD}
    ✗✗✗   WRONG!   ✗✗✗
    💀  Oof, that stings!  💀
{RESET}"""

GAME_OVER_ART = f"""
{MAGENTA}╔══════════════════════════════════════╗
║  {YELLOW}{BOLD}     🏁  GAME OVER  🏁          {RESET}{MAGENTA}    ║
╚══════════════════════════════════════╝{RESET}
"""

PERFECT_SCORE_ART = f"""{YELLOW}{BOLD}
    ⭐⭐⭐  PERFECT SCORE!  ⭐⭐⭐
    🧠 You are a certified GENIUS! 🧠
    👑 Bow down to the Quiz Monarch! 👑
{RESET}"""

STREAK_MESSAGES = [
    f"{GREEN}🔥 2 in a row! You're warming up!{RESET}",
    f"{YELLOW}🔥🔥 3 streak! On fire!{RESET}",
    f"{RED}🔥🔥🔥 4 streak! UNSTOPPABLE!{RESET}",
    f"{MAGENTA}💥💥💥💥 5+ streak! ARE YOU EVEN HUMAN?!{RESET}",
]

TAUNT_MESSAGES = [
    "Come on, even my cat knows this one! 🐱",
    "Your grandma called — she got this right! 👵",
    "A goldfish could answer this... probably. 🐟",
    "Legend says the answer is in your heart. ❤️",
    "Think harder... or just guess. No judgment. 🤷",
    "Plot twist: the answer might surprise you! 😱",
    "Pro tip: one of the answers is correct! 🧐",
]
