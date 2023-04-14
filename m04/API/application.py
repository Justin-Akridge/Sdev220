from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80))
    author = db.Column(db.String(80), unique=True, nullable=False)
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.author} - {self.publisher} - {self.book_name}"

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    return 'Hello!'

@app.route('/books', methods=['GET', 'POST'])
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"book", output}

@app.route('/books/<id>') 
def get_book(id):
        book = book.query.get_or_404(id) 
        return {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
        book = Book(book_name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
        db.session.add(book)
        db.session.commit()
        return {'id': book.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"} 
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book is deleted"}
