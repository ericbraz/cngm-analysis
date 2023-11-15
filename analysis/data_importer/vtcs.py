from config import VTCS_URL
from .base import BaseDataFetcher

class Vtcs(BaseDataFetcher):

    className = 'Vtcs'

    def __init__(self) -> None:
        super().__init__(VTCS_URL, "vtcs.json")
