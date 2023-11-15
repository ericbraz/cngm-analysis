from .cngm import Cngm
from .ppcs import Ppcs
from .vtcs import Vtcs

cngm = Cngm()
ppcs = Ppcs()
vtcs = Vtcs()

cngm.get_data()
ppcs.get_data()
vtcs.get_data()
