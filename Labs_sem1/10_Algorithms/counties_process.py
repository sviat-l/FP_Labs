"""Work with USA stated data"""
import pandas as pd


def read_data(path_to_file):
    """
    Read data from the file
    """
    return pd.read_csv(f'{path_to_file}')

def max_counties(df) -> str:
    """
    Return countie with the most number of cities
    >>> max_counties(pd.DataFrame({"STNAME":\
    ["Alaska","Alaska","Alaska","Florida","Florida","California"],"SUMLEV":[50,50,50,50,40,40]}))
    'Alaska'
    """
    return df['STNAME'].value_counts().index[0]
# print(max_counties(read_data('census.csv')))

def max_difference(df) -> str:
    """
    Return name of the
    >>> max_difference(pd.DataFrame({'SUMLEV': [50,50,50], \
    'CTYNAME': ['Geogria','Florida','Hawaii'], \
    'POPESTIMATE2010': [4888777, 1154571, 1282345], \
    'POPESTIMATE2011': [4834677, 1154571, 1283477], \
    'POPESTIMATE2012': [4888637, 1154660, 1283347], \
    'POPESTIMATE2013': [4883463, 1152253, 1284379], \
    'POPESTIMATE2014': [4846377, 1153175, 1297396], \
    'POPESTIMATE2015': [4813878, 1154038, 1264726]}))
    'Geogria'
    """
    df = df.loc[df['SUMLEV'] == 50]
    df['max_dif'] = df[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',\
                        'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015',]].max(axis=1)\
                    - df[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',\
                        'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015',]].min(axis=1)
    return df.sort_values(by='max_dif',ascending=False).iloc[0]['CTYNAME']

print(max_difference(read_data('census.csv')))

def conditional_counties(df):
    """
    Return dataframe with countries  if they suits to the conditions
    """
    return  df.loc[df['REGION'].isin([1,2]) & df['CTYNAME'].str.contains("Washin")\
                   & (df['POPESTIMATE2015'] > df['POPESTIMATE2014']),  ['STNAME', 'CTYNAME']]
# print(conditional_counties(read_data('census.csv')))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())