print("We are printing triangle today as we made nothing as of now for today")

for i in range(5):
    print("")
    for j in range(i,5):
        print("  ",end='')
    for j in range(0,i):
        print("* ",end="")
    for j in range(0,i+1):
        print("* ",end="")