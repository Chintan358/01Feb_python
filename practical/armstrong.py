
number = int(input("enter number : "))
#153
temp = number
sum = 0;
while number>0:
    rem = number%10
    sum += rem**3
    number //= 10


if(sum==temp):
    print("armstrong")
else:
    print("not armstron")