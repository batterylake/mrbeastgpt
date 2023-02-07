import pandas as pd

df = pd.read_csv('mrbeast_titles_clean.csv')

#clean up completion by removing quotation marks
df['completion'] = df['completion'].str.replace('"', '')

#clean up compeltion by making everything lowercase
df['completion'] = df['completion'].str.lower()

#add the phrase "is an example of a possible title for a YouTube video" to the end of each completion
df['completion'] = df['completion'] + ' would be a good title for a MrBeast video'

#add the phrase "hello" to the beginning of each prompt
df['prompt'] = 'create a YouTube video title using the phrase "' + df['prompt']

#export the dataframe to a csv file called "mrbeast_prompts.csv"
df.to_csv('mrbeast_prompts.csv', index=False)
print('complete')