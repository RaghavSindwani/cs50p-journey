def main():
    printsquare(4)

def printsquare(size):
    for i in range(size):
        printrow(size)

def printrow(width):
    print("#" * width)


main()
