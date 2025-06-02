from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, resources={r"/*": {"origins": "*"}})

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at).all()
    return jsonify([{
        'id': todo.id,
        'content': todo.content,
        'completed': todo.completed,
        'created_at': todo.created_at.isoformat()
    } for todo in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = Todo(content=data['content'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({
        'id': new_todo.id,
        'content': new_todo.content,
        'completed': new_todo.completed
    }), 201

@app.route('/todos/<int:id>/toggle', methods=['PATCH'])
def toggle_complete(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return jsonify({
        'id': todo.id,
        'content': todo.content,
        'completed': todo.completed
    })

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)