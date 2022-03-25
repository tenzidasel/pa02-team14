import pytest
from transactions import Transaction

@pytest.fixture
def setup():
    tr = Transaction()
    tr.add((123, 23.5, "deposit", '2022-3-20', "account X to account Y"))
    tr.add((999, 15, "deposit", '2022-3-20', "account A to account B"))
    tr.add((145, 12, "deposit", '2022-3-20', "account J to account K"))
    tr.add((712, 16, "deposit", '2022-3-20', "account Z to account S"))
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


@pytest.mark.delete
def test_delete(setup):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = setup.select_all()

    # then we add this category to the table and get the new list of rows
    cat0 = {'item_no': 125, 
            'amount': 10,
            'category': 'testing category',
            'date': '2022-3-24',
            'description':'Testing description',
            }
    rowid = setup.add(cat0)
    cats1 = setup.select_all()

    # now we delete the category and again get the new list of rows
    setup.delete(rowid)
    cats2 = setup.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1

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



   