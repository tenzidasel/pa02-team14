import pytest
from transactions import Transaction

@pytest.fixture
def setup():
    tr = Transaction()
    tr.add_jf((123, 23.5, "deposit", '2022-3-20', "account X to account Y"))
    tr.add_jf((999, 15, "deposit", '2022-3-20', "account A to account B"))
    tr.add_jf((145, 12, "deposit", '2022-3-20', "account J to account K"))
    tr.add_jf((712, 16, "deposit", '2022-3-20', "account Z to account S"))
    yield tr

@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {'item_no': 125, 
            'amount': 10,
            'category': 'testing category',
            'date': '2022-3-24',
            'description':'Testing description',
            }
    cats0 = med_db.select_all()
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = med_db.select_one(rowid)
    assert cat1['item_no']==cat0['item_no']
    assert cat1['amount'] == cat0['amount']
    assert cat1['category']==cat0['category']
    assert cat1['date']==cat0['date']
    assert cat1['description']==cat0['description']
    
def test_date(setup):
    tr = setup    

def test_month(setup):
    tr = setup 