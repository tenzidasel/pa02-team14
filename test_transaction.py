import pytest
from transactions import Transaction

@pytest.fixture
def setup():
    tr = Transaction('tracker.db')
    ds = [
        (123, 23.5, "deposit", '2022-3-20', "account X to account Y"),
        (999, 15, "deposit", '2022-3-20', "account A to account B"),
        (145, 12, "deposit", '2022-3-20', "account J to account K"),
        (712, 16, "deposit", '2022-3-20', "account Z to account S")
    ]
    tr.add(ds[0])
    tr.add(ds[1])
    tr.add(ds[2])
    tr.add(ds[3])
    yield tr

@pytest.mark.add
def test_add(setup):
    ''' add a category to db, the select it, then delete it'''

    cat0 = (125, 
            10,
            'testing category',
            '2022-3-24',
            'Testing description',
            )
    cats0 = setup.select_all()
    rowid = setup.add(cat0)
    cats1 = setup.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = setup.select_one(rowid)
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

@pytest.mark.year
def test_year_sort(setup):
    ''' add a category to db, the select it, then delete it'''

    t0 = (123, 23.5, "deposit", '2022-3-20', "account X to account Y")
    cats0 = setup.select_all()
    rowid = setup.add(t0)
    print("ROW ID",rowid)
    cats1 = setup.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = setup.select_one(rowid)
    assert cats1[-1]['date'] == cats0[-1]['date']


@pytest.mark.category
def sort_category(setup):
    ''' add a category to db, the select it, then delete it'''

    t0 = {123, 23.5, "deposit", '2022-3-20', "account X to account Y"}
    cats0 = setup.select_all()
    rowid = setup.add(t0)
    cats1 = setup.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = setup.select_one(rowid)
    assert cat1['category'] == cats0['category']

@pytest.mark.select_all
def test_select_all(setup, ds):
    ''' add a category to db, then select it and show all transactions'''

    tr1 = (123, 23.5, "deposit", '2022-3-20', "account X to account Y")
    tr0 = setup.select_all()
    counter = 0
    for i, tuple in ds:
        for tr in tr0:
            if i == tr0['id']:
                assert tr0['item_no']==tuple[0]
                assert tr0['amount']==tuple[1]
                assert tr0['category']==tuple[2]
                assert tr0['date']==tuple[3]
                assert tr0['description']==tuple[4]
                counter = counter + 1

    assert counter == len(ds)

   