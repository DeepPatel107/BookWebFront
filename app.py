from flask import Flask, render_template,request
import pickle
import numpy as np

popular_df=pickle.load(open('popular2.pkl','rb'))
pt=pickle.load(open('pt (1).pkl','rb'))
similarity_scores=pickle.load(open('similarity_score (1).pkl','rb'))
books=pickle.load(open('books2.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values),
                           image2=list(books['Image-URL-M'].values),
                           )

@app.route('/recommend_books',methods=['post'])
def recommend_books():

    user_input=request.form.get('user_input')
    index_array = np.where(pt.index == user_input)[0]  # Extract the first element
    index = index_array[0]  # Now safely access the first index

    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[0:10]

    data = []

    for i in similar_items:
        item = []
        # Access the book index from similar_items using similar_items[i][0]
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    # Find the author of the given book
    author = books[books['Book-Title'] == user_input]['Book-Author'].values
    if len(author) == 0:
        return f"No books found for '{user_input}'"
    author = author[0]

    author_books = books[books['Book-Author'] == author]['Image-URL-M'].unique()

    return render_template('index.html',data=data,other_books=author_books)



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html',
                            book_name=list(popular_df['Book-Title'].values),
                            author=list(popular_df['Book-Author'].values),
                            image=list(popular_df['Image-URL-M'].values),
                            votes=list(popular_df['num_ratings'].values),
                            rating=list(popular_df['avg_ratings'].values),
                           )

@app.route('/createAcc')
def createAcc():
    return render_template('createAcc.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/book1')
def book1():
    return render_template('book1.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)