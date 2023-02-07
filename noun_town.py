from textblob import TextBlob
import csv
import pandas as pd

df = pd.read_csv('mrbeast_videos.csv')
df.rename(columns={'0': 'completion'}, inplace=True)
df['prompt'] = df['completion'].apply(lambda x: TextBlob(x).noun_phrases)
df = df.explode('prompt')
df.to_csv('mrbeast_nouns.csv', index=False)