from app import db, User

db.create_all()

user01 = User('test_user01','test01@test.com','1111')
user02 = User('test_user02','test02@test.com','2222')
db.session.add_all([user01, user02])

db.session.commit()

print(user01.id)
print(user02.id)