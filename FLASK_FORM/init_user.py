from app import db, User

db.create_all()

user01 = User('Admin_user01','admin01@test.com','1111',"1")
user02 = User('Test_user01','test01@test.com','1111',"0")
db.session.add_all([user01, user02])

db.session.commit()

print(user01.id)
print(user02.id)