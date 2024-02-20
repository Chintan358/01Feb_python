
def test():
    try:
        a = int(input("enter number : "))
        return 1;
    except Exception:
        return 0;
    finally:
         print("always execute")
        

x = test()
print(x)