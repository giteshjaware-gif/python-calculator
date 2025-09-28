#my first python program - calculator

name=input("what is your name=")

print("Hello", name,"this is Gitesh's Personal calculator")

A = int(input("your number A="))
B = int(input("your number B="))

operation=input("operation=")

if(operation=="+"):
    print("answer is", A+B )

if(operation=="-"):
    print("answer is", A-B )

if(operation=="*"):
    print("answer is", A*B)

if(operation=="/" ):
    if(B==0):
        print("ERROR")
        print("any number divided by zero is not define")

else:
    print("answer is", A/B )

