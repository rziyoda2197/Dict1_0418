#1
def get_length(d):
    if len(d) == 0:
        return "Lug‘at bo‘sh"
    return len(d)

data = {'a': 1, 'b': 2, 'c': 3}
print(get_length(data)) 

#2
def add_item(d, key, value):
    if key in d:
        return "Kalit mavjud"
    
    d[key] = value
    return d

#3
def sum_values(d):
    return sum(d.values())

def average_values(d):
    return sum(d.values()) / len(d)

scores = {'math': 85, 'science': 90, 'history': 78}

print(sum_values(scores))
print(average_values(scores))

#4
def check_key(d, key):
    return key in d

def get_value(d, key):
    if key in d:
        return d[key]
    return "Kalit topilmadi"
