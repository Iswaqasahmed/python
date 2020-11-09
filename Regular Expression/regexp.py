import re # imported regular expression module
phoneNumber = re.compile('r(\d{4}-\d{4}-\d{3}')
search  = phoneNumber.search('My Mobile Number is 0311-3678-238')
print("my number is founded ",search)