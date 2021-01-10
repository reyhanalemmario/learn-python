import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_great):
    greeting = 'Hello, {}'.format(who_to_great)
    return greeting


r = requests.get('https://coreyms.com')
print(r.status_code)
print(r.ok)
