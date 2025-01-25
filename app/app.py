from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/crud_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Criação automática das tabelas
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Item.query.get(id)
    if request.method == 'POST':
        item.name = request.form['name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/add', methods=['POST'])
def add():
    new_item = Item(name=request.form['name'])
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')