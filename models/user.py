#!/usr/bin/python3
""" module that defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines a user by numerous attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
