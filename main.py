from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item.db'
db = SQLAlchemy(app)


class Item(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(200), nullable=False)
    itemStatus = db.Column(db.String(50), nullable=False)

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
        item_list = Item.query.order_by(Item.itemID).all()
        return render_template('home.html', item_list=item_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
