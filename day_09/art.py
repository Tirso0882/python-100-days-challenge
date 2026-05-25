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

BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"

PLAYER_COLORS = [GREEN, CYAN, MAGENTA, YELLOW]


logo = f"""{BOLD}{GREEN}
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/{RESET}
"""

vs = f"""{BOLD}{RED}
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_){RESET}
"""

lose_art = f"""{RED}{BOLD}
  +-----------+
  | GAME OVER |
  +-----------+
{RESET}"""

win_art = f"""{GREEN}{BOLD}
  +----------------+
  |  NEW HIGH SCORE |
  +----------------+
{RESET}"""

crown_art = f"""{YELLOW}{BOLD}
       .:::.
      ::::::.
  .::::::::::::.
  ':'''''''''':'
    ':::::::::'
      ':::::'
{RESET}"""

streak_art = f"""{YELLOW}{BOLD}
  **  STREAK! **
{RESET}"""

trophy_art = f"""{YELLOW}{BOLD}
      ___________
     '._==_==_=_.'
     .-\\:      /-.
    | (|:.     |) |
     '-|:.     |-'
       \\::.    /
        '::. .'
          ) (
        _.' '._
       '-------'
{RESET}"""

def scoreboard_art(players):
    """Generate a dynamic scoreboard for all players."""
    lines = []
    lines.append(f"{BOLD}{CYAN}{'=' * 40}")
    lines.append(f"{'SCOREBOARD':^40}")
    lines.append(f"{'=' * 40}{RESET}")
    sorted_players = sorted(players, key=lambda p: p['score'], reverse=True)
    for i, player in enumerate(sorted_players):
        color = PLAYER_COLORS[player['index'] % len(PLAYER_COLORS)]
        medal = ""
        if i == 0:
            medal = " << LEADER"
        bar = "#" * min(player['score'], 20)
        streak_txt = f" (streak: {player['streak']}!)" if player['streak'] >= 3 else ""
        lines.append(f"  {color}{BOLD}{player['name']:>12}{RESET}: {player['score']:>3} pts  {GREEN}{bar}{RESET}{streak_txt}{medal}")
    lines.append(f"{CYAN}{BOLD}{'=' * 40}{RESET}")
    return "\n".join(lines)


def turn_banner(player_name, player_index):
    """Show whose turn it is."""
    color = PLAYER_COLORS[player_index % len(PLAYER_COLORS)]
    return f"\n{color}{BOLD}>>> {player_name}'s turn! <<<{RESET}\n"


