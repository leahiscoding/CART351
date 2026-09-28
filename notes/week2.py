# lists = ["a","b","c","d"]
# for el in lists:
#     #el => element
#     print(f"this is {el}")
    
# # each element in the string has a position in the string so we can iterate over it as if it were a list

# testString = "A wonderful sunshiny day"
# for ch in testString:
#     print (ch)
#     # each string is a valid character, including but not limited to punctuations and spaces

# newItems = []
# newItems.append("first")
# print(newItems [0])
# #0 is the first item in the index

# #append using a for loop:
# for i in range(2,10):
#     #i is between 2 and 9 > up to 10 but not including 10
#     # third argument is the step
#     newItems.append(f"{i} is the next item")

# for el in newItems:
#     print(el)

# #if you want to go to the end of the items — use len()

# #list testLIst.insert (2 > position in array, "new element" > string) insert in 3rd place

# listA = [1,2,3,4]
# listB = [5,6,7,8]
# listA.extend(listB)
# print(listA)

# # += / + > concatenation  

# listQ = ['cats','dogs','parrots']
# print(listQ.index("cats"))


# myStringTest = "another fine day"
# print(myStringTest.index("f"))

# listToSort = ["water","question","apples","wander"]
# listToSort.sort()
# print(f"this is the sorted list {listToSort}")

#sort() > sorts a list in place
#reverse() > reverses list in place
#len() > access the length of a list
#pop() > take out the end by default in array array.pop() > remove 
#if you're using pop() at the end of the list then you remove the end of the list

# list_ex = ["stars", 23, "stripes", "dots", 62]
# if "stars" in list_ex:
#     print("yay")
# if  "star" not in list_ex:
#     print("it's not in the list")

# #join() > often you might have a list of strings 
# #if you want to make them join things together

# element_list= ["a","b","c","d"]
# glue= "*"
# single_str = glue.join(element_list)
# print(single_str)

# #split > if you want to take a string and convert it to a list
# # you have to have a delimitor > what are you splitting on 

# # often you just want a part of the list
# # list slicing is useful for slicing the lists 
# # print (list[1:5] > 2-4) the list remains unchanged

# print(element_list[::])

# aList = [1,2,3,4,5,'a','b','c','d','e'] 
# print(aList[1:5])

# # Get elements starting from index 2 to the end of the list
# bList = aList[2:] #specify start and leave end blank
# print(bList)

# # Get elements until from start until index 5 
# cList = aList[:5] #specify end and leave start blank
# print(cList)

# #negative indexing > getting the last element of the list
# print(aList[-1])

# #Get all items between two positions:

# # Get elements from index 1 to index 6 (excluding index 6)
# dList = aList[1:6]
# print(dList)

# #Get items at specified intervals:

# # Get every second element from the list, starting from the beginning (use the step)
# stepA = aList[::2]
# print(stepA)

# # Get every third element from the list, starting from index 1 to 8(exclusive)
# stepB = aList[1:8:3]
# print(stepB)

# #Negative indexing is useful when you want to access elements using indexes starting from the end of the list. The last element always has an index of -1, the second last element -2, and so on....
# #Negative indexing makes it easy to access items without needing to know the exact length of the list.

# # Get elements starting from index -2 to end of list
# negA = aList[-2:]
# print(negA)

# # Get elements starting from index 0 to index -3 (excluding 3th last index)
# negB = aList[:-3]
# print(negB)

# # Get elements from index -4 to -1 (excluding index -1)
# negC = aList[-4:-1]
# print(negC)

# # Get every 2nd elements from index -8 to -1 (excluding index -1)
# negD= aList[-8:-1:2]
# print(negD)

# #Get from index 1 to last (excluding last)
# negE= aList[1:-1]
# print(negE)

# #You can also use slicing and replace the items at those indexes:

# qList = [1,2,3,4,5,'a','b','c','d','e'] 
# qList[0:2] = 'z'    ## replace [1,2] with single ['z']
# print(qList)

rList = [1,2,3,4,5,'a','b','c','d','e'] 
rList[0:2] = 'a,b'  ## replace [1,2] with ['z','z'] 
# if you want to add something then use insert 
print(rList)

# sList = [1,2,3,4,5,'a','b','c','d','e'] 
# sList[4:-1] = 'nnn'   ## replace
# print(sList)
