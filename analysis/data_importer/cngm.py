from config import CNGM_URL
from .base import BaseDataFetcher

class Cngm(BaseDataFetcher):

    def __init__(self):
        super().__init__(CNGM_URL, "cngm.json")
