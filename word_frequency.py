#word_frequency.py counts frequency of words in a sentence

def word_frequency(sentence):
    words = sentence.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

sentence = input("Enter a sentence:")
result = word_frequency(sentence)

sorted_result = sorted(
    result.items(),
    key = lambda item: item[1],
    reverse = True
)

print("Word Frequency:\n")
for word, count in sorted_result:
    print(f"{word} : {count}")