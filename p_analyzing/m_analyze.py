import pandas as pd
def country_df (project_df):
    countries = project_df['Country'].unique().tolist()
    select_country = input(f' Which country df dou you want to see? Options are:\n "all" or one of those\n{countries}')
    project_df.sort_values(by='Country')
    project_df.set_index(keys=['Country'], drop=False)
    if select_country == 'all':
        # % people working in X job, X country, living rural or urban
        project = project_df[['Country', 'title', 'rural']].groupby(['Country', 'title', 'rural']).size().reset_index(name='Quantity')
        project['Percentage'] = ((project['Quantity'] / project['Quantity'].count()) * 100).round(2)
        project['Percentage'] = project['Percentage'].apply(lambda x: str(x) + ' %')
        print(project)
    elif select_country in countries:
        selected = project_df.loc[project_df.Country == select_country]
        print(selected)
    else:
        print(f'Sorry, {select_country} is not an option')

def group_count (project_df):
    project = project_df[['Country', 'title', 'rural']].groupby(['Country', 'title', 'rural']).size().reset_index(name='Quantity')
    return project

def percentage (project):
    # % people working in X job, X country, living rural or urban
    project['Percentage'] = ((project['Quantity'] / project['Quantity'].count()) * 100).round(2)
    project['Percentage'] = project['Percentage'].apply(lambda x: str(x) + ' %')
    project.to_csv('data/results/jobs_by_country.csv', sep=',')
    print('Done!')

