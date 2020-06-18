import pandas as pd                                                             #importing pandas

train_df = pd.read_csv('train.csv')                                             #reading glass.csv file
train_df['Sex'] = train_df['Sex'].map({'female': 1, 'male': 0}).astype(int)     # keeping female = 1 and male = 0 in sex Column
print(train_df['Survived'].corr(train_df['Sex']))                               # finding correlation and printing it