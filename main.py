from flask import Flask, render_template, url_for, request, redirect
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


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        item_new = request.form['new_item']
        new_item_db = Item(item_name=item_new)

        try:
            db.session.add(new_item_db)
            db.session.commit
            return redirect('/')
        except:
            return "Failed to find"
    else:
        list = Item.query.order_by(Item.item_id).all()
        return render_template('home.html', list=list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
