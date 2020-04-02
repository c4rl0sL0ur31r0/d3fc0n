
import pandas as pd
import numpy as np

gtd_df = pd.read_excel('globalterrorismdb_0919dist.xlsx',
                        # low_memory=False,
                        index_col = 0,
                        na_values=[''])


print('---*--- DATASET READ ---*---')
gtd_df['iday'].fillna('NaN',inplace=True)
gtd_df['location'].fillna('UNKNOWN',inplace=True)
gtd_df['attacktype1'].fillna('UNKNOWN',inplace=True)

# print(gtd_df['location'])

gtd_df['specificity'].fillna(-1, inplace=True)

gtd_df.loc[gtd_df['vicinity'] == -9, 'vicinity'] = -1

gtd_df.loc[gtd_df['doubtterr'] == -9, 'doubtterr'] = -1

gtd_df['targsubtype1_txt'].fillna('UNKNOWN', inplace=True)

gtd_df['natlty1_txt'].fillna('UNKNOWN', inplace=True)

gtd_df['guncertain1'].fillna(-1, inplace=True)

gtd_df['claimed'].fillna(-1, inplace=True)
gtd_df.loc[gtd_df['claimed'] == -9, 'claimed'] = -1

gtd_df['weapsubtype1_txt'].fillna('UNKNOWN', inplace=True)

gtd_df.loc[gtd_df['property'] == -9, 'property'] = -1

gtd_df['ishostkid'].fillna(-1, inplace=True)
gtd_df.loc[gtd_df['ishostkid'] == -9, 'ishostkid'] = -1

gtd_df.loc[gtd_df['INT_LOG'] == -9, 'INT_LOG'] = -1

gtd_df.loc[gtd_df['INT_IDEO'] == -9, 'INT_IDEO'] = -1

gtd_df.loc[gtd_df['INT_MISC'] == -9, 'INT_MISC'] = -1

gtd_df.loc[gtd_df['INT_ANY'] == -9, 'INT_ANY'] = -1


# Numeric Variables
print('---*--- PROCESSING NUMERIC VARIABLES ---*---')
# -----------------
gtd_df.loc[gtd_df['nperpcap'] == -9, 'nperpcap'] = np.nan
gtd_df.loc[gtd_df['nperpcap'] == -99, 'nperpcap'] = np.nan

# Text Variables
print('---*--- PROCESSING TEXT VARIABLES ---*---')
# --------------
gtd_df['provstate'].fillna('UNKNOWN', inplace=True)
gtd_df['city'].fillna('UNKNOWN', inplace=True)
gtd_df.loc[gtd_df['city'] == 'Unknown', 'city'] = 'UNKNOWN'
gtd_df['summary'].fillna('UNKNOWN', inplace=True)
gtd_df['corp1'].fillna('UNKNOWN', inplace=True)
gtd_df['target1'].fillna('UNKNOWN', inplace=True)
gtd_df['scite1'].fillna('UNKNOWN', inplace=True)

# Shorten Long Categories
gtd_df.loc[gtd_df['weaptype1_txt'] ==
           'Vehicle (not to include vehicle-borne explosives, i.e., car or truck bombs)',
           'weaptype1_txt'] = 'Vehicle (non-explosives)'

gtd_df.loc[gtd_df['attacktype1_txt'] ==
           'Hostage Taking (Barricade Incident)',
           'attacktype1_txt'] = 'Hostage Taking (Barricade)'

# CONVERT ATRIBUTES TO CATEGORICAL
print("--*-- CATEGORICAL ATRIBUTES --*--")
print(gtd_df.dtypes)

# List of attributes that are categorical
#cat_attrs = ['extended_txt', 'country_txt', 'region_txt', 'specificity', 'vicinity_txt',
#             'crit1_txt', 'crit2_txt', 'crit3_txt', 'doubtterr_txt', 'multiple_txt',
#             'success_txt', 'suicide_txt', 'attacktype1_txt', 'targtype1_txt',
#             'targsubtype1_txt', 'natlty1_txt', 'guncertain1_txt', 'individual_txt',
#             'claimed_txt', 'weaptype1_txt', 'weapsubtype1_txt', 'property_txt',
#             'ishostkid_txt', 'INT_LOG_txt', 'INT_IDEO_txt', 'INT_MISC_txt', 'INT_ANY_txt']

#for cat in cat_attrs:
#    gtd_df[cat] = gtd_df[cat].astype('category')

#gtd_df.info(verbose=True)

# Summary Statics
gtd_df[['nperpcap', 'nkill', 'nkillus', 'nkillter', 'nwound',
        'nwoundus', 'nwoundte']].dropna().describe(percentiles = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]).transpose()


# INCIDENT DATE
print('--*-- PROCESS INCIDENT DATE --*--')
# 297 iday attributes contain 0 to represent unknown, setting 1
gtd_df.loc[gtd_df['iday'] == 0, 'iday'] = 1
gtd_df.loc[gtd_df['imonth'] == 0, 'imonth'] = 1

gtd_df['incident_date'] = (gtd_df['iyear'].astype(str) + '-' +
                              gtd_df['imonth'].astype(str) + '-' +
                              gtd_df['iday'].astype(str))

gtd_df['incident_date'] = pd.to_datetime(gtd_df['incident_date'],
                                            format="%Y-%m-%d")

gtd_df.to_csv("global_processed2.csv", sep = ",")
print(" *** *** DATASET CLEANED *** *** ")
