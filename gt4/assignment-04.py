#LIST AND STRING METHODS
#Question 1- Reverse the whole list using list methods.
#Answer
str=[1,2,3,4,5]
str.reverse()
print("The reversed list is " ,str)

#Question 2- Print all the uppercase letters from a string.
#Answer 2
print("Enter a string")
strr=input()
final_str=""
for a in strr:
    if(a.isupper()==True):
        final_str=final_str +a
print("characters in upperCase are: ",final_str)

#Question 3- Split the user input on comma's and store the values in a list as integers
#Answer
str1=input("Enter the numbers seperated with commas")
list1=[]
list1=str1.split(",")
print("List : ",list1)

#Question 4- Check whether a string is palindromic or not.
#Answer
print("Enter a string")
strr=input()
rev="".join(reversed(strr))
print(strr,rev)
if(strr==rev):
    print("String is Palindromic")
else:
    print("String is not Palindromic")
    
#Question 5- Make a deepcopy of a list and write the difference between shallow copy
# and deep copy.
#Answer
# DeepCopy
import copy
list_1=[1,3,[7,9,5],11,15,22,19,10]
list_2=copy.deepcopy(list_1)
print('List_1: ',list_1)
print('List_2(deepcopy of list_1): ',list_2)
list_2[2][1]=13
print('After changing List_2')
print('List_1: ',list_1)
print('List_2(deepcopy of list_1): ',list_2)
print(" ")

# ShallowCopy
import copy
list_1=[1,3,[7,9,5],11,15,22,19,10]
list_2=copy.copy(list_1)
print('List_1: ',list_1)
print('List_2(Shallow copy of list_1): ',list_2)
list_2[2][1]=13
list_2[2][2]=17
print('After changing List_2')
print('List_1: ',list_1)
print('List_2(Shallow copy of list_1): ',list_2)

#DIFFERENCE
'''
#  In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
#  In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.

'''
