def main() :
    purchase = float(input("please eneter the amount of your purchase: "))
    saletax = 0.05
    saletaxamount = purchase * saletax

    countytax = 0.025
    countytaxamount = purchase * countytax

    totaltax = countytax + saletax
    totaltaxamount = saletaxamount + countytaxamount

    print("pucheas amount: ", purchase)
    print()
    print("state tax amount: ", saletaxamount)
    print("county tax amount: ", countytaxamount)
    print("the total tax amount: ", totaltaxamount)


if __name__== "__main__" :
    main()
