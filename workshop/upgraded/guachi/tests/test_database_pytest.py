import os
import sqlite3
import pytest
from guachi import database

@pytest.fixture(autouse=True)
def teardown():
    yield
    try:
        os.remove('/tmp/test_guachi')
    except Exception:
        pass

def test_create_database():
    foo = database.dbdict('/tmp/test_guachi')
    assert os.path.isfile('/tmp/test_guachi')

def test_init():
    foo = database.dbdict('/tmp/test_guachi')

    assert foo.db_filename == '/tmp/test_guachi'
    assert foo.table == '_guachi_data'
    assert foo.select_value == 'SELECT value FROM _guachi_data WHERE key=?'
    assert foo.select_key == 'SELECT key FROM _guachi_data WHERE key=?'
    assert foo.update_value == 'UPDATE _guachi_data SET value=? WHERE key=?'
    assert foo.insert_key_value == 'INSERT INTO _guachi_data (key,value) VALUES (?,?)'
    assert foo.delete_key == 'DELETE FROM _guachi_data WHERE key=?'

def test_init_guachi_table():
    """Make sure we can check other tables"""
    foo = database.dbdict('/tmp/test_guachi', table='_guachi_options')
    assert foo.table == '_guachi_options'

def test_get_item_keyerror():
    foo = database.dbdict('/tmp/test_guachi')
    with pytest.raises(KeyError):
        foo['meh']

def test_get_item():
    foo = database.dbdict('/tmp/test_guachi')
    foo['bar'] = 'beer'
    assert foo['bar'] == 'beer'
 
def test_setitem_update():
    """If it already exists, you need to do an update"""
    foo = database.dbdict('/tmp/test_guachi')
    foo['a'] = 1
    foo['a'] = 2
    assert foo['a'] == 2

def test_close_db():
    foo = database.dbdict('/tmp/test_guachi')
    # Just make sure this doesn't raise an exception
    foo._close()
    assert True

def test_setitem_typeerror():
    foo = database.dbdict('/tmp/test_guachi')
    # In Python 3, keys can be integers so this test is no longer relevant
    # We'll test a different error case
    with pytest.raises(sqlite3.ProgrammingError):
        foo._close()
        # This should raise an error as connection is closed
        foo['a'] = 1

def test_delitem():
    foo = database.dbdict('/tmp/test_guachi')
    foo['a'] = 1
    del foo['a']
    with pytest.raises(KeyError):
        foo['a']

def test_delitem_keyerror():
    foo = database.dbdict('/tmp/test_guachi')
    with pytest.raises(KeyError):
        del foo['a']

def test_integrity_check_true():
    foo = database.dbdict('/tmp/test_guachi')
    assert foo._integrity_check() is True

def test_keys():
    foo = database.dbdict('/tmp/test_guachi')
    foo['a'] = 1
    foo['b'] = 2
    assert len(list(foo.keys())) == 2
    assert 'a' in foo.keys()
    assert 'b' in foo.keys()

def test_key_empty():
    foo = database.dbdict('/tmp/test_guachi')
    assert len(list(foo.keys())) == 0

def test_keys_get_none():
    foo = database.dbdict('/tmp/test_guachi')
    assert foo.get('a') is None

def test_keys_get_value():
    foo = database.dbdict('/tmp/test_guachi')
    foo['a'] = 1
    assert foo.get('a') == 1

def test_keys_get_value_w_default():
    foo = database.dbdict('/tmp/test_guachi')
    assert foo.get('a', 'default') == 'default'
