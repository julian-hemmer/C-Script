
#####
# MODIFIER
#####

RESET = 0
BOLD = 1
UNDERLINE = 4
BLINK = 5
REVERSE = 7

def c(text, color = 0, modifier = RESET):
    return f"\033[{modifier};{color}m{text}\033[0m"