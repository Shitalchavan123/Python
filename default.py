def Area(radius,pi=3.14):
    result=pi*radius*radius
    return result

def main():
    rvalue=10.5
    pivalue=3.14
    ans=Area(rvalue,pivalue)

    ans=Area(pi=pivalue,radius=rvalue)
    print("Area of circle:",ans)

    ans=Area(10.5)
    print("Area of circle:",ans)

    ans = Area(radius=10.5)
    print("Area of circle:", ans)

    ans = Area(pi=7.10,radius=10.5)
    print("Area of circle:", ans)

if __name__ == "__main__":
    main()