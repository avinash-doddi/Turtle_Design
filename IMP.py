"""to calculate the balance and balance, and delete 0.50 from balance and display balance"""
a,b=input().split()
a=float(a)
b=float(b)
c=a+0.50
if c<=b and a%5==0:
    '''calculate bal'''
    d=b-c
    print("{:.2f}".format(d))
else:
    print("{:.2f}".format(b))
