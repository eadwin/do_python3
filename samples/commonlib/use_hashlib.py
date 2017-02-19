#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

db = {}

def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    return get_md5(password + username + 'the-Salt') == db[username]

register('acker','abc')
register('mim','abc')
print(db)
print(login('acker', 'abc'))
print(login('mim', 'abc'))
