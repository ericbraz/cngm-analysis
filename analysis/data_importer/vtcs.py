from config import VTCS_URL
from .base import BaseDataFetcher

class Vtcs(BaseDataFetcher):

    def __init__(self):
        super().__init__(VTCS_URL, "vtcs.json")
