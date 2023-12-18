from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class DyeHouse(BaseModel):
    sample_type: Literal["Sample", "Blank"]
    client: str
    client_location: str
    fermentor_used: str
    fermentor_model: str
    date: datetime
    download_url: str
