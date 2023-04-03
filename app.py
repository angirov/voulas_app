import pandas as pd

dataframe_path = './similarity_matrix.csv'
similarity_df = pd.read_csv(dataframe_path, index_col=0)

def get_similarity_percentage(author1, author2, similarity_df):
    similarity = similarity_df.loc[author1, author2] * 100
    return round(similarity, 2)

def recommend_collaborators(author, similarity_df, num_recommendations=5):
    sorted_similarities = similarity_df[author].sort_values(ascending=False)
    top_recommendations = sorted_similarities.head(num_recommendations + 1).index.tolist()
    top_recommendations.remove(author)  # remove the input author from the recommendations
    return top_recommendations

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/similarity', methods=['POST'])
def similarity():
    author1 = request.form['author1']
    author2 = request.form['author2']
    similarity = get_similarity_percentage(author1, author2, similarity_df)
    return f"The similarity percentage between {author1} and {author2} is {similarity}%."

@app.route('/recommend', methods=['POST'])
def recommend():
    author = request.form['author']
    recommendations = recommend_collaborators(author, similarity_df)
    recommendations_str = ', '.join(recommendations)
    return f"Top {len(recommendations)} recommended collaborators for {author} are: {recommendations_str}"

if __name__ == '__main__':
    app.run()