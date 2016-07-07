from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

a_train = load_files('txt_sentoken/',encoding='latin-1') #put this file in the movie_reviews folder in the nltk corpus


count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(a_train.data)


tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, a_train.target)
newArray = ['god is great', 'this movie was bad','this guy is atrocious']
X_new_counts = count_vect.transform(newArray)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(newArray, predicted):
     print('%r => %s' % (doc, a_train.target_names[category]))


