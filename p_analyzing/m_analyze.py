
def country_df (project_df):
    countries = project_df['Country'].unique().tolist()
    select_country = input(f' Which country df dou you want to see? Options are:\n "all" or one of those\n{countries}')
    project_df.sort_values(by='Country')
    if select_country == 'all':
        # % people working in X job, X country, living rural or urban
        project = project_df[['Country', 'Title', 'Rural']].groupby(['Country', 'Title', 'Rural']).size().reset_index(name='Quantity')
        project['Percentage'] = ((project['Quantity'] / project['Quantity'].sum()) * 100).round(2)
        project['Percentage'] = project['Percentage'].apply(lambda x: str(x) + ' %')
        project.to_csv('data/results/jobs_by_country.csv')
        print(project)
    elif select_country in countries:
        selected = project_df.loc[project_df.Country == select_country].groupby(['Title', 'Rural']).size().reset_index(name='Quantity')
        selected['Percentage'] = ((selected['Quantity'] / selected['Quantity'].sum()) * 100).round(2)
        selected['Percentage'] = selected['Percentage'].apply(lambda x: str(x) + ' %')
        selected.to_csv(f'data/results/jobs_by_rural_{select_country}.csv')
        print(selected)
    else:
        print(f'Sorry, {select_country} is not an option')
