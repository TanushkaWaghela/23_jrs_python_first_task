a = input("enter a number ")
f = 1
if a.isalpha():
    print("invalid input")
else:
    a=int(a);
    for i in range(1,a+1,1):
        f *= i
    print(f"the factorial is {f}")