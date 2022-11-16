# xyxy will contain any rotation of the string - xy is the part of string
# Example  - in erbottlewat x = erbottle y = wat if you do xy then you will get the similar result
# when you will do xyxy then you will get the 'erbottle-wat-erbottle-wat'
# xyxy = xy+xy = string + string

def is_substring(s1, s2):
    return s1.find(s2) > -1


def string_rotation(s1, s2):
    s1 = s1 + s1
    return is_substring(s1, s2)


print(string_rotation("waterbottle", "erbottlewat"))
