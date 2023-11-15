from config import PPCS_URL
from .base import BaseDataFetcher

class Ppcs(BaseDataFetcher):

    className = 'Ppcs'

    def __init__(self) -> None:
        super().__init__(PPCS_URL, "ppcs.json")
