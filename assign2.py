list1 = [8, 15, 32, 42, 60, 75, 122, 132, 150, 180, 190]
def divisible(list):
    for item in list:
        if(item<120):
            if(item%4==0):
                print(item)
        else:
            break
          
t = divisible(list1)
print(t)





