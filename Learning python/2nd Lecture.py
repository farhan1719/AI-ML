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
print(str[-5:-2])                                           str[a:b], here last letter got (-1) and first letter got (-5), and same as slicing it include firsh letter of firt digit (a) and exclude last letter of last digit (b)
print(str[-3:-1])


