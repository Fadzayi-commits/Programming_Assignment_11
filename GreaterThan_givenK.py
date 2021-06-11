def string_k(k, str):

    string = []


    text = str.split(" ")


    for x in text:
        if len(x) > k:
         string.append(x)
         return string
k = 3
str = "Data Science for greeks"
print(string_k(k, str))