import pytest
from transactions import Transaction

@pytest.fixture
def setup():
    tr = Transaction()
    tr.add_jf((123, 23.5, "deposit", '2022-3-20', "account X to account Y"))
    tr.add_jf((999, 15, "deposit", '2022-3-20', "account A to account B"))
    tr.add_jf((145, 12, "deposit", '2022-3-20', "account J to account K"))
    tr.add_jf((712, 16, "deposit", '2022-3-20', "account Z to account S"))
    
    

    

def test_date():
    

def test_month():
