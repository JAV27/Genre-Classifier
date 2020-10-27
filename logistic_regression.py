from numpy.lib.scimath import log
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv", index_col="index")[:10000]
df.columns = ["label", "text"]

vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+'?\w*\b", stop_words="english")
labels = df["label"].to_numpy()
label_encoder = LabelEncoder()
label_encoder.fit(["Rock", "Pop", "Hip Hop"])

x = vectorizer.fit_transform(df["text"].to_numpy())
y = label_encoder.transform(labels)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.4, random_state=42)

logreg = LogisticRegression()
logreg.fit(train_x, train_y)

weights = logreg.coef_

for i in range(3):
    print("-------------")
    maxVals = []
    for j, data in enumerate(weights[i]):
        maxVals.append((data, j))

    sortedVals = sorted(maxVals, key=lambda x: x[0], reverse=True)

    for k in sortedVals[:10]:
        print(vectorizer.get_feature_names()[k[1]])

preds = logreg.predict(test_x)
print(accuracy_score(test_y, preds))
print(confusion_matrix(test_y, preds))
for i in range(3):
    print(i)
    print(precision_score(test_y, preds, labels=[i], average="weighted"))
    print(recall_score(test_y, preds, labels=[i], average="weighted"))