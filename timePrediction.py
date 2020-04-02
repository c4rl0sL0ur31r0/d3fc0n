
import time
import collections

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import warnings; warnings.simplefilter('ignore')

from sklearn.preprocessing import scale
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Display up to 150 rows and columns
pd.set_option('display.max_rows', 220)
pd.set_option('display.max_columns', 150)

# Set the figure size for plots
mpl.rcParams['figure.figsize'] = (14.6, 9.0)

# Set the Seaborn default style for plots
sns.set()

# Set the color palette
sns.set_palette(sns.color_palette("muted"))

# Load the preprocessed GTD dataset
gtd_df = pd.read_csv('global_processed.csv',
                     low_memory=False,
                     index_col = 0,
                     na_values=[''])

# Display a summary of the data frame
gtd_df.info(verbose = True)
gtd_df['incident_date'] = pd.to_datetime(gtd_df['incident_date'])
gtd_df['gname'] = gtd_df['gname'].astype('str')

gtd_df = gtd_df.drop(['provstate', 'city', 'summary', 'corp1', 'target1',
                                  'scite1', 'dbsource'], axis=1)


scaler = preprocessing.StandardScaler()

# List of numeric attributes
scale_attrs = ['nperpcap', 'nkill', 'nkillus', 'nkillter', 'nwound', 'nwoundus', 'nwoundte']

# Normalize the attributes in place
gtd_df[scale_attrs] = scaler.fit_transform(gtd_df[scale_attrs])

# View the transformation
gtd_df[scale_attrs].describe().transpose()
gtd_df.to_csv("global_cleaned.csv", sep = ",")

#spain_df = gtd_df[gtd_df['region_txt'] == "Western Europe"].query('1970<iyear<=2018')
spain_df = gtd_df
spain_df.info(verbose = True)

# Group by incident_date
spain_counts = spain_df.groupby(['incident_date'], as_index = False).count()
spain_counts = spain_counts[['incident_date', 'iyear']]
spain_counts.columns = ['incident_date','daily_attacks']
spain_counts.head()

idx = pd.date_range('1970-01-01', '2017-12-31')
spain_ts = spain_counts.set_index('incident_date')

spain_ts = spain_ts.reindex(idx, fill_value=0)
spain_ts.head()

spain_ts.describe()


import fbprophet
import numpy as np
spain_fb = spain_ts.copy()
spain_fb['index1'] = spain_fb.index
spain_fb.columns = ['y', 'ds']

spain_fb.head()
prophet1 = fbprophet.Prophet(changepoint_prior_scale=0.15, daily_seasonality=True)
prophet1.fit(spain_fb)
# Specify 365 days out to predict
future_data = prophet1.make_future_dataframe(periods=1460, freq = 'D')

# Predict the values
forecast_data = prophet1.predict(future_data)
print(forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
print('--*-- Convertions --*--')
print(np.exp(forecast_data[['yhat', 'yhat_lower', 'yhat_upper']]))


prophet1.plot(forecast_data, xlabel = 'Date', ylabel = 'Attacks')
plt.title('Predicted Terrorist Attacks in World', fontsize=10);
plt.savefig("Global.png");

prophet1.plot_components(forecast_data)
plt.title('Predicted Terrorist Attacks Components in World', fontsize=10);
plt.savefig("Global_components.png");

prophet1.plot(forecast_data, xlabel = 'Date', ylabel = 'Attacks')
#print(prophet1.predict(forecast_data))
plt.title('Predicted Terrorist Attacks in World', fontsize=20);
plt.xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2023-12-30'))
plt.savefig("Global_future.png");
