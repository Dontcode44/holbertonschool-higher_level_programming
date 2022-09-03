#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa
"""
from hashlib import new
from unicodedata import name
import sqlalchemy
import sys
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    quer = session.query(State).filter(
        State.id == 2).first()
    quer.name = "New Mexico"
    session.commit()
    session.close()
