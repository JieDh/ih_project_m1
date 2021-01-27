from p_acquisition.m_acquisition import get_webscrapping, get_db, get_api
from p_wrangling.m_wrangling import change_rural_col, cleaning_web, merging_db_api, final_df
from p_analyzing.m_analyze import group_count, percentage, country_df


def main():
    # acquisition
    api = get_api()
    db = get_db()
    web = get_webscrapping()
# wrangling
    final_db = change_rural_col(db)
    country_code = cleaning_web(web)
    merged = merging_db_api(db, api)
    project_df = final_df(merged, country_code)
# analyze
    country = country_df(project_df)
    project = group_count(project_df)
    results = percentage(project)


if __name__ == '__main__':
    main()
