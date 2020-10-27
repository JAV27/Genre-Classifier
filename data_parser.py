import pandas as pd

artists = pd.read_csv("lyrics6genre/artists-data.csv", index_col="Link")
# lyrics = pd.read_csv("lyrics6genre/lyrics-data.csv", index_col="ALink")

# data = pd.DataFrame()

# data = artists.join(lyrics)

# data = data[data["Genre"] != "Sertanejo"]
# data = data[data["Genre"] != "Funk Carioca"]
# data = data[data["Genre"] != "Samba"]
# data = data[data["Idiom"] == "ENGLISH"]

# data = data[["Genre", "Lyric"]]
# data.index = range(len(data))
# data.index.name = "index"

# data.to_csv("data.csv")
data = pd.read_csv("data.csv", index_col="index")

print(data)

# print(data)
# print(data["Genre"] in genres)

# print(data.loc[(data["Genre"] in genres).item()])
