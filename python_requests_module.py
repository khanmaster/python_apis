# What is an API - Application programing interface
# Why - used to connect to other programs
# In Python we have a module called requests to interact with WEB-APIs

### how can we install a python package in pycharm
``` pip install requests ```

import requests

# check HTTP/HTTPS 200 success - 400 - 404 page not found
response_bcc = requests.get("https://www.bbc.co.uk/")

print(response_bcc.status_code)
print(response_bcc.headers)
print(type(response_bcc.headers))
print(response_bcc.content)

# Iteration 1
# receive a response and check if 200 - print success
# elif code 400 - page not found
# else code 404 - OOPs sorry something went wrong

## 2nd Iteration

### create a function called check_response_code() including all the above
### returns the message with status code

### 3rt Iteration? OOP with 4 pillars.



