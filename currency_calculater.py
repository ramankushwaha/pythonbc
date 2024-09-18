amount=int(input("enter your rupees in doller :"))
rate=int(input("enter your rate in rupees :"))

a=input("enter the choice \n a)rupees to doller \n b) doller to ruppees ")
if a=="a" and "A":
    print("the currency is ",rate*amount)
elif a=="b" and "b":
    print("the currency is ",amount*rate)
else:
    print("enter a valid option")