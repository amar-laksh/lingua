import sys
import re

KEYWORDS = ['amar', 'ane']
sys.argv[0] = "./lesson1-2"
if(not sys.argv[0]):
    sys.exit()

f = open(sys.argv[0])

words = set(re.sub(r'[^\w\s]','',''.join(f.readlines()).lower()).format(*KEYWORDS).split())
for keyword in KEYWORDS:
        words.remove(keyword)
print(words)
print(len(words))


