# dye-etl
ETL for Dye house data

# Installation

Create a venv called venv

`python -m venv venv`

Activate venv, for windows:

`.\venv\Scripts\activate`

pip install the requirements file

`pip install -r requirements.txt`

Make a copy of file `.env.example` and rename it `.env`. This file contains the environment variables such Notion API key. Populate the relevant variables

# Execution

`main.py` under `src/dye_etl` is the main script that would run the pipeline end to end

# Future work

Unfortunately I was not successful in completing the task, I might have spent too much time in small but nice aspects, e.g. pydantic models, env variables, rather than quickly advancing with the task

- transform the extracted data
    - identify blank sample from list of samples
    - calc the concentration of pigment
    - ...
- load the transformed data onto a database, e.g. PostgreSQL

Additionally, would be good to implement the following:
- unit testing
- populate config file and create a pydantic config model
- create a separate repo to deal with connecting to Notion
