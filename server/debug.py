#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza
import ipdb

if __name__ == '__main__':
    with app.app_context():
        ipdb.set_trace()