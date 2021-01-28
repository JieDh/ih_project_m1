# ih_project_m1
Ironhack Madrid - Data Analytics Part Time - November 2020 - Project Module 1

<p align="center">
  <img src="https://camo.githubusercontent.com/fc370d9811c3bf7ac72595d0af0aa53c0d7b1ac4db2cffe1193f1590014cda60/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3138342f312a3247446361655949785f6251415a4c78574d345073514032782e706e67">
</p>

### About
Given a country within a list, retrieve a csv about the country and it's jobs.


### :information_source: datasource
1. A database 
2. [Open Skills Project](http://dataatwork.org/data/) API
3. Country Codes from [Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes)

### :computer: **Technology stack**
Python and pandas

### :wrench: Configuration
Install Python 3.7 and pandas module. 

### :page_facing_up: Usage
    Parameters:
        a country within a list
    Returns:
        A dataframe and a csv

### :file_folder: Folder structure
```
└── ih_project_m1
    ├── data
    │   ├── processed
    │   └── raw
    │     └── raw_data_project_m1.db
    │   ├── results
    │     └── jobs_by_country
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── p_acquisition
    │   ├── m_acquisition.py
    │   └── init.py
    ├── p_analyzing
    │   ├── m_analyzing.py
    │   └── init.py
    ├── p_wrangling
    │   ├── m_wrangling.py
    │   └── init.py
    ├── .gitignore
    ├── README.md
    ├── main.py
