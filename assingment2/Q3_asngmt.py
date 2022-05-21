import re

str1 = "welcome@@#$%&^"
str2 = "welcome to python programming"

regex=re.compile('[@!#$%^&]')
if(regex.search(str1)==None):
    print("no special characters present in a string")
else:
    print("string contain special characters")

    

