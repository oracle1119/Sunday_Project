nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x % 2 == 0, nums))
print(filtered)

text = "Python"
print(text[::-1])

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)

s = "this is a test this is only a test"
word_count = {word: s.split().count(word) for word in set(s.split())}
print(word_count)

filtered = list(i for i in range(1,51) if i%3==0 and i%5==0)
print(filtered)

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)

s = "mississippi"
print(max(set(s), key=lambda x: s.count(x)))