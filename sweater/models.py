#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sweater import db



# ====================== МОДЕЛИ БАЗЫ ДАННЫХ ================================
class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }

    def __repr__(self):
        return f"User: {self.first_name}, {self.last_name}, " \
               f"{self.age}, {self.email}, {self.role}, {self.phone}"


class Order(db.Model):
    __tablename__ = "order"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)
    address = db.Column(db.String(255))
    price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
        }

    def __repr__(self):
        return f"Order: {self.name}, {self.description}, {self.start_date}, {self.end_date}, {self.address}, {self.price}, {self.customer_id}, {self.executor_id}"


class Offer(db.Model):
    __tablename__ = "offer"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }

    def __repr__(self):
        return f"Offer: {self.id}, {self.order_id}, {self.executor_id}"

# ================ КОНЕЦ СОЗДАНИЯ МОДЕЛЕЙ БД ==============================
