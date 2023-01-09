def display(no):

    if(no>0):
        no=no-1
        print(no)
        display(no)

display(5)