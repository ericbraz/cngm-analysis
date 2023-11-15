from config import CNGM_URL

class Cngm:

    def __init__(self):
        super().__init__(CNGM_URL, "cngm.json")
