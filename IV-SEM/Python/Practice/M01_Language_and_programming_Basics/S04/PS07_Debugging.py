'''bug-->errors
debugging --> finding and fixing of errors

Types of errors:
   1) Syntax error (indentation , missing of colon)
   2) Runtime error (division by zero)
   3) Logical error (missing of logics)

   Debugging Techniques:
     1) print()
     2) try-except
     3) using pdb 
     purpose: 
     1) Pause the execution 
     2) inspect the variable's value 
     3) to run the code line by line

   pdb Commands:
   1)n--> to excute the output in next line
   2)p variable --> to get the value of a variable
   3)l --> List nearby code 
   4)c--> continue the execution 
   5)s--> to start  a function
   6)r--> return from the function
   7)h--> help 
   8)q-->   quit the execution

   
try: 
    a = int(input("Enter a num: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by Zero. ")
except ValueError:
    print("Invalid input")

    '''
import pdb 
def add(a,b):
    pdb.set_trace() #set the breakpoint 
    return a+b 
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print(add(a,b))