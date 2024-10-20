"""
CP1404 - Practical 5 - 3. Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""

def main():
    user_input = input("Text: ")
    word_to_value = count_word_occurrences(user_input)
    max_word_length = max(len(word) for word in word_to_value)
    for word, count in sorted(word_to_value.items()):
        print(f"{word:{max_word_length}} : {count}")

def count_word_occurrences(text):
    words = text.split()
    word_to_value = {}
    for word in words:
        word = word.lower()
        if word in word_to_value:
            word_to_value[word] += 1
        else:
            word_to_value[word] = 1

    return word_to_value

main()