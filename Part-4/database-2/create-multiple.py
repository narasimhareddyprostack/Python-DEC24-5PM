from pymongo import MongoClient
#establish connection
client=MongoClient('mongodb://localhost:27017/')
db=client['6PM']
user_col=db['users']

users=[{'uid':1,'uname':'Giorgio','gender':'Male'},
{'uid':2,'uname':'Gabie','gender':'Male'},
{'uid':3,'uname':'Craggie','gender':'Male'},
{'uid':4,'uname':'Florella','gender':'Polygender'},
{'uid':5,'uname':'Vita','gender':'Genderfluid'},
{'uid':6,'uname':'Cindie','gender':'Female'},
{'uid':7,'uname':'Franky','gender':'Male'},
{'uid':8,'uname':'Noak','gender':'Male'},
{'uid':9,'uname':'Biddy','gender':'Female'},
{'uid':10,'uname':'Ciro','gender':'Male'},
{'uid':11,'uname':'Jarrett','gender':'Bigender'},
{'uid':12,'uname':'Zelig','gender':'Male'},
{'uid':13,'uname':'Lefty','gender':'Male'},
{'uid':14,'uname':'Sutherland','gender':'Male'},
{'uid':15,'uname':'Matteo','gender':'Male'},
{'uid':16,'uname':'Virgilio','gender':'Male'},
{'uid':17,'uname':'Lucretia','gender':'Female'},
{'uid':18,'uname':'Melisse','gender':'Female'},
{'uid':19,'uname':'Joanna','gender':'Female'},
{'uid':20,'uname':'Kean','gender':'Male'},
{'uid':21,'uname':'Joelie','gender':'Female'},
{'uid':22,'uname':'Zedekiah','gender':'Male'},
{'uid':23,'uname':'Theodor','gender':'Male'},
{'uid':24,'uname':'Ab','gender':'Male'},
{'uid':25,'uname':'Clyve','gender':'Male'},
{'uid':26,'uname':'Colver','gender':'Male'},
{'uid':27,'uname':'Lazarus','gender':'Male'},
{'uid':28,'uname':'Immanuel','gender':'Male'},
{'uid':29,'uname':'Wynny','gender':'Female'},
{'uid':30,'uname':'Lucila','gender':'Female'},
{'uid':31,'uname':'Law','gender':'Male'},
{'uid':32,'uname':'Abel','gender':'Male'},
{'uid':33,'uname':'Blondie','gender':'Female'},
{'uid':34,'uname':'Riane','gender':'Female'},
{'uid':35,'uname':'Walt','gender':'Male'},
{'uid':36,'uname':'Tyler','gender':'Male'},
{'uid':37,'uname':'Vasili','gender':'Male'},
{'uid':38,'uname':'Jenilee','gender':'Female'},
{'uid':39,'uname':'Clarie','gender':'Female'},
{'uid':40,'uname':'Tam','gender':'Male'},
{'uid':41,'uname':'Harlin','gender':'Male'},
{'uid':42,'uname':'Bethany','gender':'Female'},
{'uid':43,'uname':'Randal','gender':'Male'},
{'uid':44,'uname':'Herby','gender':'Male'},
{'uid':45,'uname':'Rodolphe','gender':'Male'},
{'uid':46,'uname':'Jeremias','gender':'Male'},
{'uid':47,'uname':'Chuck','gender':'Male'},
{'uid':48,'uname':'Quentin','gender':'Male'},
{'uid':49,'uname':'Cassaundra','gender':'Female'},
{'uid':50,'uname':'Banky','gender':'Male'},
{'uid':51,'uname':'Winthrop','gender':'Male'},
{'uid':52,'uname':'Felike','gender':'Polygender'},
{'uid':53,'uname':'Rube','gender':'Male'},
{'uid':54,'uname':'Husain','gender':'Male'},
{'uid':55,'uname':'Suzanna','gender':'Female'},
{'uid':56,'uname':'Rebeca','gender':'Female'},
{'uid':57,'uname':'Neal','gender':'Male'},
{'uid':58,'uname':'Patrizius','gender':'Male'},
{'uid':59,'uname':'Kareem','gender':'Male'},
{'uid':60,'uname':'Abram','gender':'Male'},
{'uid':61,'uname':'Ruby','gender':'Male'},
{'uid':62,'uname':'Becca','gender':'Female'},
{'uid':63,'uname':'Prinz','gender':'Male'},
{'uid':64,'uname':'Pierson','gender':'Male'},
{'uid':65,'uname':'Allyce','gender':'Female'},
{'uid':66,'uname':'Natividad','gender':'Genderqueer'},
{'uid':67,'uname':'Jsandye','gender':'Female'},
{'uid':68,'uname':'Mattie','gender':'Female'},
{'uid':69,'uname':'Catrina','gender':'Female'},
{'uid':70,'uname':'Burt','gender':'Male'},
{'uid':71,'uname':'Henrie','gender':'Female'},
{'uid':72,'uname':'Minnie','gender':'Female'},
{'uid':73,'uname':'Elberta','gender':'Female'},
{'uid':74,'uname':'Lyndell','gender':'Genderqueer'},
{'uid':75,'uname':'Chrisy','gender':'Male'},
{'uid':76,'uname':'Melina','gender':'Female'},
{'uid':77,'uname':'Laurent','gender':'Non-binary'},
{'uid':78,'uname':'Ruthann','gender':'Female'},
{'uid':79,'uname':'Chris','gender':'Male'},
{'uid':80,'uname':'Talbot','gender':'Male'},
{'uid':81,'uname':'Yulma','gender':'Agender'},
{'uid':82,'uname':'Maryjo','gender':'Female'},
{'uid':83,'uname':'Flor','gender':'Female'},
{'uid':84,'uname':'Pip','gender':'Male'},
{'uid':85,'uname':'Gabie','gender':'Female'},
{'uid':86,'uname':'Torin','gender':'Genderfluid'},
{'uid':87,'uname':'Kaile','gender':'Female'},
{'uid':88,'uname':'Jacintha','gender':'Female'},
{'uid':89,'uname':'Buck','gender':'Male'},
{'uid':90,'uname':'Meredeth','gender':'Male'},
{'uid':91,'uname':'Maurine','gender':'Female'},
{'uid':92,'uname':'Manolo','gender':'Male'},
{'uid':93,'uname':'Niki','gender':'Male'},
{'uid':94,'uname':'Melisandra','gender':'Female'},
{'uid':95,'uname':'Myranda','gender':'Female'},
{'uid':96,'uname':'Calley','gender':'Female'},
{'uid':97,'uname':'Wallace','gender':'Male'},
{'uid':98,'uname':'Jeannette','gender':'Female'},
{'uid':99,'uname':'Wilie','gender':'Female'},
{'uid':100,'uname':'Rebeca','gender':'Female'}]

user_col.insert_many(users)
print("Document inserted successfully")