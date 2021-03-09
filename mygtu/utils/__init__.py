import os
from .profile import __logo__, __info__, __version__
from .constants import PATH
from .time import time
from .year_list import ylist

if not os.path.exists(PATH):
    os.mkdir(PATH)
    
