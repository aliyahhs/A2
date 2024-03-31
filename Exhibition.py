from Artwork import Artwork


import enum


class Location(enum.Enum):          # Create ENUM for the exhibition Location
   Permanent_Gallery = 1
   Exhibition_Hall = 2
   Outdoor_Space = 3


class Exhibition:               # Class #3
   '''Class to represent an Exhibition'''
   def __init__(self, name, duration, location):
       '''Initialize the attributes of the class'''
       self.name = name
       self.duration = duration
       self.location = location
       self.artworks = []                  # Aggregation relationship with Artwork Class


   #Add setter and getter
   def setName(self, name = " "):
       self.name = name


   def getName(self):
       return self.name


   def setDuration(self, duration = " "):
       self.duration = duration


   def getDuration(self):
       return self.duration


   def setLocation(self, location = None):
       self.location = location


   def getLocation(self):
       return self.location


   def getArtworks(self):
       return self.artworks


   def add_artwork(self, artwork):         #This function will add the artworks in the artowrks class inside list that are dislayed in the exhibition
       self.artworks.append(artwork)


   def __str__(self):
       artworks = ""
       for artwork in self.artworks:
           artworks += str(artwork) + "\n"


       return (
           f"Exhibition Name: {self.name}\n"
           f"Duration of the Exhbiton: {self.duration}\n"
           f"Location of the Exhbiton : {self.location.name}\n"
           f"Artworks in the Exhubition:\n{artworks}")