def transform(text):
    var = text
    lower = True
    for i in range(len(text)):
        if var[i].isalpha():
            edit = var[i].lower() if lower == True else var[i].upper()
            pre = "" if i == 0 else var[:i]
            post = "" if i == len(text) else var[i+1:]
            var = pre + edit + post
            lower = ~lower
    return var