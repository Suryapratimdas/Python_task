def  print_name():
    name="SURYA"
    print(name)
print_name()    
def  Addition():
    a = int(input("Enter no for a:"))
    b = int(input("Enter no for b:"))
    c =a+b
    d =a-b
    e =a*b
    f =a/b
    print("addition=",c)
    
def  Subtraction():
    a = int(input("Enter no for a:"))
    b = int(input("Enter no for b:"))
    c=a-b
    print("subtraction=",c)
def  Multiplication():
    a = int(input("Enter no for a:"))
    b = int(input("Enter no for b:"))
    c=a*b
    print("multiplication=",c)
def  Division():
    a = int(input("Enter no for a:"))
    b = int(input("Enter no for b:"))
    c=a/b
    print("division=",c)  
while True:
    c =input("enter your choice=")
    if c=="1":
        Addition()
    elif c=="2":
        Subtraction()
    elif c=="3":
        Multiplication()
    elif c=="4":
        Division()
    else:
        print("exit")

