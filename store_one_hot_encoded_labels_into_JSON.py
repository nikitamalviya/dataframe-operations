import pickle

## STORE DICT into JSON
# 'data' is a dataframe with 'column' category
# 'label' is one-hot encoded label

d = {} #Empty dictionary to add values into
for label, code in zip(data['category'].value_counts().keys(),  data['category_code'].value_counts().keys()):
    d[code] = label 
