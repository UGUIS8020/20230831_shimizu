from app import db,BlogPost

all_posts = BlogPost.query.all()
print(all_posts)