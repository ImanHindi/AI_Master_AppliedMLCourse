strings = ['abcc','card', 'aaaa', 'acac']
strings.sort(key=lambda x:len(set(list(x))))
'''
return the list of string sorted by the number of uniq char in each string so :
no of unique letter in 'card'=4 , in 'aaaa'=1, in 'acac'=2 and in 'abcd'=4
'''
print(strings)
'''
out=['aaaa', 'acac', 'abcc', 'card']
which ['aaaa', 'acac', 'abcc', 'card'] have these unique letters [1,2,3,4] respectively
'''
list1=[2,15,4,7,2,19]
#list1.sort(reverse=True)
print(list1)
x=list(reversed(list1))
print(x)