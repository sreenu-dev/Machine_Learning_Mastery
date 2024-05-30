def pangrams(s):
    caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smalls="abcdefghijklmnopqrstuvwxyz"
    if len(s)<26:
        return "not pangram"
    for i in caps:
        if i not in s and smalls[caps.index(i)] not in s:
            return "not pangram"
    return "pangram"

print(pangrams("We promptly judged antique ivory buckles for the next prize"))