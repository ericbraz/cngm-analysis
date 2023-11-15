from config import PPCS_URL

class Ppcs:

    def __init__(self):
        super().__init__(PPCS_URL, "ppcs.json")
