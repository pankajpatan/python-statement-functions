

def add_up(n):
    sum = 0
    if(type(n)!=int):
        return 0
    if(n>0):
        for i in range(0,n):
            sum = sum+i
    else:
        for i in range(n,0):
            sum = sum+i
    return sum

n = int(input("Enter a Number : "))
total = add_up(n)
print("Total is" + " "+ str(total))
