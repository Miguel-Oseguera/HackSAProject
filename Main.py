print("Is this your first time? (yes or no)")
userAns = input()
if userAns.upper() == "YES":
    print("hi")
elif userAns.upper() == "NO":
    print("hello")
else:
    print("please input a valid answer.")