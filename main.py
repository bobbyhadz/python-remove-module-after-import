# Remove an imported module in Python 

import sys
import requests

# 👇️ <function get at 0x7f8c7d30e4d0>
print(requests.get)

# ✅ remove an imported module
del sys.modules['requests']
del requests

# ⛔️ NameError: name 'X' is not defined
print(requests.get)
