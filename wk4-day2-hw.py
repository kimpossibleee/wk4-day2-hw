'''Exercise #1
Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.
'''
words = ['this' , 'is', 'a', 'sentence', '.']

'''
input: list of words
process: reverse words using in-place algorithm
output: reversed list
'''

def reverse_list(words):
    j = len(words) - 1
    i = 0
    while i < j:
        words[i], words[j] = words[j][::-1], words[i][::-1]
        i += 1
        j -= 1
    return words

print(reverse_list(words))

'''
Exercise #2
Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
Should output:
{'a': 5,
'abstract': 1,
'an': 3,
'array': 2, ... etc...
'''
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

'''
input: string sentence
process:counds distinct words in string
output: dictionary with word/amount
'''
def distinct_words(sentence):
    words_dict = {}
    for word in sentence.split():
        word = word.lower()
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

print(distinct_words(a_text))

'''
Exercise #3
Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

Hint: Linear Searching will require searching a list for a given number.
nums_list = [10,23,45,70,11,15]
target = 70

# If number is not present return -1

input: nums_list
process: go through each number in list
output: return True if it exists, False if it doesn't
'''
nums_list = [10,23,45,70,11,15]
target = 70

def linear_search(nums_list, target):
    for i in range(len(nums_list)):
        if nums_list[i] == target:
            return True
        i += 1
    return False

print(linear_search(nums_list, target))
