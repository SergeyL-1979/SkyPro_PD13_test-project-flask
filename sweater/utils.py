#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint
from sweater import app, db
from sweater.models import User, Order, Offer
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))


# ====== ЧТЕНИЯ ДАННЫХ ИЗ JSON И ДОБАВЛЕНИЯ ИХ В БД ========================
with open(os.path.join(basedir, "db_json/users.json"), encoding='utf-8') as file:
    users = json.load(file)

with open(os.path.join(basedir,"db_json/orders.json"), encoding='utf-8') as file:
    orders = json.load(file)

with open(os.path.join(basedir,"db_json/offers.json"), encoding='utf-8') as file:
    offers = json.load(file)

with app.app_context():
    # Пересоздаем базу
    # db.drop_all()
    db.create_all()
    # создаем экземпляры пользователей
    users_1 = [User(**user_data) for user_data in users]
    orders_1 = [Order(**order_data) for order_data in orders]
    offers_1 = [Offer(**offer_data) for offer_data in offers]
    # добавляем в сессию и коммитим
    db.session.add_all(users_1)
    db.session.add_all(orders_1)
    db.session.add_all(offers_1)
    db.session.commit()
    #
    # pprint(db.session.query(User).all())
    # pprint(db.session.query(Order).all())
    # pprint(db.session.query(Offer).all())
# =============== КОНЕЦ ЧТЕНИЯ ДАННЫХ ИЗ ФАЙЛА =============================
