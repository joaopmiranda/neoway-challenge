from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


classifiers ={
    "MultinomialNB": Pipeline([
                                ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
                                ('model', MultinomialNB())
                            ]),
    "RandomForestClassifier": Pipeline([
                                ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
                                ('model', RandomForestClassifier())
                            ]),
    "XGBClassifier": Pipeline([
                            ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
                            ('model', XGBClassifier(
                                n_jobs=-1,
                                max_depth=10,
                                learning_rate=0.1, 
                                n_estimators=500
                            ))
                        ])    
}