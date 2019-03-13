def win_or_lose(stra,strb):
    if len(stra)>len(strb):
        return "a win!"
    if len(stra)<len(strb):
        return "a lose..."
    if stra>strb:
        return "a win!"
    if stra<strb:
        return "a lose..."
    return "a doesn't win... and a doesn't lose..."
print(win_or_lose("2007","323"))
print(win_or_lose("323","323"))