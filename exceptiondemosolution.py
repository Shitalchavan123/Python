
def main():
    try:
        print("Enter first number")
        no1 = int(input())

        print("Enter second number")
        no2 = int(input())
        ans = no1 / no2
        print("Division=",ans)

    except ZeroDivisionError:
        print("Inside Division error")

    except NameError:
        print("Exception occured")

    except ValueError:
        print("Inside value error")

    finally:
        print("Inside finally block")

if __name__== "__main__":
    main()