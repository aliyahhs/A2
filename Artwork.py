from Artist import Artist           #Applying the import function to import the attribute 'artist' from the file&class 'Artist'


class Artwork:  # Class #2
   '''Class to represent an Artwork'''
   def __init__(self, artist, title, creationDate, historicalSign, exhibitionName):
       '''Initialize the attributes of the class'''
       self.artist = artist        #Composition relationship with Artist Class
       self.title = title
       self.creationDate = creationDate
       self.historicalSign = historicalSign


   #Add setter and getter
   def setArtist(self, artist = " "):
       self.artist = artist


   def getArtist(self):
       return self.artist


   def setTitle(self, title = " "):
       self.title = title


   def getTitle(self):
       return self.title


   def setCreationDate(self, creationDate = " "):
       self.creationDate = creationDate


   def getCreationDate(self):
       return self.creationDate


   def setHistoricalSign(self, historicalSign = " "):
       self.historicalSign = historicalSign


   def getHistoricalSign(self):
       return self.historicalSign


   def __str__(self):
       #Applying str method to display the all attributes of an artist
       return (
           f"Artwork Title: {self.title}\n"
           f"Artist Name: {self.artist.name}\n"
           f"Creation Date of the ArtWork: {self.creationDate}\n"
           f"Historical Significance: {self.historicalSign}\n")