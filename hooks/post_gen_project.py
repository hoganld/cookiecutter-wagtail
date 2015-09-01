#!/usr/bin/env python
"""
Generates a .env file suitable for development purposes. Not suitable for production.
"""

import random
import string

def generate_secret_key():
    keyspace = "%s%s%s" % (string.ascii_letters, string.digits, string.punctuation)
    return ''.join([random.SystemRandom().choice(keyspace) for i in range(50)])

with open("{{cookiecutter.project_name}}/.env", "w") as f:
    f.write("SECRET_KEY=%s\n" % generate_secret_key())
    f.write("DEBUG=True")

