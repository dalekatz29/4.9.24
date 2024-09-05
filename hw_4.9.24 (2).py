# START

grade: int = int(input("Enter your grade:"))

if 0 <= grade <=40:
    print("try harder next time...")
elif 41 <= grade <= 60:
    print("You're getting there, need some more work.")
elif 61<= grade <= 80:
    print("Pretty good")
elif 81 <= grade <= 95:
    print("Awesome!")
elif 96 <= grade <= 100:
    print("Excellent!!! You're a star!")
else:
    print("illegal grade!")

# END