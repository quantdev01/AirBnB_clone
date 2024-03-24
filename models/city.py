#!/usr/bin/python3
""" This is the City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class, contains state ID and name """
    state_id = ""
    name = ""
