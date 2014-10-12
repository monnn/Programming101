def count_words(arr):
    d = {}
    for words in arr:
        count = arr.count(words)
        d.update({words: count})
    return d
print(count_words(["apple", "banana", "apple", "pie"]))
