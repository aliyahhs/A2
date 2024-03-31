from Visitorr import Visitor


class Ticket:           #Class #6
   '''Class to represent a Ticket'''
   def __init__(self, ticketNum, purchaseDate , exhibitionName):
       '''Initialize the attributes of the class'''
       self.__ticketNum = ticketNum
       self.__purchaseDate = purchaseDate
       self.__exhibitionName = exhibitionName
       self.__visitor = None                     #It will initialize visitor attribute to None, Association relationship with Visitor class


   #Add setter and getter method


   def setTicketNum(self, ticketNum = " "):
       self.__ticketNum = ticketNum


   def getTicketNum(self):
       return self.__ticketNum


   def setPurchaseDate(self, purchaseDate = " "):
       self.__purchaseDate = purchaseDate


   def getPurchaseDate(self):
       return self.__purchaseDate


   def setExhibitionName(self, exhibitionName = " "):
       self.__exhibitionName = exhibitionName


   def getExhibitionName(self):
       return self.__exhibitionName


   def getVisitor(self):
       return self.__visitor


   def assignVisitor(self, visitor):
       '''Method to assign a Visitor to the Ticket'''
       self.visitor = visitor


   def __str__(self):
       visitor_name = self.getVisitor().getName() if self.getVisitor() else "None"
       return f"Ticket Number: {self.getTicketNum()}, Purchase Date: {self.getPurchaseDate()}, Exhibition Name: {self.getExhibitionName()}, Visitor: {visitor_name}"