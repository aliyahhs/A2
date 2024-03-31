import enum


class Gender(enum.Enum):        #Create ENUM for gender (Female or Male)
   Female = 1
   Male = 2


class Artist:               #Class #1
   '''Class to represent an Artist'''
   def __init__(self, name, gender, nationality, dateOfBirth, dateOfDeath):
       '''Initialize the attributes of the class'''
       self.name = name
       self.gender = gender
       self.nationality = nationality
       self.dateOfBirth = dateOfBirth
       self.dateOfDeath = dateOfDeath


   #Add setter and getter
   def setName(self, name = " "):
       self.name = name


   def getName(self):
       return self.name


   def setGender(self, gender = None):
       self.gender = gender


   def getGender(self):
       return self.gender


   def setNationality(self, nationality = " "):
       self.nationality = nationality


   def getNationality(self):
       return self.nationality


   def setDateOfBirth(self, dateOfBirth = " "):
       self.dateOfBirth = dateOfBirth


   def getDateOfBirth(self):
       return self.dateOfBirth


   def setDateOfDeath(self, dateOfDeath = " "):
       self.dateOfDeath = dateOfDeath

   def getDateOfDeath(self):
       return self.dateOfDeath


   def __str__(self):
       #Applying str method to display the all attributes of an artist
       return f"Artist: {self.name}, Gender: {self.gender.name}, Nationality: {self.nationality}, Date of Birth: {self.dateOfBirth}, Date of Death: {self.dateOfDeath}"