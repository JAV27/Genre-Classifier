import pandas as pd
import re

data = pd.read_csv("data.csv", index_col="index")
data["Lyric"] = data["Lyric"].map(lambda line: re.sub("\[.{0,100}\]", "", line))
data["Lyric"] = data["Lyric"].map(lambda line: re.sub("\(.{0,100}\)", "", line))

data.to_csv("new_data2.csv")
