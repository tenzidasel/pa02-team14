import pytest
from transactions import Transaction, to_cat_dict_list


@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')


@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    t1 = {123, 23.5, "deposit", '2022-3-20', "account X to account Y"}
    t2 = {999, 7, "deposit", '1990-4-19', "account X to account Y"}
    t3 = {109, 9, "deposit", '1800-3-20', "account X to account Y"}
    id1 = empty_db.add(t1)
    id2 = empty_db.add(t2)
    id3 = empty_db.add(t3)
    yield empty_db


@pytest.mark.add
def test_year_sort(small_db):
    ''' add a category to db, the select it, then delete it'''

    t0 = {123, 23.5, "deposit", '2022-3-20', "account X to account Y"}
    cats0 = small_db.select_all()
    rowid = small_db.add(t0)
    cats1 = small_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = small_db.select_one(rowid)
    assert cat1['date'] == cats0['date']


@pytest.mark.add
def sort_category(small_db):
    ''' add a category to db, the select it, then delete it'''

    t0 = {123, 23.5, "deposit", '2022-3-20', "account X to account Y"}
    cats0 = small_db.select_all()
    rowid = small_db.add(t0)
    cats1 = small_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = small_db.select_one(rowid)
    assert cat1['category'] == cats0['category']
