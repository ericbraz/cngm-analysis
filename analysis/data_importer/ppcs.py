from config import PPCS_URL
from .base import BaseDataFetcher

class Ppcs(BaseDataFetcher):

    def __init__(self):
        super().__init__(PPCS_URL, "ppcs.json")
