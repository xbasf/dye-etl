import requests


def query_table(
    api_key: str, database_id: str, notion_table_page_size: int = 100
) -> dict:
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    payload = {"page_size": notion_table_page_size}
    try:
        response = requests.post(
            url, json=payload, headers=headers, timeout=120
        )
    except requests.ConnectionError as error:
        print(error)

    return response.json()
