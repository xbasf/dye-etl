import os

from connection import query_table
from dotenv import load_dotenv
from extract import extract

load_dotenv()

NOTION_TOKEN = os.environ.get("NOTION_API_KEY")
DATABASE_ID = os.environ.get("NOTION_TABLE_ID")

raw_data = query_table(api_key=NOTION_TOKEN, notion_table_page_size=DATABASE_ID)
dye_houses = extract(raw_data=raw_data)

# NOTE: transform would follow..
