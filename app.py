from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import pandas as pd
import pickle


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

file_name = 'sim_df.pkl'
df = pd.read_pickle(file_name)


with open('authors_list.pkl','rb') as f:
    authors = pickle.load(f)


def get_score(lst, author_1, author_2):
  try:
    id_1 = lst.index(author_1)
    id_2 = lst.index(author_2)
  except ValueError:
    return "One or both authors do not exist"
  return str(int(df[id_1][id_2] * 100))


class Authors2score(FlaskForm):
    author_1 = StringField("one name", validators=[DataRequired()])
    author_2 = StringField("another name", validators=[DataRequired()])
    submit = SubmitField("get score", validators=[DataRequired()])


@app.route("/hwllo")
def hello():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def form():
    score = None
    form = Authors2score()
    if form.validate_on_submit():
        author_1 = form.author_1.data
        author_2 = form.author_2.data
        score = get_score(authors, author_1, author_2)
    return render_template("index.html",
                           form=form,
                           score=score)


if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)