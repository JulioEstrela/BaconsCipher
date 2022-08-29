import textwrap as tw
import string

alphabet = tuple(string.ascii_lowercase)

baconCode = ["AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA",
"AABBB", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA", "ABBAB", "ABBBA",
"ABBBB", "BAAAA", "BAAAB", "BAABA", "BAABB", "BABAA", "BABAB", "BABBA", 
"BABBB","BBAAA", "BBAAB"]

text = input()
temp = ""
res = []

for i in text:
    if i >= 'a' and i <= 'z':
        i = 'A'
    elif i >= 'A' and i <='Z':
        i = 'B'
    else:
        i = ''
    temp += i

temp = tw.wrap(temp, 5)

for chunk in temp:
    for item in baconCode:
        if item == chunk:
            item = alphabet[baconCode.index(item)]
            res += item

res = "".join(res)
print(temp)
print(res)
