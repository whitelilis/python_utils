#!/usr/bin/env python
import hashlib

def file_md5(path):
    with open(path) as file_to_check:
        data = file_to_check.read()
        md5_returned = hashlib.md5(data).hexdigest()
        return md5_returned
