def add(no):
    print("Enter the element")
    no=int(input())
    ans=0

    while(no>=0):
        ans=ans+no
        no=no-1
    return ans
no=0
ret=add(no)

print(ret)