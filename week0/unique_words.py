def unique_words_count(arr):
    second_array = []
    for words in arr:
        if words not in second_array:
            second_array.append(words)
    return len(second_array)
print(unique_words_count(["python", "python", "python", "ruby"]))
