import pytest, os, sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# package modules
from AtomicHubMonitor.MarketSalesRequest import MarketSalesRequest

# Alt 1 - from [folder] import [python script]
# Alt 2 -from [folder.script] import [Class]

class Test_NAME(unittest.TestCase): 

    def test_NAME(self): 
        # ARRANGE

        # ACT

        # ASSERT
        pass
