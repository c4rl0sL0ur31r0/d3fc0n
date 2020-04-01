import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier

df = pd.read_excel('dataset/DataToTrain.xlsx')
# for i in change_listBoolean:
#    df[i] = (df[i]).astype(dtype=bool)

# df['iyear'] = (df['iyear']).astype('uint8')
#df['imonth'] = (df['imonth']).astype('uint8')
#df['iday'] = (df['iday']).astype('uint8')

df['country'] = (df['country']).astype('category')
# df['region_txt'] = (df['region_txt']).astype('category')
# df['provstate'] = (df['provstate']).astype('category')
# df['attacktype1'] = (df['attacktype1']).astype('category')
df['targtype1'] = (df['targtype1']).astype('category')
# df['targsubtype1'] = (df['targsubtype1']).astype('category')
# df['weaptype1'] = (df['weaptype1']).astype('category')
df['success'] = (df['success']).astype('boolean')
df['suicide'] = (df['suicide']).astype('boolean')
df['individual'] = (df['individual']).astype('boolean')
#df['crit1'] = (df['crit1']).astype('bool')
#df['crit1'] = (df['crit1']).astype('bool')

print(df.head())

# objetivo = 'targtype1_txt', 'weaptype1_txt'
# ideology =         'Anarq', 'ENVT', 'COMM', 'AntiFascista', 'LW', 'RW',
#         'NS', 'Jihad', 'NeoLudita', 'RE', 'SUPR'

X = df[['country', 'success', 'suicide', 'individual', 'attacktype1',
        'targtype1', 'weaptype1','iyear','imonth','iday']]

y = df[['crit1','crit2','crit3']]

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    stratify=df[['region_txt']])

max_depth = 30

regr_rf = RandomForestClassifier(n_estimators=300,
                                 max_depth=max_depth,
                                 random_state=0,
                                 n_jobs=-1,
                                 verbose=True
                                 )

regr_rf.fit(X_train, y_train)

# Predict on new data
# y_multirf = regr_multirf.score(X_test,y_test)
y_rf = regr_rf.score(X_test, y_test)
# print(y_multirf)
print("Score RF: %s" % y_rf)
percent = y_rf * 100
# 0.8494


print('READY TO SAVE MULTI_CRITERIAL MODEL PREDICTIONS: %s' % percent)

filename = 'predictores/predict_MutiCriteria_model.sav'
pickle.dump(regr_rf, open(filename, 'wb'))
print("Model %s SAVED" % filename)

# to load model
# load the model from disk
# individual = pickle.load(open(filename, 'rb'))
# print(result)
