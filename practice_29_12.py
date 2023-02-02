"""
problem statements:
1.Write a Python program to add 'ing' at the
end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
def st_change(str):
  if len(str) > 2:
      if str[-3:] == 'ing':
          str += 'ly'
  return str
print(st_change('zing'))
print(st_change('string'))
print(st_change('abhi'))

op->
zingly
stringly
abhi

Process finished with exit code 0
-----------------------------------------------------------------
In the following example,user will enter the password data.
if the password matches, it will print welcome to python course, else
 print wrong password and user will renenter password.
 in the 4th trial it will print one trial left





predefined_password = 'password2233'


def pass_func():

    for correct_pass in range(4):
        password =(input('enter the password:'))
        if correct_pass < 3:



            if password == predefined_password:
            print('you have entered correct password')
            break
                elif password != predefined_password:
                    print('you have entered wrong password')
                    elif correct_pass == 3:
                    return 'you have only one chance left'
                else:
            print('check the password you have entered')
pass_func()


-----------------------------------------------
. Write a Python program to find the first appearance
 of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
---------------------------------------
1. Write a python program to sort python dictionaries using keys

d = {'abhi':24,'ashish':26,'abraham':48,'atul':18}
{i:d[i] for i in sorted(d)}
op-->
{'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}
--------------------------------------
2. Python program to sort Python Dictionaries by Values
d = {'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}
print({i:y for i,y in sorted(d.items(),key= lambda x:x[1])})

op-->
{'atul': 18, 'abhi': 24, 'ashish': 26, 'abraham': 48}
----------------------------------
3. Python program to find the sum of all items in a dictionary
d = {'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}


# solution 1: by using for loop concept using a normal function
def func_Name(d):
        sum = 0
        for i in d.values():
                sum += i
        return sum

# Driver Function
print("Sum :", func_Name(d))

op-->
Sum : 116
---------------------------
# solution using reduce function
from functools import reduce
print(reduce(lambda x,y:x+d[y],d,0))
op-->
116
------------------------------------
4. Python program to remove a key from a dictionary
# solution using del keyword to remove a particular key
del d['abhi']
print(d)

op-->
{'abraham': 48, 'ashish': 26, 'atul': 18} # 'abhi' navachi key remove zali
-------------------------------
# Using items() + dict comprehension to Remove a Key from a Dictionary
new_d = {x:y for x,y in d.items() if x != 'abraham'}
print(new_d)
op--->
{'abhi': 24, 'ashish': 26, 'atul': 18}
---------------------------
5. Python program to merge two Dictionaries
d = {'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}
d2 = {'karan':21, 'suhas':27, 'madhu':33, 'kashish':37}
# using ** we can merge two dictionaries
op-->
{'karan': 21, 'suhas': 27, 'madhu': 33, 'kashish': 37, 'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}
--------------------------
d = {'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}
d2 = {'karan':21, 'suhas':27, 'madhu':33, 'kashish':37}
# solution using copy() and update()
k = d2.copy()
k.update(d)
print(k)

op-->
{'karan': 21, 'suhas': 27, 'madhu': 33, 'kashish': 37, 'abhi': 24, 'abraham': 48, 'ashish': 26, 'atul': 18}
----------------------------------------


6. Program to create grade calculator in Python


print("Enter Marks Obtained in 5 Subjects: ")
english = int(input())
science = int(input())
mathematics = int(input())
history = int(input())
geography = int(input())

total = english+science+mathematics+history+geography
average = total/5

if average>=91 and average<=100:
        print('Your grade is A1')
elif average>=81 and average<91:
        print('Your grade is A2')
elif average >=71 and average<81:
        print('Your grade is B1')
elif average >=61 and average<71:
        print('Your grade is B2')
elif average >= 51 and average<61:
        print('Your grade is C1')
elif average >=41 and average<51:
        print('Your grade is C2')
elif average >= 35:
        print('Your grade is C3')
else:
        print('You have failed the exam\ntry again next year')


op-->
Enter Marks Obtained in 5 Subjects:
81
78
91
84
72
Your grade is A2
-------------------------------------------
7. Print anagrams together in Python using List and Dictionary

# anagrams: Any two strings that have the same character in a different order are known as anagrams.
i. e.,
input = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac'] and
the output should be = [['cat', 'tac'], ['dog', 'god'], ['fried', 'fired'], ['pat', 'tap']]

tips to solve above problem statement:
-Initialize the list of strings.
-Initialize an empty dictionary.
-Iterate over the list.
-Sort the string.
-Check whether it's present in the dictionary or not.
-If it is present in the dictionary, then append the string to its list.
-Else initialize the key with a list including the current string to store the anagrams.
-Print all the values of the dictionary in a list.


solution:

# initialzing a list of strings
anagrams = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
# initializing an empty dict
grouped_anagrams = {}
# iterating over the list to group all anagrams
for string in anagrams:
   # sorting the string
   sorted_string = str(sorted(string))
   # checking the string in dict
   if sorted_string in grouped_anagrams:
      # adding the string to the group anagrams
      grouped_anagrams[sorted_string].append(string)
   else:
       grouped_anagrams[sorted_string] = [string]
       # initializing a list with current string

# printing the values of the dict (anagram groups)
print(list(grouped_anagrams.values()))

op-->
[['cat', 'tac'], ['dog', 'god'], ['fired', 'fried'], ['pat', 'tap']]

Process finished with exit code 0

## another easy solution

anagrams = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
ang_list = []
ang_dict ={}

for i in anagrams:
    for j in anagrams:
        if sorted(i) == sorted(j) and i != j:
            if i not in ang_dict.values():
                ang_dict.update({i:j})
                ang_list.append([i,j])
print(ang_list,ang_dict)

op--->
[['cat', 'tac'], ['dog', 'god'], ['fired', 'fried'], ['pat', 'tap']]
{'cat': 'tac', 'dog': 'god', 'fired': 'fried', 'pat': 'tap'}

------------------------------------------
8. Check if binary representations of two numbers are an anagram


-Given two numbers you are required to check whether they
 are anagrams of each other or not in binary representation.
# Input : a = 8, b = 4
# Output : Yes
# Binary representations of both
# numbers have same 0s and 1s.
# Check each bit in a number is set or not
# and return the total count of the set bits.
def countSetBits(n):
   count = 0
   while n > 0:
      count += n & 1
      n >>= 1
   return count


def areAnagrams(A, B):
   return countSetBits(A) == countSetBits(B)


# Driver code
if __name__ == "__main__":

   a, b = 8, 4
   if areAnagrams(a, b):
      print("yes the are anagrams")
   else:
      print("no they are not anagrams")

op-->
yes the are anagrams

Process finished with exit code 0
--------------------------------------
9. Python Counter to find the size of the largest subset of anagram words


solution:
# Function to find the size of largest subset
# of anagram words
from collections import Counter

def maxAnagramSize(input):

	# split input string separated by space
	input = input.split(" ")

	# sort each string in given list of strings
	for i in range(0,len(input)):
		input[i]=''.join(sorted(input[i]))

	# now create dictionary using counter method
	# which will have strings as key and their
	# frequencies as value
	freqDict = Counter(input)

	# get maximum value of frequency
	print (max(freqDict.values()))

# Driver program
if __name__ == "__main__":
	input = 'ant magenta magnate tan gnamate'
	maxAnagramSize(input)

op-->

3
--------------------------------
10. Python Dictionary to find mirror characters in a string
# Given a string and a number N, we need to mirror the characters
from the N-th position up to the length of the string
in alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pneumlmrz

solution:

# function to mirror characters of a string

def mirrorChars(input, k):
   # create dictionary
   original = 'abcdefghijklmnopqrstuvwxyz'
   reverse = 'zyxwvutsrqponmlkjihgfedcba'
   dictChars = dict(zip(original, reverse))

   # separate out string after length k to change
   # characters in mirror
   prefix = input[0:k - 1]
   suffix = input[k - 1:]
   mirror = ''

   # change into mirror
   for i in range(0, len(suffix)):
      mirror = mirror + dictChars[suffix[i]]

   # concat prefix and mirrored part
   print(prefix + mirror)


# Driver program
if __name__ == "__main__":
   input = 'harshwardhan'
   k = 3
   mirrorChars(input, k)


op-->
haihsdziwszm

Process finished with exit code 0
-----------------------------------------------
11. Counting the frequencies in a list using a dictionary in Python
def count_frequencies(lst):
    counts = {}
    for x in lst:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
    return counts

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = count_frequencies(lst)
print(counts)

op-->
{1: 1, 2: 2, 3: 3, 4: 4}

Process finished with exit code 0
------------------------------------------------------
12. Python program to convert a list of Tuples into Dictionary
def convert_to_dict(lst):
    return dict(lst)

lst = [("apple", 1), ("banana", 2), ("cherry", 3)]
dct = convert_to_dict(lst)
print(dct)


op-->
{'apple': 1, 'banana': 2, 'cherry': 3}

Process finished with exit code 0
-------------------------------------------------
13. Scraping And Finding Ordered Words In A Dictionary using Python


import requests
from bs4 import BeautifulSoup
import re

def get_words(url):
    # Download the webpage
    response = requests.get(url)
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract the words
    words = re.findall(r'\b\w+\b', soup.get_text())
    return words

def find_ordered_words(url, words):
    # Get the words from the webpage
    webpage_words = get_words(url)
    # Initialize a list to store the ordered words
    ordered_words = []
    # Iterate over the words in the webpage
    for i, word in enumerate(webpage_words):
        if i + len(words) > len(webpage_words):
            break
        # Check if the current word and the following words match the words in the list
        if webpage_words[i:i+len(words)] == words:
            ordered_words.append(words)
    return ordered_words

# Example
url = "http://www.example.com"
words = ["this", "is", "an", "example"]
ordered_words = find_ordered_words(url, words)
print(ordered_words)
-----------------------------------------

14. Create a list of tuples from the given list having a number and its cube in each tuple
def get_cubes(lst):
    return [(x, x**3) for x in lst]

lst = [1, 2, 3, 4, 5]
cubes = get_cubes(lst)
print(cubes)


op-->
[(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]

Process finished with exit code 0
------------------------------------------

15. Sort a list of tuples by the second Item


def sort_by_second_item(lst):
    return sorted(lst, key=lambda x: x[1])

lst = [("cherry", 3), ("apple", 1), ("banana", 2),]
sorted_lst = sort_by_second_item(lst)
print(sorted_lst)

op-->
[('apple', 1), ('banana', 2), ('cherry', 3)]

Process finished with exit code 0

--------------------------------------------
16. Python Program for Insertion Sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j] :
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

lst = [5, 2, 4, 6, 1, 3]
insertion_sort(lst)
print(lst)

op-->
[1, 2, 3, 4, 5, 6]

#Insertion sort has a time complexity of O(n^2) in the worst case,
 so it may not be the most efficient sorting algorithm for large lists.
  However, it has a number of advantages, including its simplicity,
  low overhead, and ability to sort lists in place (without creating a new sorted list).
  These features make it a good choice for certain types of problems.

#  time complexity O(n**2)

Process finished with exit code 0
-----------------------------------------

17. Python Program for Selection Sort



Selection sort works by iterating over the elements of the list,
and selecting the minimum element at each step.
It then swaps the minimum element with the current element,
and moves on to the next element. This is repeated until the list is sorted.

The algorithm maintains two sublists: a sorted sublist, and an unsorted sublist.
At each step, the minimum element from the unsorted sublist is selected
 and added to the sorted sublist.
 The unsorted sublist shrinks by one element at each step,
 as the minimum element is moved to the sorted sublist.
 When all the elements have been moved to the sorted sublist, the algorithm is complete.

 # Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):

	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)


#  time complexity O(n*n)
 -----------------------------------------------
 18. Python Program for Bubble Sort


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]

lst = [5, 2, 4, 6, 1, 3]
bubble_sort(lst)
print(lst)

op-->

[1, 2, 3, 4, 5, 6]

Process finished with exit code 0

# Python program for implementation of Bubble Sort


def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
if __name__ == "__main__":

    arr = [5, 1, 4, 2, 8]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i], end=" ")



#Bubble sort works by iterating over the elements of the list and
#swapping adjacent elements that are out of order.
#This is repeated until the list is sorted.

#The algorithm maintains a flag that indicates whether any swaps
#have been made during a pass through the list.
#If no swaps are made, then the list is already sorted and the algorithm can stop.
#This optimization can reduce the worst-case time complexity of the algorithm from O(n^2) to O(n).

----------------------------------------------
19. Python Program for Merge Sort

# Time Complexity: O(n*log(n))
--------------------------------------------
str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
print(list((filter(lambda x:x>lenght,numbers))))

=---------------------------
# 23.Write a Python program to calculate the sum of the positive
# and negative numbers of a given list of numbers using lambda function.

lst = [11,22,-34,-2,-45,56,87,-8]
positive = [i for i in lst if i>0]
negative = [i for i in lst if i<0]
from functools import reduce
pos_num_sum =(reduce(lambda x,y:x+y,positive))
neg_num_sum =(reduce(lambda x,y:x+y,negative))
print(pos_num_sum,neg_num_sum)

--------------------------------

lst = [11,22,-34,-2,-45,56,87,-8]
print('sum of negative num:', sum(list(filter(lambda x: x < 0, lst))))
print('sum of positive num:', sum(list(filter(lambda x: x>0,lst))))
--------------------------------------
#20.Write a Python program to find the numbers of a given string and store them in a list, display the
numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.

def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))
op-->
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Process finished with exit code 0

-------------------------------------
#21.Write a Python program that multiply each number of given list
with a given number using lambda function. Print the result.
--------------------------------------------------------
2.	Write a program that will convert celsius value to fahrenheit
 celsius = float(input("Enter temperature in celsius: ")) fahrenheit = (celsius * 1.8) + 32 print(str(celsius )+
 " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit. ")


celsius = float(input('Enter Temperature in Celsius:'))
fahrenheit = ((9/5)*celsius)+32
print(fahrenheit)

op-->
Enter Temperature in Celsius:27
80.6

Process finished with exit code 0

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(str(celsius )
+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit. ")

op-->
Enter temperature in celsius: 27
27.0 degree Celsius is equal to 80.6 degree Fahrenheit.

Process finished with exit code 0
-----------------------------------------------
3. User will input (2numbers).Write a program to swap the numbers
a = 1
b = 2
a,b = b,a
print(a)
print(b)

op-->
2
1

Process finished with exit code 0




"""





