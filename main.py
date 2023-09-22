from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item.db'
db = SQLAlchemy(app)


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), nullable=False)
    item_status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.item_id


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
