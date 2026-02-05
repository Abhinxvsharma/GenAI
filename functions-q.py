
def sum_even_numbers(n):
    sum=0
    for i in n:
        if i%2==0:
            sum+=i
    return sum

  
n=int(input("Enter the list size: "))
l=[]
for i in range(n):
    a=int(input("enter the element "))
    l.append(a) 

print(l)


print(sum_even_numbers(l))




