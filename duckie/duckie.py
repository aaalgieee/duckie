from random import randint

print("=================")
print("|duckie debugger|")
print("=================")

def main():
    x = input("\nyou: ")
    if x == (" "):
        x
    elif x == ("end"):
        end()
    else:
        i = randint(1, 5)
    while i < 6:
        print("quack", end=(" "))
        i = i+1
    main()
    print("\n")
main()

    