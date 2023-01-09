
def display(no):
    if(no>0):
        no=no-1
        display(no)
        print(no)

display(4)