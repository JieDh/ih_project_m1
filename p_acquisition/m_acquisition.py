# importing all modules we gonna need
from sqlalchemy import create_engine
import pandas as pd
import requests


def get_db():
    engine = create_engine('sqlite:///data/raw/raw_data_project_m1.db')
    db_df = pd.read_sql_query(
        "SELECT country_info.uuid, country_info.country_code, country_info.rural, career_info.normalized_job_code FROM country_info JOIN career_info ON career_info.uuid = country_info.uuid",
        engine)
    return db_df


def get_api():
    response = requests.get('http://api.dataatwork.org/v1/jobs/861a9b9151e11362eb3c77ca914172d0/related_jobs')
    #transform the data into a json type
    transform = {"uuid": "97540260779e3ed95254cec83475ed07", "title": "Applications Systems Analyst",
                 "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "861a9b9151e11362eb3c77ca914172d0",
                                                                      "title": "Automatic Data Processing Planner",
                                                                      "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "50c2c974472fde19aed2e47b35691577", "title": "Computer Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "9d7dda6d7915650c681128203a896506",
                                                                         "title": "Computer Analyst Supervisor",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "5ab17bbc6fd0008e239d2d4be22f6a6c", "title": "Computer Methods Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "fcaf4aac737e53ad24b9f32f08b8740f",
                                                                         "title": "Computer or Data Processing Systems Consultant",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "9c2953b636a8cc64e87087594868ed58", "title": "Computer Systems Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "bf2e6241e484f7b95b6f56e947d3ca53",
                                                                         "title": "Computer Systems Consultant",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "e79df6bc40d3640f7f1c0d45298f5989", "title": "Computer Systems Design Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "d803646eb5eb0353451a13c8f6fc7f9e",
                                                                         "title": "Computer Systems Designer",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "721f8a5289ff95f866272ea0941b6459", "title": "Cross-Enterprise Integrator",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "894ca61c22718617c7e2404f582153da",
                                                                         "title": "Data Processing Consultant",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "e7b3e1c6a32c7247cd4857e4c3574165", "title": "Data Processing Systems Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "b24ece3300d2f8ab34f9553e531183d6",
                                                                         "title": "Data Processing Systems Project Planner",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "70150ea5cc2c4a0dcb9d3dc238835f2e", "title": "Digital Computer Systems Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "747b0eb1a51900e9c200409022732366",
                                                                         "title": "E-Business Specialist",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "efa63c7ddecde82a992dcc9c2175d0ab", "title": "Engineering Systems Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "f7e387ed7f3b36dc521a46160ca91954",
                                                                         "title": "Functional Analyst",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "1749cdbc2468d6628bcd833ff0ac1a11", "title": "Healthcare Applications Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "7cf9a601e023e14526d10cc77605e401",
                                                                         "title": "Information Systems Analyst (ISA)",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "968efdcdc4f635e64f6bf9978c9d52e9", "title": "Information Systems Architect",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "c5c0c419a2ae9b68c9244bb6ac995073",
                                                                         "title": "Information Systems Consultant",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "8fd2c0b754c45385dd8b68c34f71c505",
                    "title": "Information Technology Generalist (IT Generalist)",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "f271021b74461e6226374cbc7d465941",
                                                                         "title": "Information Technology Specialist (ITS)",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "d5a901898ceaeadb622d28d73d83e3cb", "title": "Information Technology Systems Manager",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "cdf220c51580a4b7cdc548dadd630ab9",
                                                                         "title": "Internet E-Commerce Specialist",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "63b451f06614bd51fd53a70879afdad5",
                    "title": "IT Business Analyst (Information Technology Business Analyst)",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "7604157a983a06a7908cdd0698e4a0a2",
                                                                         "title": "Management Information System Analyst (MIS Analyst)",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "2e8ad38bd092daaaf8955ba735c19440", "title": "Programming Specialist",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "060721c98fdfc207dbc8d1d8e37a7232",
                                                                         "title": "Scientific Systems Analyst",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "7c1a76c4c31058476f255402242d9927", "title": "Software Consultant",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "12f112b5a3fba1af653835f51c257330",
                                                                         "title": "Systems Administration Analyst",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "e5a8bd5e00b6c3ec703eaec9a28d80bd",
                    "title": "Systems Analysis Information Technology Specialist",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "6debe7648b28e668b47b135cdc002ef5",
                                                                         "title": "Systems Architect",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "2808fb0c20b6bd4ba7cb423360122372", "title": "Health Systems Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "a135111342b3da84c967eba58e8c494e",
                                                                         "title": "Information Systems Auditor",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "90974ee1e64d53f4ab01d863fd105cdb", "title": "Information Systems Planner",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "e0a65e148d67764a6fcba9c1cd5ec024",
                                                                         "title": "Information Technology Auditor (IT Auditor)",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}, {
                    "uuid": "90082e1c828d92eccbb9c4b7a145b06b", "title": "Applications Analyst",
                    "parent_uuid": "0148f61d4227497728ce33490843d056"}, {"uuid": "cf81121543f08d762c89add012cdd707",
                                                                         "title": "Business Analyst",
                                                                         "parent_uuid": "0148f61d4227497728ce33490843d056"}
    df_related_jobs = pd.json_normalize(transform)
    #renaming 'uuid' column to 'normalize_job_code'
    api_df = df_related_jobs.rename(columns={'uuid': 'normalized_job_code'})
    return api_df

def get_webscrapping():
    country_url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    dfs = pd.read_html(country_url)
    web_df = pd.concat(dfs[0:13], axis=1, ignore_index=True)  # axis=1 so we don't have code with country mixed
    return web_df
