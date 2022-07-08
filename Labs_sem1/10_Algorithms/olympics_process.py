""" Work with olipics date"""
import pandas as pd

def read_data():
    """ Read date from csv file return data frame"""
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)
    names_ids = df.index.str.split('\\s\\(') # split the index by '('
    df.index = names_ids.str[0] # the [0] element is the country name (new index)
    df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID
    df = df.drop('Totals')
    return df

def first_country(df):
    """ Return information from the first row"""
    return df.iloc[0,]

def summer_biggest(df):
    """ Return name of the country with the most number of summer gold medals
    >>> summer_biggest(pd.DataFrame({'Country': \
    ['United States','Bulgaria', 'Ukraine'], 'Gold': [786,42, 13],\
    'Gold.1': [133, 2, 12]},\
    index=['United States', 'Bulgaria', 'Ukraine']))
    'United States'
    """
    return df.sort_values(by='Gold',ascending=False).iloc[0,].name

def difference_biggest(df):
    """ Return name of the country with the most differense of gold medals
    >>> difference_biggest(pd.DataFrame({'Country': \
    ['United States','Bulgaria', 'Ukraine'], 'Gold': [786,42, 13],\
    'Gold.1': [133, 2, 12]},\
    index=['United States', 'Bulgaria', 'Ukraine']))
    'United States'
    """
    df['difference'] = abs(df['Gold.1'] - df['Gold'])
    return df.sort_values(by='difference',ascending=False).iloc[0,].name

def difference_biggest_relative(df):
    """ Return name of the country with the most relative differense of gold medals
    >>> difference_biggest_relative(pd.DataFrame({'Country': \
    ['United States','Bulgaria', 'Ukraine'], 'Gold': [786, 42, 13],\
    'Gold.1': [214, 2, 12]},\
    index=['United States', 'Bulgaria', 'Ukraine']))
    'Bulgaria'
    """
    df['rel_diff'] = abs(df['Gold.1'] - df['Gold'])/(df['Gold.1']+df['Gold']) % 1
    return df.sort_values(by='rel_diff',ascending=False).iloc[0,].name

def get_points(df):
    """ Return Series of the dataframe with points for medals """
    df['Points'] = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2']
    return df['Points']
