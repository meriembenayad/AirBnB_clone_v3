#!/usr/bin/python3
""" Test BaseModel """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db",
    "Test is not relevant for BaseModel"
)
class test_basemodel(unittest.TestCase):
    """ Test BaseModel """

    def __init__(self, *args, **kwargs):
        """ TEst init """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ TEst SetUp """
        pass

    def tearDown(self):
        """ Test tearDown """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ Test Default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test Kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test kwargs_int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """document documt"""
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".
                         format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """ Test to_dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test kwargs """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """document documt"""
        n = {"name": "test"}
        new = self.value(**n)
        self.assertEqual(new.name, n["name"])

    def test_id(self):
        """ Test id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ TEst created_at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test updated_at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        new.save()
        self.assertFalse(new.created_at == new.updated_at)
