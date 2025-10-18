def main():
    x = int(input("Please type a number: "))

    if x >= 0:
        print("The abs of ", x)

    elif x<= 0:
        y = x * -1
        print("The abs of ", x, "is ",y)

main()
