# Date : 19/12/2022

# ------------------------------------------

# Question1:
# def findLen(string):
#     """Returns the lenght of the given string"""
#     return len(string)


# strrr = "This is a demo string"
# print(f"The Lenght of the string is : {findLen(strrr)}")

# ------------------------------------------

# Question2:
# def findFrequency(string):
#     """Returns number of counter of each char in dict"""
#     count = {}
#     for i in string:
#         if i not in count.keys():
#             count[i] = 0

#     for i in string:
#         count[i] += 1

#     return count


# strr = "www.google.com"
# print(findFrequency(strr))

# ------------------------------------------

# Question3:
# def f2l2(string):
#     """Returns first 2 and last 2 char if condition true"""
#     if len(string) < 2:
#         return ""
#     else:
#         return str(string[:2]) + str(string[len(string) - 2:])


# strr = "rohan"
# print(f2l2(strr))

# ------------------------------------------

# Question4:
# def changeStr(string):
#     """string all occurrences of its first char have been changed to '$'"""
#     tmp = list(string.strip(""))
#     for i in range(1, len(string)):
#         if tmp[i] == string[0]:
#             tmp[i] = "$"

#     string1 = ""

#     for i in tmp:
#         string1 += i
#     del tmp
#     return string1


# strr = "rohanr"
# print(changeStr(strr))

# ------------------------------------------
#
# Question5:
# def swapChar(string1, string2):
#     """swap the first two characters of each string"""
#     tmp1 = list(string1.strip(""))
#     tmp2 = list(string2.strip(""))

#     for i in range(0, 2):
#         tmp1[i], tmp2[i] = tmp2[i], tmp1[i]

#     tstr1 = ""
#     tstr2 = ""

#     for i in tmp1:
#         tstr1 += i

#     for i in tmp2:
#         tstr2 += i

#     del tmp1, tmp2
#     return f"{tstr1} {tstr2}"


# str1 = "abc"
# str2 = "xyz"
# print(swapChar(str1, str2))

# ------------------------------------------
#
# Question6:
# def strModify(string):
#     """add 'ing' at the end of a given string. if string already ends with 'ing' then add 'ly'"""
#     if string[(len(string) - 3):] == "ing":
#         string += "ly"
#     else:
#         string += "ing"
#     return string


# strr = "abc"
# print(strModify(strr))

# ------------------------------------------

# Question7:
# def not_poor(str1):
#     snot = str1.find('not')
#     spoor = str1.find('poor')

#     if spoor > snot and snot > 0 and spoor > 0:
#         str1 = str1.replace(str1[snot:(spoor+4)], 'good')
#         return str1
#     else:
#         return str1


# strr = "The lyrics is not that poor!"
# print(not_poor(strr))

# ------------------------------------------

# Question8:
# def findLongest(lst):
#     tmp = []
#     for n in lst:
#         tmp.append([len(n), n])
#     tmp.sort()
#     ans = f"{tmp[-1][0]} {tmp[-1][1]}"
#     return ans


# lst1 = ["My", "Name", "is", "Rohan", "Experience"]
# print(findLongest(lst1))

# ------------------------------------------

# Question9:
# def removeNthChar(string, index):
#     """remove the nth index character from a nonempty string"""
#     if len(string) <= 0:
#         return "String is empty"
#     else:
#         tmp = list(string.strip(""))
#         tmp.pop(index)
#         string = ""

#         for i in tmp:
#             string += i

#         del tmp
#         return string


# strr = "rWappnetSystems"
# index = 0
# print(removeNthChar(strr, index))

# ------------------------------------------

# Question10:
# def charExchange(string):
#     """returns new string where the first and last chars have been exchanged"""
#     tmp = list(string.strip(""))
#     tmp[0], tmp[-1] = tmp[-1], tmp[0]

#     string = ""
#     for i in tmp:
#         string += i

#     del tmp
#     return string


# strr = "nohaR"
# print(charExchange(strr))

# ------------------------------------------

# Question11:
# def removeOdd(string):
#     """remove the characters which have odd index values of a given string"""
#     tmp = list(string.strip(""))
#     counter = 0
#     for i in range(0, len(string), 2):
#         tmp.pop((i - counter))
#         counter += 1

#     tstr = ""

#     for i in tmp:
#         tstr += i

#     del tmp
#     return tstr


# strr = "MyNameIsRohan"
# print(removeOdd(strr))

# ------------------------------------------

# Question12:
# def findFrequency(string):
#     """Returns number of counter of each char in dict"""
#     count = {}
#     for i in string:
#         if i not in count.keys():
#             count[i] = 0

#     for i in string:
#         count[i] += 1

#     return count


# strr = "My name is Rohan"
# print(findFrequency(strr))

# ------------------------------------------

# Question13:
# def convertString(string):
#     """takes input from the user and displays that input back in upper and lower cases"""
#     print(string.upper())
#     print(string.lower())


# txt = input("Enter any String to Convert : ")
# convertString(txt)

# ------------------------------------------

# Question14:
# items = "red, white, black, red, green, black" #input("Input comma separated sequence of words")
# words = [word for word in items.split(",")]
# print(",".join(sorted(list(set(words)))))

# ------------------------------------------

# Question15:
# def addTags(tag, string):
#     """function to create the HTML string with tags around the word(s)"""
#     return f"<{tag}>{string}</{tag}>"


# tag = "b"
# strr = "Python Tutorial"
# print(addTags(tag, strr))

# ------------------------------------------

# Question16:
# def insStrMid(tags, string):
#     """function to insert a string in the middle of a string"""
#     tmp = list(tags.strip(""))

#     tmp.insert(int(len(tmp) / 2), string)
#     tstr = ""

#     for i in tmp:
#         tstr += i

#     del tmp
#     return tstr


# strr = "Python"
# tags = "[[]]"
# print(insStrMid(tags, strr))

# ------------------------------------------

# Question17:
# def lastTwoChar(string):
#     """function to get a string made of 4 copies of the last two characters"""

#     return string[len(string) - 2:] * 4


# strr = "Exercises"
# print(lastTwoChar(strr))

# ------------------------------------------

# Question18:
# def first3Char(string):
#     """function to get a string made of its first three characters"""
#     return string[0:3]


# strr = "ipyz"
# print(first3Char(strr))

# ------------------------------------------

# Question19:
# def seprateString(sep, string):
#     """get the last part of a string before a specified character"""
#     tmp = string.find(sep)
#     if tmp == -1:
#         return "Not Valid Seprator"
#     else:
#         return string[0:tmp]


# sep = "-"
# strr = "https://www.w3resource.com/python-exercises"
# print(seprateString(sep, strr))

# ------------------------------------------

# Question20:
# def customReverse(string):
#     """function to reverses a string if it's length is a multiple of 4"""
#     if len(string) % 4 == 0:
#         return string[::-1]
#     else:
#         return string


# strr = "MyNamIsRohan"
# print(customReverse(strr))

# ------------------------------------------

# Question21:
# def customUpper(string):
#     """string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters"""
#     counter = 0
#     for i in range(0, 4):
#         if string[i].isupper():
#             counter += 1

#     if counter >= 2:
#         return string.upper()
#     else:
#         return string


# strr = "MyNameisRohan"
# print(customUpper(strr))

# ------------------------------------------

# Question22:
# def lexicographi_sort(s):
#     """program to sort a string lexicographically"""
#     return sorted(sorted(s), key=str.upper)


# print(lexicographi_sort('w3resource'))
# print(lexicographi_sort('quickbrown'))

# ------------------------------------------

# Question23:
# def rmvNewLine(string):
#     """program to remove a newline in Python"""
#     return string.replace("\n", " ")


# strr = "My\nName\nIs\nRohan"
# print(rmvNewLine(strr))

# ------------------------------------------

# Question24:
# def checkChar(string, check):
#     # This Program is Case Sensitive
#     """check whether a string starts with specified characters"""
#     if string[0] == check:
#         return True
#     else:
#         return False


# strr = "MyNameIsRohan"
# check = "M"
# print(checkChar(strr, check))

# ------------------------------------------

# Question25:
#"""program to create a Caesar encryption"""
# pass

# ------------------------------------------

# Question26:
# import textwrap
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# print()
# print(textwrap.fill(sample_text, width=50))
# print()


# ------------------------------------------
