#normal functions/named functions
def add(no1,no2):
    return no1+no2

#lambda functions/unnamed functions
#lambda parameters:body

addfunction=lambda a,b:a+b

ans1=add(11,10)
ans2=addfunction(10,11)

print("Addition using normal function:",ans1)
print("Addition using lambda function:",ans2)


print("Type of lambda function:",type(addfunction))