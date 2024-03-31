from Artist import Artist, Gender
from Artwork import Artwork
from Exhibition import Exhibition, Location
from ExhibitionEvents import ExhibitionEvent, Visitors
from Visitorr import Visitor, Category
from Ticket import Ticket



artist1 = Artist("Leonardo da Vinci", Gender.Male, "Italian", "1452", "1519")
print(artist1)


artwork1 = Artwork(artist1, "Mona Lisa", "c. 1503–1506", "Famous portrait", "Louvre Exhibition")
print(artwork1)

exhibition1 = Exhibition("Louvre Exhibition", "3 months", Location.Permanent_Gallery)
exhibition1.add_artwork(artwork1)
print(exhibition1)

event1 = ExhibitionEvent("Louvre Special Event", "1 week", Location.Outdoor_Space, " SHeikh Zayed Art", Visitors.VVIP)
event1.add_artwork(artwork1)
print(event1)

visitor1 = Visitor("Aliya", 25, Gender.Female, "Aliya@gmail.com", Category.Exhibition)
print(visitor1)

ticket1 = Ticket("AE9971538", "24/04/01", "Louvre Exhibition")
ticket1.assignVisitor(visitor1)
print(ticket1)