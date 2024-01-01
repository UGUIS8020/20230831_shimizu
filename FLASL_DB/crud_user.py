from app import db,User

user03 = User('test_user03','test03@test.com','3333')
db.session.add(user03)
db.session.commit()

all_users = User.query.all()
print(all_users)

userid_1 = User.query.get(1)
print(userid_1.username)

username_2 = User.query.filter_by(username='test_user02')
print(username_2.all())

userid_1 = User.query.get(1)
userid_1.username = 'test_user01_update'
db.session.add(userid_1)
db.session.commit()

userid_2 = User.query.get(2)
db.session.delete(userid_2)
db.session.commit()

all_users = User.query.all()
print(all_users)