# class_professors = {'Cart_253_A':'Pippin Bar',
#                     'Cart_211':'Brad Todd',
#                     'Cart_214':'Joanna Berzowska', 
#                     'Cart_215':'Jonathan Lessard'}

# print(type(class_professors))

# #you can have complex data structure value

# #there could be nesting going on

# specialList = {17: [1.6, 2.45], 42: [11.6, 19.4], 101: [0.123, 4.89], 102: 1.05}

# #to access the data type

# print(type(specialList))

# #question how to get the list out of dict if it's nested?

# #how to access the first element of the list?

# # print(specialList[17])
# # # 17 is the key

# # print(type(specialList[102]))

# # how to access pippin bar?

# print(class_professors['Cart_253_A'])

# # you need to know your keys—otherwise, the program is going to fail

# # what are the keys of the speicial list?

# print(type(specialList.keys()))

# # it's important to always know that what kind of value is it and how can I use it to my benefit

# # going through each key
# for key in specialList.keys():
#     print(specialList[key])
# ### question how to print the first key if I wanna know the first key?

# #going through values
# print(specialList.values())
# for value in specialList.values():
#     print(value)


# #going through items (prints each topple)
# print(specialList.items())
# for item in specialList.items():
#  print(item)
#  print(item[0])

# # you're iterating over the keys
# for item in specialList:
#    print (item)
#    print(specialList[item])


# for item in class_professors:
#     print(item)


  
# for item in class_professors:
#     print(class_professors[item])



shopping = {
            "vegetables": {"green":[{"spinach":["green"]},"broccoli","lettuce"],"orange":["carrots"]},
            "fruit": ['canteloupe', 'banananas'],
             "bakery": ['bagels', 'rye bread'], }

print(shopping["vegetables"]["green"][0]["spinach"])

shopping_rev = ["cleaning_items"] = ["dish-soap", "sponges"]
shopping_rev["cleaning_items"].append("bleach")


# The order of keys

# Python stores the key/value pairs in a dictionary in the order you added them to the dictionary 
# **in most cases** -: this was not the case in all versions of python and may not be in the future... 
# therefore do not rely on the fact that right now Python preserves insertion order in dictionaries.
# Dictionary keys are unique

# Another important fact about dictionaries is that you can't put the same key into one dictionary twice. If you try to write out a dictionary that has the same key used more than once, 
# Python will silently ignore all but one of the key/value pairs. 
# For example:

{'a': 1, 'a': 2, 'a': 3}
#{'a':3} is the result

# Similarly, if you attempt to set the value for a key that already exists in the dictionary (using =), you won't actually add a second key/value pair for that key. Rather, you'll just overwrite the existing value:

test_dict = {'a': 1, 'b': 2}
#test_dict['a'] is 1

test_dict['a'] = 100
test_dict['a']
#test_dict['a'] is 100