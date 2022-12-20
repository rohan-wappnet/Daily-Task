# Date : 16/12/2022

# Set-1

# ------------------------------------------

# Question1:
# lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = [8, 9, 10]
# lst1.append(7)  # Add element in the list
# lst1.extend(lst2)  # Join another list in the end if list 1
# lst1.insert(10, 11)  # Insert element at the given index
# lst1.remove(1)  # Removes the given value from the list
# lst1.pop(7)  # Removes the given index value

# ------------------------------------------

# Question2:
# lst1.index(2)  # Returns the index of the given value
# lst1.count(2)  # Returns the number of occurance
# lst1.sort()  # Sort the list, by default asc order
# lst1.reverse()  # Reverse the list
# lst2 = lst1.copy()  # Copy entire list to another variable/list
# lst1.clear()  # Removes all elements from the list

# ------------------------------------------

# Question3:
# lst1 = [1, 2, 3, 4, 5, 6]
# print(lst1[2:4]) #[start:stop:jump]

# ------------------------------------------

# Question4:
# num = []
# for i in range(1, 31):
#     num.append(i)
# sq = list(map(lambda x: x * x, num))  # Creates a list of all number squares
# tmp = len(num) - 5
# result = (sq[0:5]) + (sq[tmp:len(sq)])  # Adding first and last 5 values
# print(result)

# ------------------------------------------

# Question5:
# var_tupple = (1, 2, 3, 4, 5) #Tupples are immutable
# var_tupple.count(2) #Returns number of counts
# var_tupple.index(2) #Returns the index of the element

# ------------------------------------------

# Question6:
# var_tupple = (1, 2, 3, 4, 5) #Tupples are immutable
# print(var_tupple[::-1]) #[start:stop:jump]

# ------------------------------------------

# Question7:
# from functools import reduce


# def sum_all(lst):
#     """Function to sum all elements of list"""
#     sum = reduce(lambda x, y: x+y, lst)
#     return sum


# def multply_all(lst):
#     """Function to multiply all elements of list"""
#     mul = reduce(lambda x, y: x*y, lst)
#     return mul


# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(sum_all(list1))
# print(multply_all(list1))

# ------------------------------------------

# Question8:
# def get_largest_value(lst):
#     """Returns largest value from the list"""
#     return max(lst)


# def get_smallest_value(lst):
#     """Returns largest value from the list"""
#     return min(lst)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(get_largest_value(list1))
# print(get_smallest_value(list1))

# ------------------------------------------

# Question9:
# def sub_lists(lst):
#     """function to generate all the sub lists"""
#     lists = [[]]
#     for i in range(len(lst) + 1):
#         for j in range(i):
#             lists.append(lst[j: i])
#     return lists


# list1 = [1, 2, 3]
# print(sub_lists(list1))

# ------------------------------------------

# Set-2

# ------------------------------------------

# Question1:
# from functools import reduce


# def sum_all(lst):
#     """Function to sum all elements of list"""
#     sum = reduce(lambda x, y: x+y, lst)
#     return sum


# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(sum_all(list1))

# ------------------------------------------

# Question2:
# from functools import reduce


# def multply_all(lst):
#     """Function to multiply all elements of list"""
#     mul = reduce(lambda x, y: x*y, lst)
#     return mul


# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(multply_all(list1))

# ------------------------------------------

# Question3 and Question 4:
# def get_largest_value(lst):
#     """Returns largest value from the list"""
#     return max(lst)


# def get_smallest_value(lst):
#     """Returns largest value from the list"""
#     return min(lst)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(get_largest_value(list1))
# print(get_smallest_value(list1))

# ------------------------------------------

# Question5:
# def custom_func(lst):
#     """count the number of strings where the string length is 2 or more and the first and last character are same"""
#     counter = 0
#     for i in lst:
#         if len(i) < 2:
#             continue
#         else:
#             if i[0] == i[len(i) - 1]:
#                 counter += 1
#     return counter


# list1 = ['abc', 'xyz', 'aba', '1221']
# print(custom_func(list1))

# ------------------------------------------

# Question6:
# def output(tup):
#     """function to sort list by last element of tuple"""
#     return sorted(tup, key=lambda x: x[-1])

# tuple1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(output(tuple1))

# Question7:
# def remove_duplicates(lst):
#     """Remove Duplicates from a list"""
#     return list(set(lst))


# list1 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]
# print(remove_duplicates(list1))

# ------------------------------------------

# Question8:
# def isempty(lst):
#     """Checks weather list is empty or not"""
#     if len(lst) <= 0:
#         return "List is Empty"
#     else:
#         return "List is not Empty"


# list1 = []
# print(isempty(list1))

# ------------------------------------------

# Question9:
# lst = [1, 2, 3, 4, 5]
# lst2 = lst.copy() #Copies the given list to new variable
# print(lst2)

# ------------------------------------------

# Question10:
# def custom_func(strr, num):
#     """Returns list of element whose len is greater than given num_check"""
#     lst = strr.split(" ")
#     ans = []
#     for i in lst:
#         if len(i) > num - 1:
#             ans.append(i)
#     return ans

# strr = "My name is Rohan"
# num_check = 3
# print(custom_func(strr, num_check))

# ------------------------------------------

# Question11:
# def check_list(lst1, lst2):
#     """returns True if they have at least one common member"""
#     for i in lst1:
#         if i in lst2:
#             return True
#     return False


# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# print(check_list(list1, list2))

# ------------------------------------------

# Question12:
# def remove_element(lst):
#     if len(lst) < 5:
#         return "Enter list with atleast 5 elements"
#     else:
#         lst.pop(0)  # Removes the given index
#         lst.pop(4 - 1)  # tmp variable will be minus from index
#         lst.pop(5 - 2)  # tmp variable increment after each pop
#         return lst


# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(remove_element(list1))

# ------------------------------------------

# Question13:
# Python program to generate a 3*4*6 3D array whose each element is *
# pass

# ------------------------------------------

# Question14:
# def remove_even(lst):
#     """Removes Even number from list"""
#     for i in lst:
#         if i % 2 == 0:
#             lst.remove(i)
#     return lst


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(remove_even(list1))

# ------------------------------------------

# Question15:
# import random

# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)

# print(mylist)

# ------------------------------------------

# Question16:
# num = []
# for i in range(1, 31):
#     num.append(i)
# sq = list(map(lambda x: x * x, num))  # Creates a list of all number squares
# tmp = len(num) - 5
# result = (sq[0:5]) + (sq[tmp:len(sq)])  # Adding first and last 5 values
# print(result)

# ------------------------------------------

# Question17:
# num = []
# for i in range(1, 31):
#     num.append(i)
# sq = list(map(lambda x: x * x, num))  # Creates a list of all number squares
# print(sq[5:]) #Prints sq except first 5 elements

# ------------------------------------------

# Quesion18:
# Python program to generate all permutations of a list in Python
# Pass

# ------------------------------------------

# Question19:
# from functools import reduce


# def sum_all(lst):
#     """Function to sum all elements of list"""
#     sum = reduce(lambda x, y: x+y, lst)
#     return sum


# lst1 = [1, 2, 3, 4, 5]
# lst2 = [5, 6, 7, 8, 9]
# lst1_sum = sum_all(lst1)
# lst2_sum = sum_all(lst2)

# print(f"Len diff of list = {len(lst1) - len(lst2)}")
# print(f"Value diff of list = {lst1_sum - lst2_sum}")

# ------------------------------------------

# Question20:
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(f"List = {lst}")
# indexx = input("Enter index you want to access : ")
# if indexx.isnumeric:
#     try:
#         indexx = int(indexx)
#         print(lst[indexx])
#     except Exception as e:
#         print("Index out of bounds")
# else:
#     print("Please Enter Numeric Value")

# ------------------------------------------

# Question21:
# def charToString(lst):
#     """Converts char to one string"""
#     strr = ""
#     for i in lst:
#         strr += i
#     return strr


# list1 = ['R', 'o', 'h', 'a', 'n']
# print(charToString(list1))

# ------------------------------------------

# Question22:
# def findIndex(lst, elementt):
#     """Returns index of the given element"""
#     if elementt in lst:
#         return lst.index(elementt)


# lst = ['1', '2', '3', '4', '5', '6', '7', '8']
# elementt = '2'
# print(findIndex(lst, elementt))

# ------------------------------------------

# Question23:
# def flatten_list(lst):
#     """flatten a shallow list"""
#     new_list = []
#     for i in lst:
#         new_list.extend(i)
#     return new_list


# shallow_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(flatten_list(shallow_list))

# ------------------------------------------

# Question24:
# lst1 = [3, 4, 5]
# lst2 = [1, 2]
# lst2.extend(lst1)
# print(lst2)

# ------------------------------------------

# Question25:
# import random

# lst = [1, 2, 3, 4, 5, 6]
# print(random.choice(lst))

# ------------------------------------------

# Question 26:
# python program to check whether two lists are circularly identical
# Pass

# ------------------------------------------

# Question 27:
# def findSmallest(lst):
#     """Find the smallest value from the list"""
#     return min(lst)


# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(findSmallest(list1))

# ------------------------------------------

# Question28:
# def secondLargest(lst):
#     """This function returns the second largest value"""
#     lst.sort()
#     lst.reverse()
#     return lst[1]


# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(secondLargest(list1))

# ------------------------------------------

# Question29:
# def uniqueValue(lst):
#     """This function returns unique value from the list"""
#     return list(set(lst))

# list1 = [11,22,11,11,22,22,33,33,44,44,44,44,33,22]
# print(uniqueValue(list1))

# ------------------------------------------

# Question30:
# def getCount(lst, element):
#     """This returns the frequency of the elements in a list"""
#     return lst.count(element)


# list1 = [1, 1, 1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 1]
# element = 2
# print(getCount(list1, element))

# ------------------------------------------

# Question31:
# def countInRange(lst, start, end, element):
#     """program to count the number of elements in a list within a specified range"""
#     counter = 0
#     for i in range(start, end + 1):
#         if lst[i] == element:
#             counter += 1
#     return counter


# list1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 3, 2, 2, 1, 1, 1]
# element = 1
# print(countInRange(list1, 1, 15, element))

# ------------------------------------------

# Question32:
# test_list = [5, 6, 3, 8, 2, 1, 7, 1]
# sublist = [8, 2, 7]

# Check for Sublist in List
# c=0
# res=False
# for i in sublist:
# 	if i in test_list:
# 		c+=1
# if(c==len(sublist)):
# 	res=True

# print("Is sublist present in list ? : " + str(res))

# ------------------------------------------

# Question33:
# def sub_lists(lst):
#     lists = [[]]
#     for i in range(len(lst) + 1):
#         for j in range(i):
#             lists.append(lst[j: i])
#     return lists


# list1 = [1, 2, 3]
# print(sub_lists(list1))

# ------------------------------------------

# Question34:
# Python program using Sieve of Eratosthenes method for computing primes upto a specified number
# Pass

# ------------------------------------------

# Question35:
# def customFunc(lst, n):
#     """list by concatenating a given list which range goes from 1 to n"""
#     tmp1 = []
#     for j in range(n):
#         for i in lst:
#             tmp1.append(str(i) + str(j + 1))
#     return tmp1


# list1 = ['p', 'q']
# n = 5
# print(customFunc(list1, n))

# ------------------------------------------

# Question36:
# def getId(var):
#     return str(id(var))


# var1 = "This is string variable"
# print(getId(var1))

# ------------------------------------------

# Question37:
# def findCommon(lst1, lst2):
#     """This function finds common elements from both list"""
#     tmp = []
#     for i in lst1:
#         if i in lst2:
#             tmp.append(i)
#     return tmp


# list1 = [1, 2, 3, 4]
# list2 = [7, 6, 5, 4]
# print(findCommon(list1, list2))

# ------------------------------------------

# Question38:
# def changePos(lst):
#     """change the position of every n-th value with the (n+1)th in a list"""
#     for i in range(0, len(lst), 2):
#         lst[i], lst[i+1] = lst[i+1], lst[i]
#     return lst


# list1 = [0, 1, 2, 3, 4, 5, 6, 8]
# print(changePos(list1))

# ------------------------------------------

# Question39:
# def convToStr(lst):
#     """convert a list of multiple integers into a single integer"""
#     tmp = ""
#     for i in lst:
#         tmp += str(i)
#     return int(tmp)


# list1 = [11, 33, 50]
# print(convToStr(list1))

# ------------------------------------------

# Question40:

# from itertools import groupby
# from operator import itemgetter

# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#     print(letter)
#     for word in words:
#         print(word)

# ------------------------------------------