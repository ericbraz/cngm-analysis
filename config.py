import os
from dotenv import load_dotenv

DATA_SUBFOLDER = 'analysis/data_importer/data'

# find env variables
load_dotenv()

### Defining proxies ###
PROXY_ONE = os.getenv('PROXY_ONE')
PROXY_TWO = os.getenv('PROXY_TWO')
PROXY_THR = os.getenv('PROXY_THR')
PROXY_FOU = os.getenv('PROXY_FOU')
PROXY_FIV = os.getenv('PROXY_FIV')
PROXIES = [
    {
        'http': PROXY_ONE,
        'https': PROXY_ONE,
    },
    {
        'http': PROXY_TWO,
        'https': PROXY_TWO,
    },
    {
        'http': PROXY_THR,
        'https': PROXY_THR,
    },
    {
        'http': PROXY_FOU,
        'https': PROXY_FOU,
    },
    {
        'http': PROXY_FIV,
        'https': PROXY_FIV,
    },
]

### Loading Env Variables ###

# get URL env variable
SOURCE_URL = os.getenv('SOURCE_URL')

# CNGM endpoint
CNGM_END = os.getenv('CNGM_END')
CNGM_URL = SOURCE_URL + CNGM_END

#
VTCS_END = os.getenv('VTCS_END')
VTCS_URL = SOURCE_URL + VTCS_END

#
PPCS_END = os.getenv('PPCS_END')
PPCS_URL = SOURCE_URL + PPCS_END
