from database import init_db
from database import db_session
from models import Car
print("SEEDING TEST DATABASE")
init_db()
car = Car('Chevy', 'Cruise', 'Red', '2000')
db_session.add(car)

car = Car('Ford', 'Mustang', 'Red', '2012')
db_session.add(car)


car = Car('Aston Martin', 'DB5', 'Silver', '1964')
db_session.add(car)

car = Car('Toyota', 'Camry', 'Blue', '2012')
db_session.add(car)


db_session.commit()
print("DONE!")