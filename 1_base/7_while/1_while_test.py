a=1
sum=0

def sum_add(num):
    a=1
    sum=0
    while a<num:
        sum = sum+a
        a+=1
    return sum

sum = sum_add(10)
print("sum:",sum)