import requests
import pandas as pd
from sqlalchemy import create_engine

def setup(api_key):
    """
    setting API Key
    """
    # api_key = requests.get('http://api.dataatwork.org/v1/spec/skills-api.json')

def get_rural(path):
    engine = create_engine('sqlite:///data/raw_data_project_m1.db')
    rural = pd.read_sql_query("select * from country_info", engine)
    return rural

def acquisition(path, api_key):
    # print('setting api key...')
    # setup(api_key)

    jobs_api = setup(api_key)

    #getting db
    print('getting db as df')
    rural_classification = get_rural(path)
    print(f'got (len{rural_classification})')
    #getting only the column we need
