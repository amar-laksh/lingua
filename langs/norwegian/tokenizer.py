import sys
import re

KEYWORDS = ['amar', 'ane']
if(len(sys.argv) == 1):
    sys.exit()

f = open(sys.argv[1])

words = set(re.sub(r'[^\w\s]','',''.join(f.readlines()).lower()).format(*KEYWORDS).split())
for keyword in KEYWORDS:
        words.discard(keyword)
print(sorted(words))
print(len(words))
