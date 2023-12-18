from typing import List

from src.dye_etl.data_model import DyeHouse


def extract(raw_data: dict) -> List[DyeHouse]:
    """
    This functionn extracts the information from the returned table query and
    returns a list of DyeHouse objects
    """
    dye_houses = list()
    for data_sample in raw_data["results"]:
        dye_houses.append(
            DyeHouse(
                sample_type=data_sample["properties"]["Sample type"]["select"][
                    "name"
                ],
                client=data_sample["properties"]["Client"]["select"]["name"],
                client_location=data_sample["properties"]["Client location"][
                    "select"
                ]["name"],
                fermentor_used=data_sample["properties"]["Fermentor used"][
                    "select"
                ]["name"],
                fermentor_model=data_sample["properties"]["Fermentor model"][
                    "select"
                ]["name"],
                date=data_sample["properties"]["Date"]["date"]["start"],
                download_url=data_sample["properties"]["Download URL"]["url"],
            )
        )
    return dye_houses
