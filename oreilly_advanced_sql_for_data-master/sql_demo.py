#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:21:51 2017

@author: amit
"""

from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///thunderbird_manufacturing.db')
conn = engine.connect()

def get_all_customers():
  stmt = text("select * from customer")
  return list(conn.execute(stmt))

def customer_for_id(customer_id):
  stmt = text("select * from customer where customer_id = :id")
  return conn.execute(stmt, id = customer_id).first()

print(customer_for_id(3))



  
