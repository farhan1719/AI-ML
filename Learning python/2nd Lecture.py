#STRING
str1= "This is a strings.\nwe are creating it in python."   #\n is a sequence character. which is used for next line. 
print(str1)

str1= "This is a strings.\twe are creating it in python."   #\t is same. for using Tab.
print(str1)

#BASIC OPERATION
#Concatenation
str1= "Farhan"
str2= "Ahmad"
final_str=str1+str2
print(final_str)

#Length of str
str1="Farhan"                                               # using len(str) to find length of string. it includes character,digits,spaces,special character like $ % # @ etc.
print(len(str1))

str2="Ahmad"
len1=len(str2)
print(len1)

#INDEXING
str= "Farhan Ahmad"                                         #Farhan FA  
ch=str[0]                                                   #012345678
print(ch)                                                   #indexing is a assining a no of your character including spaces or special character
                                                            # str[x] , using this we can write specific character of assigned no, and here x is a assigned no
ch=str[1]                                                   # And assigned no of a string is always starts with Zero.
print(ch)

print(str[6])

#SLICING
str= "Farhan Ahmad"                                         # str[a:b] , Using this write particilar character of a word, from character a to character b. are called slicing.
print(str[1:6])                                             # where a and b are index assigning no.
print(str[0:7])                                             # when we write a part of word from a word, str[a:b], here resultant word is always including a letter and excluding b letter.
print(str[7:11])
print(str[:7]) #[0:7]

print(str[7:12])
print(str[7:len(str)])
print(str[7:]) #[7:len(str)]

# negativ index slicing
str="apple"                                                 #  a  p  p  l  e
print(str[-3:-1])                                           # -5 -4 -3 -2 -1
print(str[-5:-2])                                           #str[a:b], here last letter got (-1) and first letter got (-5), and same as slicing it include firsh letter of firt digit (a) and exclude last letter of last digit (b)
print(str[-3:-1])



#STRING FUNCTIONS
 #str.endswith("er")
str="I am studying python from ApnaCollege"                # str.endswith("xyZ") using this we can check xyZ is a last letters of a string yess or no.
print(str.endswith("app"))                                 # return true if string ends with substr
print(str.endswith("ege"))

 #str.capitalie()
str="i am studying python from ApnaCollege"
print(str.capitalize())                                    # str.capitalize(), using this we can only capitalize first letter of a sentence, rest smaller 
print(str)                                                 # or it cannot change the orignal.

str="i am studying python from ApnaCollege"                # but if we want to change the original one so the can do this
str=(str.capitalize())
print(str)  

 #str.replace(old,new)
str="i am studying python from ApnaCollege"                # str.replace(old,new), using this we can replace , word or letter.
print(str.replace("o","a"))
print(str.replace("python","javascript"))
                                                    # self made
                                                    #str="i am studying python from ApnaCollege"
                                                    #a=input("a=")
                                                    #b=input("b=")
                                                    #print(str.replace(a,b))
 
 #str.find(word)
str="i am studying python from ApnaCollege"
print(str.find("o"))                                        # str.find(word), using this we can find a word or character from a string, like "o","am"
print(str.find("am"))                                       # and result shows index no of a character or word , like "o" shows 18, and "am" shows 2.
print(str.find("Q"))                                        # and which letter, or character does not exist in a string , the result shows -1.

 #str.count("am")
str="i am studying python from ApnaCollege"                 # str.count("am"), using this we count the no of word or character are repeated in a string.
print(str.count("o"))
print(str.count("from"))



#practice Questions
# 1.WAP to input user's first name & print its length.
#a=input("Enter Your First Name:")
#print("Length of your name is:",len(a))

# 2.WAP to find the occurrence of '$' in a string.
#str= "Hi am am $ $a $ symbol$ $99.99"
#print(str.count("$"))



#CONDITIONAL STATEMENTS
age=21                              # if(contition):, elif(condition):, else: are conditional statements. using this we can check a condition is true or false.
if(age>=18):
    print("can vote & drive")       # we can write multiple times elif, or if statement, but always starts with if statement

light= "green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("wait")

print("end of code")

num=5                               # also we can write multiple times if statements, and every times it checks the condition is true or false, and if it is true then it executes the code.
if(num>2):                          
    print("grater than 2")          
if(num>3):
    print("grater than 3")

num=5
if(num>2):
    print("grater than 2")          # but elif statement checks when if statement is false, then it checks the condition of elif statement, and if it is true then it executes the code.
elif(num>3):
    print("grater than 3")

light= "pink"                       
if(light=="red"):                   
    print("Stop")                     
elif(light=="green"):               
    print("Go")
elif(light=="yellow"):
    print("Wait")
else:                               # else statement, we can writw it at the end , and only one time, and it executes the code when all the if and elif statements are false.
    print("Light is broken")

age=12
if(age>=18):
    print ("Can Vote")
else:
    print("Can not Vote")

print("end of code")

 #Grade student based on marks
marks =int(input("Enter student marks:"))

if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"

print("Grade of student is:",grade)

 # same in my way
#marks=int(input("Enter your marks:"))
#if(marks>=90):
#    print("Grade A")
#if(90>marks>=80):
#    print("Grade B")
#if(80>marks>=70):
#    print("Grade C")
#if(70>marks):
#   print("Grade D")




