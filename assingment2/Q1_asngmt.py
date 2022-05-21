def capitalize(s):
     s, result = s.title(), ""
     for word in s.split():
           result += word[:-1] + word[-1].upper() + " "
     return result[:-1]
print(capitalize("we are learning python"))


