# Basic list manipulation
def p(a_list):
    print(*a_list, sep=" ")

words = ['a', 'b', 'c']
print(words[1:])
print(words[:1] + words[2:])
for w in words[:]:
    words.insert(0, w)
p(words)

seen = set()
unique = []
for w in words:
    if w not in seen:
        unique.append(w)
        seen.add(w)
unique.sort()
p(unique)

words.sort()
p(list(set(words)))
