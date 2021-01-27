import re
import pandas as pd
db_name = 'raw_data_project_m1.db'

def change_rural_col(db_df):
    db_df.to_csv('data/processed/clean_db_df.csv', sep=',')
    return db_df

def cleaning_web(web_df):
    web_df = web_df.dropna(axis=1, how='all')
    country_melt = web_df[[0, 2, 4, 6, 8, 11, 13, 16, 18, 20, 23, 26, 28, 31, 34, 36, 38, 41, 44, 47]].melt(value_name='Country')['Country']
    code_melt = web_df[[1, 3, 5, 7, 9, 12, 14, 17, 19, 21, 24, 27, 29, 32, 35, 37, 39, 42, 45, 48]].melt(value_name='country_code')['country_code']
    code = pd.concat([country_melt, code_melt], axis=1)
    country_code = code[['Country', 'country_code']]
    country_code_df = country_code.dropna(axis=0, thresh=1)  # thresh = 1 so we need minimum 2 NaN values in a row
    def clean_parenthesis(code_column):
        return re.sub('[()]', '', code_column)

    country_code_df['country_code'] = country_code_df['country_code'].astype(str).apply(clean_parenthesis)
    country_code_csv = country_code_df.to_csv('data/processed/country_code.csv')
    return country_code_df

def merging_db_api (db, api):
    db_api = pd.merge(db, api, on=['normalized_job_code'], how='outer')
    return db_api

def final_df(db_api, country_code_df):
    project_df = pd.merge(db_api, country_code_df, on=['country_code'], how='outer')
    # Time to clean the final df!
    project_df.dropna(subset=['uuid', 'normalized_job_code', 'title'], inplace=True)
    project_df.reset_index(inplace=True)
    #drop index column that was created when we did the reset
    project_df.drop('index', axis=1, inplace=True)
    project_csv = project_df.to_csv('data/processed/project.csv')
    return project_df

