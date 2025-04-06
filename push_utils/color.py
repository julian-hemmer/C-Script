
#####
# MODIFIER
#####

RESET = 0
BOLD = 1
FAINT = 2
ITALIC = 3
UNDERLINE = 4
BLINK = 5
REVERSE = 7
STRIKE_THROUGH = 9

def c(text, fg=15, modifier=None, bg=None):
    seq = []
    if isinstance(modifier, list):
        seq.extend(str(m) for m in modifier)
    elif modifier is not None:
        seq.append(str(modifier))
    seq.append(f"38;5;{fg}")

    if bg is not None:
        seq.append(f"48;5;{bg}")

    return f"\033[{';'.join(seq)}m{text}\033[0m"