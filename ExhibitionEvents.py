from Exhibition import Exhibition


import enum


class Visitors(enum.Enum):          # Create ENUM for the type of Visitors
   VVIP = 1
   VIPP = 2
   Regular = 3


class ExhibitionEvent(Exhibition):    #Class #4
   '''Class to represent the exhibition Event'''
   def __init__(self, name, duration, location, theme, visitors):
       '''Initialize the attributes of the class'''
       super().__init__(name, duration, location)      #This is inheritence relationship by inheriting these attributes from the Parent(Exhibition Class)
       self.theme = theme
       self.visitors = visitors                #an instance of the Visitors enum


    #Add setter and getter
   def setTheme(self, theme = " "):
       self.theme = theme


   def getTheme(self):
       return self.theme


   def setVisitors(self, visitors = None):
       self.visitors = visitors


   def getVisitors(self):
       return self.visitors


   def __str__(self):
       return f" Exhibition Event name:{self.name}, Duration:{self.duration}, Location of the Exhibition Event:{self.location}, Theme of the Event:{self.theme}, Type of Visitors in the event:{self.visitors.name}"