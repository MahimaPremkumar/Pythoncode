#Addition of 2 numbers:

# print(3+5)

# a=int(input("Enter no 1:"))
# b=int(input("Enter no 2:"))
# print(a+b)

# a=float(input("Enter no 1:"))
# b=float(input("Enter no 2:"))
# print(a+b)

# a=int(input("Enter num 1:"))
# b=int(input("Enter num 2:"))
# c=a+b
# print(f"The sum of {a} and {b} is {c}")

# a=int(input("Enter no:"))
# b=int(input("Enter no:"))
# c=a+b
# print(f"The sum of {a} and {b} is {c:.2f}")

# def add():
#     a= int(input("Enter a value:"))
#     b= int(input("Enter a value:"))
#     print (a+b)
#     return a+b
# add()

# def add(num1,num2):
#     return num1+num2
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# result=add(num1,num2)
# print(f"The sum of {num1} and {num2} is {result}")
    
#Print numbers 1 to 100

# for i in range(1,101):
#     print(i)

# n= int(input("Enter a value:"))
# for i in range(1,n):
#     print(i,end=" ")

# n=int(input("Enter a value:"))
# while n<=100:
#         n+=1
#         print(n,end=" ")

# print([i for i in range(1,100)])

# print(*(i for i in range(1, 100)))

# i=1
# n=int(input("Enter num:"))
# while i<=n:
#     print (n)
#     n+=1

# n=int(input("Enter a num:"))
# print([i for i in range(1,n+1)])
  
# a=[]
# for i in range(1,101):
#     a.append(i)
#     i+=1
# print(a)

#Sum of natural numbers

# n=int(input('Enter a number:'))
# total=0
# for i in range(n):
#     total+=i
# print(total)

# n=int(input("Enter a num:"))
# i=0
# total=0
# while  i<=n:
#     total=total+i
#     i+=1
# print(total)

# def add(n,sum):
#     for i in range(1,n):
#         sum+=i
#     return sum
# sum=0
# n=int(input("Enter num:"))
# print(f'The sum of natural numbers from 1 to {n} is {add(n,sum)}')

# def natural_numbers():
#     total=0
#     n=int(input("Enter a num:"))
#     for i in range(1,n+1):
#         total+=i
#     return total
# natural_numbers()

#Even number

# n=int(input("Enter a num:"))
# even=[]
# odd=[]
# for i in range(1,n):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even:",even)
# print("Odd:",odd)

# n=int(input("Enter a num:"))
# i=1
# even=[]
# odd=[]
# while i<=n:
#     if i%2==0:
#         even.append(i)
#         i+=1
#     elif i%2!=0:
#         odd.append(i)
#         i+=1
#     else: 
#         break
# print("Even:",even) 
# print("Odd:"odd)

#Sum of even numbers
# n=int(input("Enter num:"))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# n=int(input("Enter num:"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum+=i
#     i+=1
# print("Sum of even num:",sum)

# def sum(n):
  
#     sum=0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum+=i
#             i+=1
#         return sum

# n=int(input("Enter a num:"))
# print("Sum of even num:",sum)

# def sum_of_evenno(n):
#     sum=0
#     for i in range(1,n):
#         if i%2==0:
#             sum+=i
#     return sum
# num=int(input())
# print('Sum of even num is',sum_of_evenno(num))

# list1=[]
# for i in range(1,101):
#     if i%2==0:
#         list1.append(i)
# print (list1)

# list1=[]
# i = 1
# while i<=100:
#     if i%2==0:
#         list1.append(i)
#     i+=1
# print(list1)
  
# def sum_of_evennum():
#     total=0
#     for i in range(1,101):
#         if i%2==0:
#             total += i
#     return total
# sum_of_evennum()

#Odd number

# sum=0
# for i in range(1,50):
#     if i%2!=0:
#         sum+=i
# print(sum)    

# i=1
# sum=0
# while i<=10:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(sum)

# def sum(total):
#     for i in range(1,n):
#         if i%2!=0:
#             total+=i
#     return total
# total=0
# n=int(input())
# print(f"The sum of odd number for 1 to 10 {sum(total)}")

# num1=int(input("Enter num:"))
# num2=int(input("Enter num:"))
# for i in range(num1,num2):
#     if i%2!=0:
#         print(i)

#Remove Punctuation from string

# str= "Hi! I am Zoya, from California."
# a=str.replace("!","")
# print(a)

# str= "Hi! I am Zoya, from California."
# punctuation="!@#$%^&*(){}[\]?/,|-_:;.<>="
# new_str=" "
# for i in str:
#     if i not in punctuation:
#         new_str+=i
# print(new_str)

# import string

# # define a function
# def remove_punctuation(text):
#     return ''.join(char for char in text if char not in string.punctuation)

# # user input
# sentence = input("Please enter your sentence: ")

# # call a function
# print(remove_punctuation(sentence))
    
#Calculator

# num1=int(input())
# num2=int(input())
# operation=input("add/sub/mul/div:")

# if operation=="add":
#     print(num1+num2)
# elif operation=="sub":
#     print(num1-num2)
# elif operation=="mul":
#     print(num1*num2)
# elif operation=="div":
#     print(num1/num2)
# else:
#     print("Invalid input")

# def add(n1,n2):
#     return n1+n2
# def sub():
#     return n1-n2
# def mul():
#     return n1*n2
# def div():
#     if n2!=0:
#         return n1/n2
#     else:
#         print("Division by zero are not allowed")
# while True:
#     n1=int(input())
#     n2=int(input())
#     operation=input("add/sub/mul/div:")
#     if operation=="add":
#         a=add(n1,n2)
#         print(a)
#     elif operation=="sub":
#         s=sub()
#         print(s)
#     elif operation=="mul":
#         m=mul()
#         print(m)
#     elif operation=="div":
#         d=div()
#         print(d)
#     else:
#         print("Your input is invalid")
#         break

# def add(n1,n2): #Multiple Operations with same input
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2
# n1=int(input("Enter num1:"))
# n2=int(input("Enter num2:"))
# result=add(n1,n2)
# print("Add ans:", result)
# result1=sub(n1,n2)
# print("Sub ans:", result1)
# result2=mul(n1,n2)
# print("Mul ans:", result2)
# result3=div(n1,n2)
# print("Div ans:", result3)

# class calculator:
#     def __init__(self):
#         self.n1=int(input("Enter a value:"))
#         self.n2=int(input("Enter a value:"))
#         self.options=input("add/sub/mul/div:")
#     def add(self):
#         return self.n1+ self.n2
#     def sub(self):
#         return self.n1- self.n2
#     def mul(self):
#         return self.n1*self.n2
#     def div(self):
#         return self.n1/self.n2
# cals=calculator()
# sum=cals.add()
# print("Added value:", sum)
# minus=cals.sub()
# print("Subrated value:",minus)
# into=cals.mul()
# print("Multiplied value:", into)
# divide=cals.div()
# print("Divied value:",divide)

# class calculator:
#     def __init__(self,n1,n2,option):
#         self.n1= n1
#         self.n2= n2
#         self.options= option
#     def add(self):
#         return n1+n2
#     def sub(self):
#         return n1-n2
#     def mul(self):
#         return n1*n2
#     def div(self):
#         return n1/n2
# while True:
#     n1=int(input("Enter n1:"))
#     n2=int(input("Enter n2:"))
#     option= input('add/sub/mul/div')
#     cals=calculator(n1,n2,option)
#     if option=="add":
#         sum=cals.add()
#         print(sum)
#     elif option=="sub":
#         minus=cals.sub()
#         print(minus)
#     elif option=="mul":
#         multiply=cals.mul()
#         print(multiply)
#     elif option=="div":
#         divide=cals.div()
#         print(divide)
#     else:
#         print("Invalid entry")
#         break

# class calculator:
#     def __init__(self):
#         self.n1=int(input())
#         self.n2= int(input())
#         self.options=input("add/sub/mul/div:")
#     def add(self):
#         return self.n1+self.n2
#     def sub(self):
#         return self.n1-self.n2
#     def mul(self):
#         return self.n1*self.n2
#     def div(self):
#         return self.n1/self.n2
# while True:
#     cals=calculator()
#     if cals.options=="add":
#         sum=cals.add()
#         print(sum)
#     elif cals.options=="sub":
#         minus=cals.sub()
#         print(minus)
#     elif cals.options=="mul":
#         multiply=cals.mul()
#         print(multiply)
#     elif cals.options=="div":
#         divide=cals.div()
#         print(divide)
#     else:
#         print("Invalid entry")
#         break

# operation=input("Enter the calculations:")
# result=eval(operation)
# print("Result:",result)

# def calculator(exp):
#     result= eval(exp)
#     return result 
# exp=input("Enter a mathematical operation:")
# cals=calculator(exp)
# print("Answer:",cals)

#Multiplication Tables 

# t=int(input("Enter value:"))
# for j in range(1,11):
#     print(j,"*",t,"=",end="")
#     print(j*t)
    
# t=int(input("Enter value:"))
# for i in range(1,11):
#     print(i,"*",t,"=",i*t)

# t=int(input("Enter tables to be multiplied:"))
# i=int(input("Enter num:"))
# while i<=10:
#     print(i,"*",t,"=",i*t)
#     i+=1

# def tables():
#     t=int(input("Enter value:"))
#     print("Multiplication tables of",t)
#     for i in range(1,11):
#         print(i,"*",t,"=",i*t)
# tables()

#Check whether a list is empty or not

# my_list=[]
# if my_list:
#     print("List is not empty")
# else:
#     print("List is empty")

# my_list=[1,2,3,4,5]
# if not my_list:
#     print("List is empty ")
# else:
#     print("not empty")

# list=[1,2,3,4,5]
# if list==[]:
#     print("List is empty")
# else:
#     print("List is not empty")

# i=[]
# if len(i)==0:
#     print("List is empty")
# else:
#     print("Non-Empty list")
    
#decorators

# def mydec(str):
#     def func():
#         print("Before printing")
#     str()
#     print("After printing")
#     return func
# @mydec
# def greetings():
#     print("Hello World")
# greetings()

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# @smart_div
# def div(a,b):
#     print(a/b)
# division=smart_div(div)
# div(2,4)

#Sorting words
  
# my_list=["Hi","my",'name',"Is","Mahima"]
# my=" ".join(my_list)
# my1=my.lower()
# my2=my1.split()
# my2.sort()
# print(my2)

# words=["watermelon","apple","Pineapple","cherry","Berry"]
# joined_words=" ".join(words)
# joined_words1=joined_words.lower()
# joined_words2=joined_words1.split()
# joined_words2.sort()
# print(joined_words2)

# sentence="I am Mahima and I am 23 years old"
# sentence1=sentence.lower()
# sentence2=sentence1.split()
# sentence2.sort()
# sentence3=" ".join(sentence2)
# print(sentence3)

# def sorting():
#     words=input("Enter your sentence:")
#     a=words.lower()
#     b=a.split()
#     b.sort()
#     c=" ".join(b)
#     print(c)
# sorting()

# calender

# import calendar 
# year=int(input("Enter a year:"))
# print(calendar.calendar(year))

# import calendar
# year=int(input("Enter year:"))
# month=int(input("Enter month:"))
# print(calendar.month(year, month))

# import datetime
# now=datetime.datetime.now()
# print("Current date and time:",now)

# import datetime
# today=datetime.date.today()
# print(today)

#Removing duplicates

# my_list=[1,2,3,4,5,2,6,7,8,3]
# set=set(my_list)
# list=list(set)
# print(list)

# my_list=[1,2,3,4,5,6,1,2,2,3,4,8,9]
# store_data=set()
# for i in my_list:
#     if my_list.count(i)>1:
#         store_data.add(i)
# list_data=list(store_data)
# print(list_data)

# list1=[23,12,34,45,23,45,67,87,21]
#list1.sort()                  # ascending order
# list1.sort(reverse=True)     # desending order
# print(list1)

#bubble sort

# list1=[23,12,34,45,23,45,67,87,21]
# n=len(list1)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if list1[j]> list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print("Sorted list:")
# for i in range(len(list1)):
#     print(list1[i])
  
# def bubblesort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

# arr=[1,2,3,7,5,4,3]
# bubblesort(arr)
# for i in range(len(arr)):
#     print(arr[i])

#selection sort

# list=[12,11,10,14,15]
# size=len(list)
# for s in range(size):
#     min_idx= s
#     for j in range(s+1,size):
#         if list[j]< list[min_idx]:
#             list[j],list[min_idx]=list[min_idx],list[j]
# print(list)

# def selectionsort(n,arr):
#     for s in range(n):
#         min_idx= s
#         for j in range(s+1, n):
#             if arr[j]< arr[min_idx]:
#                 arr[j],arr[min_idx]=arr[min_idx],arr[j]
# arr=[12,11,13,14,15,10]
# n=len(arr)
# selectionsort(n,arr) 
# print("Sorted list:",arr)

# list=[12,11,23,43,21]
# tem=0
# l=len(list)
# for i in range(l):
#     for j in range(0,l):
#         if list[i]<list[j]:
#             tem=list[i]
#             list[i]=list[j]
#             list[j]=tem
# print(list)

# sortingwithoutsort()

# n=int(input("Enter len:"))
# my_list=[]
# for k in range(n):
#     arr=int(input(f"Enter {k+1} num:"))
#     my_list.append(arr)
# print("List before sorting:",my_list)

# num=0
# for i in range(0,len(my_list)):
#     for j in range(i+1,len(my_list)):
#         if my_list[i]>my_list[j]:#ascending order
#             my_list[i]<my_list[j]#decending order
#             num=my_list[i]
#             my_list[i]=my_list[j]
#             my_list[j]=num
# print('list after sorting:',my_list)

#Pattern hollow sq

# size = int(input('Enter Size of the hollow Square: '))
# i = 0
# while i<size:
#     j = 0
#     while j<size:
#       if i == 0 or i == size-1 or j == 0 or j == size-1:
#         print("*", end=" ")
#       else:
#         print(" ", end=" ")
#       j+=1
#     print("\r")
#     i+=1

# size = int(input('Enter Size of the hollow Square: '))
# for i in range(size):
#    for j in range(size):
#       if i == 0 or i == size-1 or j == 0 or j == size-1:
#          print("*", end=" ")
#       else:
#          print(" ", end=" ")
#    print("\r")#carrier return moves cursor to next line

# len=int(input("Enter the length:"))
# for i in range(len):
#    for k in range(len):
#       if i==0 or k==0 or i==len-1 or k==len-1:
#          print('*',end=" ")
#       else:
#          print(" ",end=" ")
#    print( )#empty print func can also move cursor to next line

#Password verification:

# Password=input("Enter password:")
# Password_len=len(Password)
# upper_case,lower_case,numbers,spl_char,no_space=False,False,False,False,False
# if Password_len>=8 and Password_len<20:
#     for i in Password:
#         if i.isupper():
#             upper_case=True
#         if i.islower():
#             lower_case=True
#         if i.isdigit():
#             numbers=True
#         special=["@","#","*","$","&"]
#         if i in special:
#             spl_char=True
#         if i !=" ":
#             no_space=True
# else:
#     print("Password should contain 8 to 20 characters")
# print({"uppercase":upper_case,
#        "lowercase":lower_case,
#        "integers":numbers,
#        "special_char":spl_char,
#        "no_space":no_space
#        })

#Prime numbers
                    
# a=int(input("Enter num:"))
# if a > 1:
#     for x in range(2,a):
#         if(a%x)==0:
#             print("Composite number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Your num is less than 1")

#Left angle triangle:

# len=int(input("Enter the length:"))
# for i in range(len):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n=int(input("Enter num:"))
# for i in range(n):
#     print('* '*i,end="")
#     print()

#Right angle triangle:

# n=int(input("Enter len:"))
# for i in range(n):
#     print(" "*(n-i),"*"*i,end=" ")
#     print()

# len=int(input("Enter len:"))
# for i in range(len):
#     for j in range(2*(len-i)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end= " ")
#     print()

#Pyramid triangle:

# len=int(input("Enter len:"))
# for i in range(1,len):
#     print(" "*(len-i-1),"* "*i)

#Username and password
# username='user123'
# password='pass@123'
# user_name=input("Enter username:")
# pass_word=input("Enter password:")
# if user_name==username and pass_word==password:
#     print("Login successful!")
# else:
#     print("Invalid login")

#Positive or negative number
# num=int(input("Enter a num:")) #1 
# if num > 0:
#   print("Positive number")
# elif num<0:
#   print("Negative number")
# else:
#   print("The given number is 0")

#Simple calculator
# num1=int(input("Enter num1:")) #2
# num2=int(input("Enter num2:"))
# options=input("add/sub/mul/div:")
# if options=="add":
#   print("Add value:",num1+num2)
# elif options=="sub":
#   print("Sub value:",num1-num2)
# elif options=="mul":
#   print("Multiplied value:",num1*num2)
# elif options=="div":
#   if num1 == 0:
#     print("0 is not divisible")
#   else:
#     print("Divided value:",num1/num2)
# else:
#   print("Invalid entry")

#Grade
# score=int(input("Enter score:")) #3
# if score>=90 and score<=100:
#   print(f"The given score {score} has grade A+")
# elif score>=70 and score<90:
#   print(f"The given score {score} has grade A")
# elif score>=50 and score<70:
#   print(f"The given score {score} has grade B")
# elif score>=35 and score<50:
#   print(f"The given score {score} has grade C")
# elif score<35:
#   print(f"The given score {score} has grade F")
# else:
#   print("Incorrect entry")

#Leap year or not
# year=int(input("Enter year:"))   #4
# if (year%4==0 and year%100!=0) or (year%400==0):
#   print(f"{year} it's a leap year")
# else:
#   print(f"{year} it's not a leap year")

#BMI
# Weight=int(input("Enter your weight in kgs:"))   #5
# Height=float(input("Enter your height in m:"))
# BMI=Weight/(Height**2)
# if BMI<18.5:
#   print(f"Your BMI {BMI:.2f}: You are underweight")
# elif BMI>=18.5 and BMI<=25:
#   print(f"Your BMI {BMI:.2f}: You have a healthy weight")
# elif BMI>25 and BMI<=30:
#   print(f"Your BMI {BMI:.2f}: You are Overweight")
# else:
#   print(f"Your BMI {BMI:.2f}:You are Obese")

#Equilateral or isoscales or scalene
# Len1=float(input("Enter the len1 of the triangle:"))  #6
# Len2=float(input("Enter the len2 of the triangle:"))
# Len3=float(input("Enter the len3 of the triangle:"))
# if Len1==Len2==Len3:
#     print("Equilateral triangle")
# elif Len1==Len2 or Len2==Len3 or Len1==Len3:
#     print("Isoscales triangle")
# elif Len1!=Len2!=Len3:
#     print("Scalene triangle")
# else:
#     print("Triangle type not mentioned")

#Largest of 3 numbers
# num1=int(input("Enter num1:"))  #7
# num2=int(input("Enter num2:"))
# num3=int(input("Enter num3:"))
# if num1>num2 and num1>num3:
#     print(f"The largest number is {num1}")
# elif num2>num1 and num2>num3:
#     print(f"The largest number is {num2}")
# else:
#     print(f"The largest number is {num3}")

# username=input("Enter your username:")  #8
# password=input("Enter your password:")
# # len_username=len(username)
# len_password=len(password)
# upper_case,lower_case,numbers,spl_char,space=False,False,False,False,False
# if len_password>=8 and len_password<=20:
#     for i in username:
#         for i in password:
#             if i.isupper():
#                  upper_case=True
#             if i.islower():
#                 lower_case=True
#             if i.isdigit():
#                 numbers=True
#             spl_char=['!','@','#','$','%','^','&','*']
#             if i in spl:
#                 spl=True
#             if i != " ":
#               space=True
# else:
#     print("Password character should be more than 8 and less than 20 char")
# print ({
#     "uppercase":upper_case,
#     'lowercase':lower_case,
#     "numbers":numbers,
#     "splchar":spl_char,
#     "space":space
#     })

# print("=====SHIPPING CALCULATOR=====")   #9
# cost=float(input("Enter the cost of the items purchased in rupees:"))
# if cost>2.00 and cost<=30.00:
#     print(f"Shipping cost: 5.95 rupees")
#     print(f"Cost of items purchsed:{cost}")
#     print(f"The total price for ur order is {cost+5.95:.2f}")
        
# elif cost>30.00 and cost<=50.00:
#     print(f"Shipping cost: 7.95 rupees")
#     print(f"Cost of items purchsed:{cost}")
#     print(f"The total price for ur order is {cost+7.95:.2f}")
        
# elif cost>50.00 and cost<=75.00:
#     print(f"Shipping cost: 9.95 rupees")
#     print(f"Cost of items purchsed:{cost}")
#     print(f"The total price for ur order is {cost+9.95:.2f}")
    
# elif cost>75.00:
#     print(f"Shipping cost:FREE")
    
# else:
#     print("Cost should be greater than 2.00")
# print("Thanks for shopping:)")

# def __init__():
#     weight=float(input("Enter the weight of the purchase in kg:"))
#     destination=float(input("Enter approximate distance in km:"))
#     cost=float(input("Total cost of the purchase:"))

# def weight(self,weight,cost):
#     if weight<=2:
#         print("The shipping cost:50.00")
#         return cost+50.00
#     elif weight>2 and weight<=10:
#         print("The shipping cost:75.00") 
#         return cost+75.00
#     elif weight<10:
#         return "free"
#     else:
#         print("ERROR:Weight is below 1 kg")

# def destination(self,weight,destination,cost):
#     if destination>50:
#         print("The shipping cost:100.00")
#         return cost+100.00
#     elif destination>20 and destination<=50:
#         print("The shipping cost:50.00")
#         return cost+50.00
#     elif destination>=5 and destination<=20:
#         print("The shipping cost:25.00")
#         return cost+25.00
#     else:
#         print("Destination below 5km has no shipping cost")

# weight(weight)
# destination(destination)

# print("=====Tax Calculator=====") #10
# annual_income=int(input("Enter your annual income:"))
# if annual_income>=300000 and annual_income<=700000:
#     print("You come under 5% tax slab")
#     income_tax=annual_income * 5/100
#     print("The tax amount to be paid:", income_tax)

# elif annual_income>700000 and annual_income<= 1000000:
#     print("You come under 10% tax slab")
#     income_tax= annual_income * 10/100
#     print("The tax amount to be paid:",income_tax)

# elif annual_income>1000000 and annual_income<=1200000:
#     print("You come under 15% tax slab")
#     income_tax=annual_income * 15/100
#     print("The tax amount to be paid:",income_tax)

# elif annual_income>1200000 and annual_income<=1500000:
#     print("You come under 20% tax slab")
#     income_tax= annual_income* 20/100
#     print("The tax amount to be paid:",income_tax)

# elif annual_income>1500000:
#     print("You come under 30% tax slab")
#     income_tax=annual_income * 30/100
#     print("The tax amount to be paid:",income_tax)

# else:
#     print("You are deducted from paying tax")    

#Shipping cost
# weight=float(input("Enter weight of your purchase in kg: ")) #9
# destination=float(input("Enter destination in km:"))
# cost=float(input("Enter the cost of ur purchase:"))
# sample_cost = 2
# cost_per_kg= 2
# cost_per_km= 5
# formula=sample_cost+(cost_per_kg*weight)+(cost_per_km*destination)
# if weight <2 and destination >5:
#     print("You have no charges for shipping")
# else:
#     print("The shipping cost for ur purchase:",formula)
#     print("The total cost of ur order is",cost+formula)

# Prime or composite number
# a=int(input("Enter num:")) #11
# if a > 1:
#     for x in range(2,a):
#         if(a%x)==0:
#             print("Composite number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Your num is less than 1")

#Traffic light
# import time 
# traffic_lights=input("red/yellow/green:") #12
# if traffic_lights=="red":
#     print("STOP!It's red signal")
#     time.sleep(60)
# elif traffic_lights=="yellow":
#     print("Please wait!")
#     time.sleep(30)
# elif traffic_lights=="green":
#     print("GO!It's green signal")
#     time.sleep(60)
# else:
#     print("Please enter valid traffic light")

#C to F
# temp=float(input("Enter degree:"))#13
# formula_CF=5/9*(temp-32)
# if True:
#     print(f"The fahrenheit degree is:{formula_CF:.2f}")

# temp=float(input("Enter degree:"))
# formula_FC=(temp*(9/5))+32
# if True:
#     print(f"The celsius degree is:{formula_FC:.2f}")

#Quiz game
# print("Q1:Which planet in the Milky Way is the hottest?")
# options=input("A:Mercury\nB:Venus\nC:Earth\nD:Jupiter")
# Ans=input("Answer:").upper()
# if Ans=="A":
#     print("Wrong Answer")
# elif Ans=="B":
#     print("Correct Answer")
# elif Ans=="C":
#     print("Wrong Answer")
# elif Ans=="D":
#     print("Wrong Answer")
# score=0
# if Ans=="B":
#     score+=1
#     print(f"Score:{score}")
# else:
#     print(f"Score:{score}")

# print("Q2:Who was the first woman to win a Nobel Prize?")
# options=input("A:Marie Curie\nB:Sunita Williams\nC:Mother Teresa\nD:Aiswarya Rai")
# Ans=input("Answer:").upper()
# if Ans=="A":
#     print("Correct Answer")
# elif Ans=="B":
#     print("Wrong Answer")
# elif Ans=="C":
#     print("Wrong Answer")
# elif Ans=="D":
#     print("Wrong Answer")

# if Ans=="A":
#     score+=1
#     print(f"Score:{score}")
# else:
#     print(f"Score:{score}")

# print("Q3:What is the highest boiling point of water?")
# options=input("A:101 C\nB:201 C\nC:100 C\nD:102 C")
# Ans=input("Answer:").upper()
# if Ans=="A":
#     print("Wrong Answer")
# elif Ans=="B":
#     print("Wrong Answer")
# elif Ans=="C":
#     print("Correct Answer")
# elif Ans=="D":
#     print("Wrong Answer")

# if Ans=="C":
#     score+=1
#     print(f"Score:{score}")
# else:
#     print(f"Score:{score}")



# '''
# another way
# '''

# print("Q1:Which planet in the Milky Way is the hottest?")
# print("A:Mercury\nB:Venus\nC:Earth\nD:Jupiter")
# Ans=input("Answer:").upper()
# score=0
# if Ans=="A":                #print('wrong') if Ans == "A" else print("cort")
#     print("Wrong Answer")
# elif Ans=="B":
#     print("Correct Answer")
#     score+=1
# elif Ans=="C":
#     print("Wrong Answer")
# elif Ans=="D":
#     print("Wrong Answer")
# else:
#     print("some mistake")
# print(score)

# print("Q2:Who was the first woman to win a Nobel Prize?")
# options=input("A:Marie Curie\nB:Sunita Williams\nC:Mother Teresa\nD:Aiswarya Rai\n")
# Ans=input("Answer:").upper()
# if Ans=="A":
#     print("Correct Answer")
#     score+=1
# elif Ans=="B":
#     print("Wrong Answer")
# elif Ans=="C":
#     print("Wrong Answer")
# elif Ans=="D":
#     print("Wrong Answer")
# else:
#     print("some mistake")

# print("total score is ",score)

'''
-------------------------------------------------------------

'''
#datetime
# import datetime
# year=int(input("Enter the year(eg:2023):"))
# month=int(input("Enter the month(eg:1-12):"))
# day=int(input("Enter the day(eg:1-31):"))

# x=datetime.date(year,month,day)
# day_of_week = x.strftime("%A")
# print(f"The day of the week is {day_of_week}")

# today=datetime.date.today()
# print(today)

#Age verification
# age=int(input("Enter your age:")) #16
# if age>=18 and age<60:
#     print("You are eligible for voting")
# elif age>=60:
#     print("You are senior citizen and eligible for voting")
# else:
#     print("You are not eligible")   

# print("Welcome to Vending Machine!")
# items=input("1:Coke cola-30\n2:Pepsi-30\n3:Lays-20\n4:Water Bottle-10\nSelect the item number you wish to purchase:")
# balance=40
# if items=="1":
#     print("You selected Coke cola-Rs.30")
#     charges=int(input("1:Card or 2:Cash:"))
#     if charges=="1":
#         print("Please enter your card")
#         if balance>30:
#             balance-=30
#             print(f"Your current balance is {balance}")
#         else:
#             print("You have insufficent balance")
#     if charges=="2":
#         print("Please insert Rs.30")
  
# elif items=="2":
#     print("You selected Pepsi-Rs.30")
#     charges=input("1:Card or 2:Cash:")
#     if charges=="1":
#         print("Please enter your card")
#         if balance>30:
#             balance-=30
#             print(f"Your current balance is {balance}")
#         else:
#             print("You have insufficent balance")
#     if charges=="2":
#         print("Please insert Rs.30")
 
# elif items=="3":
#     print("You selected Lays-Rs.20")
#     charges=input("1:Card or 2:Cash:")
#     if charges=="1":
#         print("Please enter your card")
#         if balance>20:
#             balance-=20
#             print(f"Your current balance is {balance}")
#         else:
#             print("You have insufficent balance")
#     if charges=="2":
#         print("Please insert Rs.20")
   
# elif items=="4":
#     print("You selected Water Bottle-Rs.10")
#     charges=input("1:Card or 2:Cash:")
#     if charges=="1":
#         print("Please enter your card")
#         if balance>10:
#             balance-=10
#             print(f"Your current balance is {balance}")
#         else:
#             print("You have insufficent balance")
#     if charges=="2":
#         print("Please insert Rs.10")

# else:
#     print("Invalid entry")
# print("Thanks for purchasing!")   

# rock,paper,scissors: 
# Game=str(input("rock or paper or scissors:")).lower()
# if Game=="rock":
#     print("Paper")
# elif Game=="paper":
#     print("Scissors")
# elif Game=="scissors":
#     print("Rock")      
# else:
#     print("Invalid entry")

# import random
# choice=["rock","paper","scissors"]
# user_input=input("rock or paper or scissors:").lower()
# computer_input=random.choice(choice)
# print("You chose:",user_input)
# print("Computer chose:",computer_input)
# if user_input==computer_input:
#     print("Tie")
# elif user_input=="rock" and computer_input=="scissors":
#     print("You win!")
# elif user_input=="paper" and computer_input=="rock":
#     print("You win!")
# elif user_input=="scissors" and computer_input=="paper":
#     print("You win!")
# else:
#     print("Computer wins!")

# import random
# options=["rock","paper","scissors"]
# user_input=input("Enter rock or paper or scissors:")
# computer_input=random.choice(options)
# print("You chose:",user_input)
# print("Computer chose:",computer_input)

# if user_input==computer_input:
#     print("It's a tie")
# elif (user_input=="rock" and computer_input=="scissors") or (user_input=="scissors" and computer_input=="paper") or (user_input=="paper" and computer_input=="rock"):
#     print("You win!")
# else:
#     print("Computer wins!")


# palindrome:
# str=str(input("Enter a string:"))
# a=str[::-1]
# print(a)

# string=str(input("Enter a string:"))
# if string[::1]==string[::-1]:
#     print("The given string is a palindrome")
# else:
#     print("The given string is not a palindrome")


# bank statement
# print("Welcome to HDFC Bank")
# options=input("1:Withdraw/2:deposit/3:balance:")
# balance=3000
# if options=="1":
#     withdraw=float(input("Enter the amount to withdraw:"))
#     if balance>withdraw:
#         balance-=withdraw
#         print(f"The current balance is:{balance}")
#     if balance<withdraw:
#         print("Inadequate balance")
# if options=="2":
#     deposit=float(input("Enter the amount to deposit:"))
#     balance+=deposit
#     print(f"The current balance is:{balance}")
# if options=="3":
#     print(f"The current balance is:{balance}")


# import time

# colors = ["Red", "Yellow", "Green"]
# while True:
#     for color in colors:
#         print(color)
#         if color == "Red":
#             time.sleep(4)
#         elif color == "Yellow":
#             time.sleep(1)
#         else:
# 	        time.sleep(3)

# questions = ["What's 2+2?", "Capital of France?", "Year of Moon landing?"]
# answers = ["4", "Paris", "1969"]
# score = 0

# for q, a in zip(questions, answers):
#     user_answer = input(f"{q} ")
#     if user_answer.lower() == a.lower():
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Wrong. The correct answer is {a}")
# print(f"Your final score is {score}/{len(questions)}")

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)


# num=int(input("Enter the num:"))
# for i in range(1,11):
#     print(f"{i}*{num}= {i*num}")

#Factorial number
# mul=1
# num=int(input("Enter the factorial num:"))
# if num>1:
#     for i in range(1,num+1):
#         mul*=i
#     print(f"The factorial of {num} is {sum}")
# else:
#     print("Negative values are not allowed")

# print("Even numbers:")
# for i in range(1,51):
#     if i%2==0:
#         print(i)

#Reversing string
# str=input("enter the value: ")
# length_ofthe_letter = len(str)
# str1=" "
# for i,j in enumerate(str):
#     index_addr = length_ofthe_letter-i-1
#     print(str[index_addr])

# str=input("Enter a string:")
# str_reversed=" "
# for i in range(len(str)-1,-1,-1):
#     str_reversed+=str[i]
# print( str_reversed)

#Vowels
# count=0
# str=input("Enter the string:").lower()
# vowels=['a','e','i','o','u']
# for i in str:
#     if i in vowels:
#         count+=1
# print("The number of vowels:",count)

#Triangle:
# n=int(input("Enter n:"))
# for i in range(n):
#     print('*' * i)

# n=int(input("n:"))
# for i in range(n):
#     print(" "*(n-i),"*"*i,end=" ")
#     print()

#Prime number
# num=int(input())
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#           print("Composite number")
#           break
#         else:
#           print("Prime number")
#           break
# else:
#     print("Number below 1")

#Add each digit from a number:
# add=0
# num=int(input("Enter a num:"))
# num1=str(num)
# for i,j in enumerate(num1):
#     add+=int(j)
#     print(add)

# n = int(input("Enter n:"))
# total = []
# # m = len(str(n))  # Length of the number when converted to a string

# # # Loop through each digit of the number
# for i in str(n):
#     print(i)
#     total.append(int(i))
#     print(total)

# print(sum(total))

# sum=0
# n=int(input("Enter n:"))
# str_n=str(n)
# for i in str_n:
#     sum+=int(i)
#     print(sum)

#power without ** symbol
# mul=1
# n=int(input("Enter n:"))
# power=int(input("Enter power:"))
# for i in range(1,power+1):
#     mul= mul*n
#     print(mul)

#Largest element in the list
# my_list=[12,13,89,30]
# largest=my_list[0]
# for i in my_list:
#     if i>largest:
#         largest=i
# print(f"The largest number in the list is {largest}")

#Remove all occurrences of a specific element from a list.
# my_list=[12,12,13,14,15,12,17,18]
# num=my_list[0]
# empty=[]
# for i in my_list:
#     if i==num:
#         continue
#     else:
#         empty.append(i) 
# print(empty)

# my_list=[int(x) for x in input("Enter num separated by space:").split()]
# num_to_remove=int(input("Enter the num to remove:"))
# for i in my_list:
#     if i!=num_to_remove:
#         print(i)

# num=[int(i) for i in input("Enter the num to find avg:").split()]
# sum=0
# count=0
# for x in num:
#     sum+=x
#     count+=1
# avg=sum/count
# print(avg)

#Perfect number or not
# number=int(input("Enter the num:"))
# sum=0
# for num in range(1,number):
#     if number%num==0:
#         sum+=num   
# if sum==number:
#     print("Perfect number")
# else:
#     print("Not a perfect number")
            
# from itertools import permutations

# num= [i for i in input("Enter num:").split()]
# for p in permutations(num):
#     pp=' '.join(p)
#     print(pp)

# string=input("Enter a string:")
# for p in permutations(string):
#     pp=''.join(p)
#     print(pp)

# string=[i for i in input("Enter  a str:")]
# for i in permutations(string):
#     print(i)

# from itertools import combinations

# str=input("Enter a str:")
# for s in combinations(str,2):
#     print(s)

# string=input("Enter a str:")
# for i in combinations(string,2):
#     c=" ".join(i)
#     print(c)

# integer=[i for i in input("Enter integer separated by space:").split()]
# for i in combinations(integer,2):
#     c=" ".join(i)
#     print(c)

# Print the Fibonacci sequence up to n terms
# n=int(input("Enter n:"))
# a,b=0,1
# for _ in range(n):
#     print(a)
#     a,b=b,a+b


# list1=[23,12,34,45,23,45,67,87,21]
# n=len(list1)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if list1[j]> list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print("Sorted list:")
# for i in range(len(list1)):
#     print(list1[i])

# for i in range(65,91):
#     print(f"{chr(i)}:{i}")
 
        