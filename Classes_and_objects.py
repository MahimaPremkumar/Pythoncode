# class goa:
#     name=" "
#     drink=" "
#     def party(self):
#         print('Lets party')
#     def beach(self):
#         print('Enjoying in beach')
# ramesh=goa()
# suresh=goa()

# ramesh.name="Ramesh"
# suresh.name="Suresh"
 
# ramesh.drink="Yes"
# suresh.drink='No'

# print(ramesh.name)
# print(ramesh.drink)

# print(suresh.name)
# print(suresh.drink)

# ramesh.party()
# suresh.beach()

# class laptop:
#     price=" "
#     processor=" "
#     ram=" "

# hp=laptop()
# Lenovo=laptop()
# Dell=laptop()

# hp.price=25000
# Lenovo.price=23000
# Dell.price= 45000

# hp.processor= 'i3'
# Lenovo.processor= 'i5'
# Dell.processor= "i7"

# hp.ram= '8 GB'
# Lenovo.ram='4 GB'
# Dell.ram='16 GB'

# print('Dell price:',Dell.price)
# print('Dell processor:', Dell.processor)
# print('Dell ram:',Dell.ram)

# class laptop:
#     def __init__(self):
#         self.price=0
#         self.processor=" "
#         self.ram=" "
# hp=laptop()
# hp.price=35000
# hp.processor='i5'
# hp.ram= '8Gb'

# print(hp.price)

# class laptop:
#     def __init__(self):
#         self.name=""
#         self.processor=""
#         self.ram=""
#     def display(self):
#         print("Name:", self.name) 
#         print("Processor:", self.processor)
#         print("Ram:", self.ram)
    
# Dell=laptop()
# Dell.processor="i5"
# Dell.name="Dell"
# Dell.ram="8Gb"
# Dell.display()



# class Laptop:
#     def __init__(self):
#         self.name = ""
#         self.processor = ""
#         self.ram = ""
    
#     def display(self):
#         print("Name:", self.name) 
#         print("Processor:", self.processor)
#         print("Ram:", self.ram)
    
# Dell = Laptop()
# Dell.processor = "i5"
# Dell.name = "Dell"
# Dell.ram = "8Gb"
# Dell.display()

# class student:
#     def __init__(self):
#         self.name=""
#         self.register_no= ''
#     def display(self):
#         print("Name:", self.name)
#         print("Register_no:", self.register_no)
# x=student()
# y=student()

# x.name="Marvin"
# y.name="David"

# x.register_no= 65201
# y.register_no= 34290

# x.display()
# y.display()

# class fruit:
#     def __init__(self,col):
#         self.color= col

# apple=fruit("Red")
# print(apple.color)

# class teacher:
#     def __init__(self,name,regno):
#         self.name= name
#         self.regno= regno
#     def display(self):
#         print("Name:",self.name)
#         print("Regno:", self.regno)
# t1=teacher("Ram", "023")
# t2=teacher("Devi", "345")

# t1.display()
# t2.display()

# class calculator:
#     def __init__(self,a,b):
#         self.a= a
#         self.b= b
#     def add(self):
#         print(self.a+self.b)
# a=int(input())
# b=int(input())
# calculation=calculator(a,b)
# calculation.add()

  
# class same:
#     def __init__(self):
#         self.name= ""
#         self.type= ""
#     def setname(cls):
#         cls.name="Mahima"
#         print(cls.name)
# sep=same()
# same.setname(same)
# sep.name= "Mahima"
# sep.type= "Mytype"
# print(sep.name)
# print(sep.type)

# class dad:
#     def phone(self):
#         print("Dad's Phone")
# class son:
#     def laptop(dad):
#         print("Son's laptop")
# class grandson:
#     def pc(son):
#         print("My pc")

# prem=dad()
# prem.laptop()
 
# suba=son()
# suba.pc()

# class python:
#     def __init__(self):
#         self.customername= "John"

# c1=python()
# c1.customername()


# class tablet():
#     def __init__(self):
#         self.name= "Mahima"
#         self.age= 23
#     def flames(self):
#         print(self.name)
#         print(self.age)
# class phone(tablet):
#     def tab (self):
#         self.name= "John"
#         self.age= 45

# x=tablet()
# y=phone()
# print(y.tab)


# class vehicle:
#     no_of_wheels=2
#     def carwash(self):
#         print("Once in a week")
# class bike(vehicle):
#     no_of_airbages= 4

# class scooter(bike):
#     ev= "yes"

# x=scooter()
# print(x.no_of_airbages)
# print(x.no_of_wheels)
# print(x.ev)
# x.carwash()


# class grandfather:
#     def phone(self,name):
#         self.name= name

# class father:
#     def laptop(self,name2):
#         self.name2= name2
# class son:
#     def tablet(self):
#         print("Son's tablet")


# x=grandfather()
# y=father()
# z=son()

# x.name= "Shri"
# y.name2="Anand"

# print(x.phone("name"))
# print(y.laptop("name"))
# z.tablet()

# class father:
#     hair_color= "White"
#     def music(self):
#         print("Kuthu paatu!")
# class mother:
#     hair_color= "Black"
#     eye_color= "Blue"
#     def music(self):
#         print('Melody paatu!')

# class child(mother,father):
#     no_of_legs=2

# child=child()
# child.music()
# print(child.hair_color)
# print(child.eye_color)



