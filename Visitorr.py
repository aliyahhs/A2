import enum


class Category(enum.Enum):          # Create ENUM for the category type of the Visitor
   Tour = 1
   Exhibition = 2
   Special_Events = 3


import enum


class Gender(enum.Enum):        #Create ENUM for gender (Female or Male)
   Female = 1
   Male = 2




class Visitor:          #Class #5
   '''Class to represent a Visitor'''
   def __init__(self, name, age, gender, email, category):
       '''Initialize the attributes of the class'''
       self.__name = name
       self.__age = age
       self.__gender = gender
       self.__email = email
       self.__category = category


   #Add setter and getter method
   def setName(self, name = " "):
       self.__name = name


   def getName(self):
       return self.__name


   def setAge(self, age = " "):
       self.__age = age


   def getAge(self):
       return self.__age


   def setGender(self, gender=None):
       self.__gender = gender


   def getGender(self):
       return self.__gender


   def setEmail(self, email=" "):
       self.__email = email


   def getEmail(self):
       return self.__email


   def setCategory(self, category=None):
       self.__category = category


   def getCategory(self):
       return self.__category


   def __str__(self):
       return f"Visitor: {self.getName()}, Age: {self.getAge()}, Gender: {self.getGender().name}, Email: {self.getEmail()}, Category: {self.getCategory().name}"
