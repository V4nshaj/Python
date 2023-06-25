ch = int(input("Enter choice: "))
if ch==1:
    n=int(input("Enter the value till series gets printed: "))
    print("Fibonacci Series: ")
    a, prev=0, 1
    print(a, end=', ')
    while a<=n:
        k=a
        a=a+prev
        print(a, end=', ')
        prev=k
elif ch==2:
    n=int(input("Enter the no.: "))
    print("Multiplication upto 15: ")
    for i in range(1, 16):
        print(f"{n} * {i} = ", n*i)
else:
    print("Wrong input")