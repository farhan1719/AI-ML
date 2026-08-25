#how to print in python
print("Farhan ahmad")
print("Hellow World")
print("My age is 19")
print("My name is Farhan Ahmad.", "My age is 19.")
print(45)
print(33)
print(45+33)

#variable= a variable is a name given to a memory location in program.
name="Farhan"
age=19
price=25.99
age2=age
#name, age, price are variables
#and farhan, 19, 25.99 are values of variables
print("name")
print(name)
print(age)
print(price)
print(age2)
print("My name is:",name)
print("my age is:",age)
print("book price is:",price)
 #TYPER OF VARIABLES / data types of variables
print(type(name))               #name or english words rehta hai variable me to wo 'String'(str) type ka variable hota hai
print(type(age))                #age me integer values hote hain to wo 'Integer'(int) type ka variable hogahota hai
print(type(price))              #price me decimal values hote hain to wo 'Float'(float) type ka variable hota hai
old=False
a=None
print(type(old))                #old me True/False values hote hain to wo 'Boolean'(bool) type ka variable hota hai
print(type(a))                  #a me None value hai to wo 'NoneType'(None) type ka variable hota hai

#Print SUM
a=1000
b=500
sum=a+b
print(sum)

c=20
d=27
sum2=c+d
print(sum2)

E=57
F=778
sum3=E-F
print(sum3)

#Types of Operators in Python
#Arithmetic Operators
A=5
B=2

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B) # For find remainder
print(A**B) # Fro find A^B

#Relational Operators
G=10
H=20

print(G==H) #False          #for equality
print(G!=H) #True           #for not equal
print(G>=H) #False          #for greater than or equal to
print(G>H) #FAlse           #for greater than
print(G<=H) #True           #for less than or equal to
print(G<H) #True            #for less than

#Assignment Operators
num=10
#num=num+5                  #we can also write num+=5 instead of num=num+5
num+=5                      #we can also write num+=5 instead of num=num+5
print("num:",num)           #same as we can do for -=, *=, /=, %=, **=, //= operators

#Logical Operators
#not
print(not False) #True 
print(not True) #False
a=50
b=30
print(not(a>b))

#and
val1=True                               #using 'and' operator: if both values are True then only it will return True otherwise it will return False
val2=True
print("and operator:", val1 and val2)      

val1=True                               
val2=False
print("and operator:", val1 and val2)

val1=20                                 #and operator: we can also write values instead of True/False, if both values are non-zero then it will return second value otherwise it will return first value
val2=50                                 #and operator: 0 returns False and any non-zero value returns True
print("and operator:", val1 and val2)   #and operator: if your one value is 0 in both values then it will return 0 otherwise your both values are non-zero then it will return second value

val1=0
val2=50
print("and operator:", val1 and val2)

#or
val1=True
value2=False
print("or operator:", val1 or value2)      #using 'or' operator: if any one value is True then it will return True otherwise it will return False

val1=False
value2=False
print("or operator:", val1 or value2) 

print("or operator:",(a==b) or (a>b))

#Type Conversion
a=2                     #here a is integer type variable and b is float type variable, but when we add both variables then a will be converted into float type variable automatically and then it will add both variables and this automatacally conversion is a type conversion 
b=4.25                  # ans = 6.25
sum=a+b                
print(sum)             

    #a="2"                   # but if we add string type variable with integer type variable then it will give error because python does not support automatic type conversion between string and integer type variables (here python cant do type conversion automatically) so we have to convert string type variable into integer type variable manually using int() function and then it will add both variables and this manual conversion is a type conversion
    #b=4.25
    #sum=a+b
    #print(sum)              # ans= error

#Type Casting
a=int("2")                  #here we have converted string type variable into integer type variable manually using int() function and then it will add both variables and this manual conversion is a type casting
b=4.25
print(a+b)
print(type(a))

a=float("2")                #similarly we can also convert string type variable into float type variable manually using float() function and then it will add both variables and this manual conversion is a type casting
b=4.25
print(a+b)
print(type(a))

a=5.5
a=int(a)                  #here we have converted float type variable into integer type variable manually using int() function and then it will add both variables and this manual conversion is a type casting
print(type(a))

#Input in python

     #input("Enter your name:")             # Input in python : isme hum run hone ka baad bahar se input daal sakte hai

    #name=input("Enter your name:")         
    #print ("Welcome",name) 

    #age=input("Enter your age:")
    #print("Your age is:",age)
    #print(type(age))                       #here all types of values (like str,float,int) give us string value in result

    #val=input("Enter your value:")              #here value is in "int" type but when we check type of val it gives str, because in (input) value always consider like "str", chahe wo flot ya int type ka q na ho
    #rint(type(val),val)                         
                                                 #but if we want same value in "int" type then we have to convert it into "int" type using int() function and then it will give us same value in "int" type
#name=input("Enter name:")
#age=int(input("Enter age:"))                    #here we have converted string type variable into integer type variable manually using int() function and then it will give us same value in "int" type
#marks=float(input("Enter marks:"))              #sililarly we can also convert string type variable into float type variable manually using float() function and then it will give us same value in "float" type

#print("Welcome",name)
#print("age=",age)
#print("marks=",marks)



#practice Questions
# 1.write a program to input 2 numbers & print their sum.
#a=int(input("Enter your maths marks:"))
#b=int(input("Enter your physics marks:"))
#print("Total marks:",a+b)

# 2.WAP to input side of a square & print its area.
#a=float(input("Side of a Square:"))
#print("Area of a Square:",a*a)

# 3.WAP to input 2 floting point number & print their average.
#a=float(input("Your first floting value:"))
#b=float(input("Your second floting value:"))
#print("Average floting value",(a+b)/2)

# 4.WAP to input 2 int numbers, a and b.
#print True if a is grater than or equal to b, if not False.
a=int(input("a:"))
b=int(input("b:"))
print("Result:",a>=b)
print("farhan Ahmad")



