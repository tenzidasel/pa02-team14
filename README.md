# pa02-team14

## About our app

### Running pylint

### Running pytest

### Running tracker.py + features of our app


$ pylint *.py
************* Module pytest
pytest.py:1:0: C0114: Missing module docstring (missing-module-docstring)
*************
<?>:16:4: W0622: Redefining built-in 'exit' (redefined-builtin)
pytest.py:1:0: W0406: Module import itself (import-self)
pytest.py:12:13: W0621: Redefining name 'dbfile' from outer scope (line 6) (redefined-outer-name)
pytest.py:14:4: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
pytest.py:19:13: W0621: Redefining name 'empty_db' from outer scope (line 12) (redefined-outer-name)
pytest.py:21:4: C0103: Variable name "t1" doesn't conform to snake_case naming style (invalid-name)
pytest.py:22:4: C0103: Variable name "t2" doesn't conform to snake_case naming style (invalid-name)
pytest.py:23:4: C0103: Variable name "t3" doesn't conform to snake_case naming style (invalid-name)
pytest.py:24:4: W0612: Unused variable 'id1' (unused-variable)
pytest.py:25:4: W0612: Unused variable 'id2' (unused-variable)
pytest.py:26:4: W0612: Unused variable 'id3' (unused-variable)
pytest.py:31:19: W0621: Redefining name 'small_db' from outer scope (line 19) (redefined-outer-name)
pytest.py:34:4: C0103: Variable name "t0" doesn't conform to snake_case naming style (invalid-name)
pytest.py:44:18: W0621: Redefining name 'small_db' from outer scope (line 19) (redefined-outer-name)
pytest.py:47:4: C0103: Variable name "t0" doesn't conform to snake_case naming style (invalid-name)
pytest.py:2:0: W0611: Unused to_cat_dict_list imported from transactions (unused-import)
*************
<?>:4:4: W0611: Unused import _pytest.mark (unused-import)
*************
<?>:5:4: W0611: Unused import _pytest.recwarn (unused-import)
*************
<?>:6:4: W0611: Unused import _pytest.runner (unused-import)
*************
<?>:7:4: W0611: Unused import _pytest.python (unused-import)
*************
<?>:8:4: W0611: Unused import _pytest.skipping (unused-import)
*************
<?>:9:4: W0611: Unused import _pytest.assertion (unused-import)
*************
<?>:36:4: W0611: Unused import _pytest.freeze_support (unused-import)
*************
<?>:40:8: W0611: Unused import _pytest.genscript (unused-import)
*************
<?>:46:4: W0611: Unused import _pytest.debugging (unused-import)
*************
<?>:50:8: W0611: Unused import _pytest.pdb (unused-import)
*************
<?>:56:4: W0611: Unused import _pytest.fixtures (unused-import)
************* Module test_category
test_category.py:14:13: W0621: Redefining name 'dbfile' from outer scope (line 9) (redefined-outer-name)
test_category.py:16:4: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
test_category.py:21:13: W0621: Redefining name 'empty_db' from outer scope (line 14) (redefined-outer-name)
test_category.py:35:11: W0621: Redefining name 'small_db' from outer scope (line 21) (redefined-outer-name)
test_category.py:40:8: C0103: Variable name "s" doesn't conform to snake_case naming style (invalid-name)
test_category.py:58:4: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
test_category.py:66:13: W0621: Redefining name 'med_db' from outer scope (line 35) (redefined-outer-name)
test_category.py:82:16: W0621: Redefining name 'med_db' from outer scope (line 35) (redefined-outer-name)
test_category.py:102:16: W0621: Redefining name 'med_db' from outer scope (line 35) (redefined-outer-name)
************* Module test_transaction
test_transaction.py:23:16: C0303: Trailing whitespace (trailing-whitespace)
test_transaction.py:48:27: C0303: Trailing whitespace (trailing-whitespace)
test_transaction.py:65:14: C0303: Trailing whitespace (trailing-whitespace)
test_transaction.py:68:14: C0303: Trailing whitespace (trailing-whitespace)
test_transaction.py:114:0: C0305: Trailing newlines (trailing-newlines)
test_transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test_transaction.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:6:4: C0103: Variable name "tr" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:7:4: C0103: Variable name "ds" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:20:13: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:34:28: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)
test_transaction.py:35:29: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)
test_transaction.py:36:29: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)
test_transaction.py:37:25: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)
test_transaction.py:38:32: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)
test_transaction.py:42:16: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:64:14: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:65:4: C0103: Variable name "tr" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:65:4: W0612: Unused variable 'tr' (unused-variable)
test_transaction.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:67:15: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:68:4: C0103: Variable name "tr" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:68:4: W0612: Unused variable 'tr' (unused-variable)
test_transaction.py:71:19: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:74:4: C0103: Variable name "t0" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:80:4: W0612: Unused variable 'cat1' (unused-variable)
test_transaction.py:85:18: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:88:4: C0103: Variable name "t0" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:97:27: C0103: Argument name "ds" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:97:20: W0621: Redefining name 'setup' from outer scope (line 5) (redefined-outer-name)
test_transaction.py:103:11: W0622: Redefining built-in 'tuple' (redefined-builtin)
test_transaction.py:104:12: C0103: Variable name "tr" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:100:4: W0612: Unused variable 'tr1' (unused-variable)
test_transaction.py:104:12: W0612: Unused variable 'tr' (unused-variable)
************* Module tracker
tracker.py:91:1: E0001: invalid syntax (<unknown>, line 91) (syntax-error)
************* Module transactions
transactions.py:16:0: C0301: Line too long (153/100) (line-too-long)
transactions.py:101:0: C0301: Line too long (109/100) (line-too-long)
transactions.py:115:44: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:47:4: E0102: method already defined line 37 (function-redefined)
transactions.py:95:8: C0103: Constant name "item_num" doesn't conform to UPPER_CASE naming style (invalid-name)
transactions.py:95:8: W0601: Global variable 'item_num' undefined at the module level (global-variable-undefined)
transactions.py:118:18: W0622: Redefining built-in 'tuple' (redefined-builtin)
transactions.py:158:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:168:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:1:0: R0801: Similar lines in 2 files
==category:[61:68]
==transactions:[124:131]
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
 (duplicate-code)
transactions.py:1:0: R0801: Similar lines in 2 files
==pytest:[4:13]
==test_category:[7:15]
@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database ''' (duplicate-code)
transactions.py:1:0: R0801: Similar lines in 2 files
==category:[61:66]
==transactions:[102:108]
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
 (duplicate-code)

-----------------------------------
Your code has been rated at 6.44/10
