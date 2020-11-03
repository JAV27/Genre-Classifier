import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import tensorflow as tf

seq_length = 100
step = seq_length
# maxlen = 1000

df = pd.read_csv("data.csv", index_col="index")
df = df.reindex(np.random.permutation(df.index))
df.columns = ["label", "text"]
labels = df["label"].to_numpy()
texts = df["text"].to_numpy()

tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
# x = pad_sequences(x, maxlen=maxlen, padding="post")

label_encoder = LabelEncoder()
label_encoder.fit(["Rock", "Pop", "Hip Hop"])
encoded_labels = label_encoder.transform(labels)

data = np.concatenate(sequences, encoded_labels, axis=1)

print(data.shape)
exit()

# def preprocess(

x = []
y = []
for label_ind, sequence in enumerate(sequences):
    for i in range(0, len(sequence) - seq_length, step):
        x.append(sequence[i: i+seq_length])
        y.append(encoded_labels[label_ind])

x = to_categorical(x)
y = to_categorical(y)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.4, random_state=42)


