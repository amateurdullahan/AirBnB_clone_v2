#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
import MySQLdb


class test_dbStorage(unittest.TestCase):
    """ Class to test the database storage method """

    def test_new(self):
        """ New object is correctly added to database """
        db = MySQLdb.connect(host="localhost", user="hbnb_test",
                             passwd="hbnb_test_pwd", db="hbnb_test_db")
        cur = db.cursor()
        cur.execute("""SELECT COUNT(*) FROM states""")
        count1 = cur.fetchall()
        new = State()
        new.save()
        cur.execute("""SELECT COUNT(*) FROM states""")
        count2 = cur.fetchall()
        self.assertEqual(count1 + 1, count2)
        cur.close()
        db.close()

    def test_all(self):
        """ __objects is properly returned """
        # tests that storage.all() returns dictionary of objects
        new = BaseModel()
        new.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
        dict_key = "{}.{}".format("BaseModel", new.id)
        self.assertIn(dict_key, temp)

        # tests storage.all() with cls argument, with no cls instances
        all_states = storage.all(State)
        db = MySQLdb.connect(host="localhost", user="hbnb_test",
                             passwd="hbnb_test_pd", db="hbnb_test_db")
        cur = db.cursor()
        cur.execute("""SELECT COUNT(*) FROM states""")
        count = cur.fetchall()
        self.assertEqual(len(all_states.keys()), count)
        # creates cls instance and retests storage.all() with cls
        new_state = State()
        new_state.name = "California"
        new_state.save()
        all_states = storage.all(State)
        self.assertEqual(len(all_states.keys()), count + 1)
        for k, v in all_states.items():
            self.assertEqual("California", v.name)
        cur.execute("""SELECT COUNT(*) FROM states""")
        count2 = cur.fetchall()
        self.assertEqual(count + 1, count2)
        # tests delete method
        storage.delete(new_state)
        all_states = storage.all(State)
        self.assertEqual(len(all_states.keys()), count)
        cur.close()
        db.close()

    def test_empty(self):
        """ Data is saved to database """
        new = State()
        new.name = "California"
        new.save()
        C_id = new.id
        db = MySQLdb.connect(host="localhost", user="hbnb_test",
                             passwd="hbnb_test_pd", db="hbnb_test_db")
        cur = db.cursor()
        cur.execute("""SELECT COUNT(*) FROM states""")
        count = cur.fetchall()
        self.assertNotEqual(count, 0)
        cur.close()
        db.close()

    def test_reload(self):
        """ Storage database is successfully loaded to __objects """
        new = State()
        new.name="testing"
        new.save()
        storage.reload()
        self.assertIn("testing", storage.all(State).values())

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        new.save()
        _id = new.id
        for key in storage.all().keys():
            temp = key
            if _id in key:
                self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ DBStorage object storage created """
        from models.engine.db_storage import DBStorage
        print(type(storage))
        self.assertEqual(type(storage), DBStorage)

