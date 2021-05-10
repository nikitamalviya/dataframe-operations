# read csv
data = pd.read_csv(datapath, engine="python")
print(data.shape, data.columns)


# read required columns only 
data_orig = pd.read_csv(datapath, engine="python")
selected_column_names = ['email', 'category','subcategory','department', 'subject','service']
data = data_orig[selected_column_names]


# getting unique and unique value counts 
app['category'].unique()
app['category'].value_counts()


# merge values of columns into a new column
data["categoryService"] = (data["category"] + " , " + data["department"]).astype("string") # merging string values


# merging dataframes
resultant_data = pd.concat([df1, df2, df3, df4])


# save dataframe into csv
data.to_csv(path + "mydata.csv")


# access dataframe row using index number
row_index = 0
data['department'].iloc[row_index])


# access row using column value
print(df.loc[df['Name'] == 'Bert'])


df.set_index("Name", inplace=True)
print(df.loc[['Gwen', 'Page']])


# selecting rows having particular value
app = data[data['department'] == 'Application Management']


# selecting rows based on multiple condition
options = ['Math', 'Commerce']
# selecting rows based on condition
rslt_df = dataframe[dataframe['Stream'].isin(options)]


# add a row in existing dataframe
index = 0
new_row = {'department':5, 'email': df1['email'].iloc[index], 'subject': df1['subject'].iloc[index]}
data = data.append(new_row, ignore_index=True)


# drop a row using index number
data = data.drop(data.index[index])


# drop duplicate rows
data.drop_duplicates()


# drop the rows even with single NaN or single missing values
df_data.dropna()


# drop an observation or row
df_data.drop([1,2]) # 1 &  2 are the index here


# drop a row by condition
df_data[df_data.Name != 'Nikita']


# rename dataframe column name
data = data.rename(columns = {'email_processed':'email'}, inplace = True) 


# drop duplicates
result_df = df.drop_duplicates()


# drop all duplicates 
result_df = df.drop_duplicates(keep=False)


# drop duplicate rows & keep the last row 
df.drop_duplicates(keep='last')


# find the row is duplicated or not by making a new column with True/False status
df["is_duplicate"]= df.duplicated()


# sorting of dataframe column ascending order (Ranking)
df['score_ranked']=df['Score'].rank(ascending=1)


# Ranking of score descending order
df['score_ranked']=df['Score'].rank(ascending=0)


# create an empty dataframe
data = pd.DataFrame(columns=['a', 'b', 'c'])


# create a new dataframe
data = pd.DataFrame(columns=['email', 'department', 'department_1'])
data['email'] = unique_emails # list of items having same length as another columns value
data['department'] = department # list of items having same length as another columns value
data


# editing or change dataframe column values
for index in range(data.shape[0]):
    value = data['category'].iloc[index]
    if value == 'Access Modification' or cat_value == 'Access Removal':
        data['category'].iloc[index] = 'New Request - Access'                

        
# label encoding using sklearn
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['department_1'] = label_encoder.fit_transform(data['department'])
print(data['department'].value_counts(), data['department_1'].value_counts())


# plot graph for analyzing column's value
import seaborn as sns
plt.figure(figsize=(16, 4))
sns.barplot(data['department'].value_counts().index, data['department'].value_counts().values)
plt.show()

