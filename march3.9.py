#Exception Handling
x=5
y=0
try:
    z=int(input())
    print(x/y)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError as e:
    print("Can't convert int to str",e)
except Exception as e:
    print("Invalid",e)    
print("bye")