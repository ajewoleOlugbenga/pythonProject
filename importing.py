import re

string = "I do not know why 'I AM YELLING' but they told me that i am"
print(string)

new = re.sub('[a-z]','',string)
print(new)