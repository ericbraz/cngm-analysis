from config import CNGM_URL
from .base import BaseDataFetcher

class Cngm(BaseDataFetcher):

    className = 'Cngm'

    def __init__(self) -> None:
        super().__init__(CNGM_URL, "cngm.json")
