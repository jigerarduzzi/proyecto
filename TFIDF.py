#'''Text classification: TFIDF (ELI5) with Sklearn logistic regression'''
#
#py -m pip install scikit-learn
from sklearn.model_selection import train_test_split  
from sklearn.model_selection import cross_val_score, StratifiedKFold  
from sklearn.pipeline import Pipeline  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import classification_report  
import numpy as np  
#py -m pip install seaborn
import seaborn as sns  
import pandas as pd  
#import eli5__author__= "https://medium.com/@guzman.gp"
import matplotlib.pyplot as plt
#py -m pip install eli5
import eli5
import warnings
warnings.filterwarnings("ignore")


file_alias = "Dataset"  

path_to_data = f'datasets/{file_alias}.csv'

try:   
    df = pd.read_csv(path_to_data, low_memory=False)  
    print(df.columns)
    fig,ax = plt.subplots()
    df['labels'].value_counts().plot(ax = ax, kind = 'bar', ylabel = 'frequency')
    plt.show()
except FileNotFoundError:   
    raise FileNotFoundError(f"File {file_alias} at path {path_to_data} doesn't exist.")

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['labels'], test_size=0.1, random_state=12)
cv = StratifiedKFold(n_splits=2, shuffle=True)

tfidf_vectorizer = TfidfVectorizer(smooth_idf=True, norm='l2', sublinear_tf=True)
lgr_model = LogisticRegression(C=25, solver='saga', max_iter=2000)
lgr_pipeline = Pipeline([('tfidf', tfidf_vectorizer),('clf', lgr_model)])

lgr_pipeline.fit(X_train, y_train)
len(lgr_pipeline[0].get_feature_names_out())

scores = cross_val_score(lgr_pipeline, X_train, y_train, cv=cv)  
sc_mean = scores.mean()  
sc_dev = scores.std()*2  
print(f'''Accuracy per fold: {scores}  Mean accuracy: {round(scores.mean(),3)}  Std. deviation: +- {round(scores.std()*2,3)}''')

#hay que instalar ipython para que funcione py -m pip install ipython
eli5.show_weights(lgr_pipeline, vec=lgr_pipeline[0], top=20, feature_filter=lambda x: x != '<BIAS>')

y_pred = lgr_pipeline.predict(X_test)  
confs_matrix = pd.crosstab(y_test, y_pred)  
sns.heatmap(confs_matrix, annot=True, cbar=True) 
y_test = list(y_test)  
X_test = list(X_test)  
mistakes = [X_test[i] for i in range(len(y_pred)) if y_test[i] != y_pred[i]]  
print(classification_report(y_test, y_pred))

print(f'{len(mistakes)} mistakes from {len(y_test)} validation samples:')  
for i,f in enumerate(mistakes):   print(f"X {f} -> {y_test[i]}")




