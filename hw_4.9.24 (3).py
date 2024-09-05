# START

vol: int = int(input("Write a volume level you want from 0 to 10: "))

while vol < 0 or vol > 10:
    print("invalid volume, try again...")
    vol: int = int(input("Write a volume level you want from 0 to 10: "))
match vol:
    case 0:
        print("mute")
    case 1 | 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud")

# END
