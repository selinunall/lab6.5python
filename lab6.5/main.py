#question1
def find_common(list1, list2):
    list3 = set(list1) & set(list2)
    return list(list3)


#question2
def palindrome_strings(s_list):
    palindromes=[]

    for string in s_list:
        if string == string[::-1]:
            palindromes.append(string)

    return palindromes


#question3
def eratosthenes_primes(input_list):


    sieve = [True] * (max(input_list) + 1)

    sieve[0] = sieve[1] = False

    for i in range(2, int(max(input_list) ** 0.5) + 1):

        if sieve[i]:
            for j in range(i * i, len(sieve), i):
                sieve[j] = False

    prime_list = [x for x in input_list if sieve[x]]

    return prime_list


#question4
def anagrams(word,word_list):
    word_items = sorted(word)
    a_list = []

    for string in word_list:
        sorted_string = sorted(string)
        if sorted_string == word_items:
            a_list.append(string)
    return a_list






list1=[1,4,0,8]
list2=[2,4,6,8]
common_list = find_common(list1,list2)
print(common_list)

string_list=['selin','ana','kapı','ata']
palindrome_list=palindrome_strings(string_list)
print(palindrome_list)

integer_list=[5,9,6,16,85,31,11]
prime_list=eratosthenes_primes(integer_list)
print(prime_list)

wordList=['enlist','google','inlets','banana']
anagram_list=anagrams('listen',wordList)
print(anagram_list ) 