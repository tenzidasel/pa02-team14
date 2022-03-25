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
   

def test_date(setup):
    tr = setup    

def test_month(setup):
    tr = setup 



@pytest.mark.select_all
def test_select_all(tr):
    ''' add a category to db, then select it and show all transactions'''

    tr0 = {'item_no':'1',
            'amount':23.5,
            'category': 'deposit',
            'date':'2022-3-24',
            'description':'account A to account B'
    tr0 = tr.select_all()
    rowid = tr.add(tr0)
    trs1 = tr.select_all()
    assert len(tr1) == len(tr0) + 1
    tr1 = tr.select_one(rowid)
    assert tr1['item_no']==tr0['item_no']
    assert tr1['amount']==tr0['amount']
    assert tr1['category']==tr0['category']
    assert tr1['date']==tr0['date']
    assert tr1['description']==tr0['dascription']



   