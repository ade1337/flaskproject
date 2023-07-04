from app import app, db, Article, Category

a = Article(category_id = 2, title='Статья2', introduction = 'Вступление2', text = 'Текст статьи2')

with app.app_context():
    db.session.add(a) # user как пример
    db.session.commit()
