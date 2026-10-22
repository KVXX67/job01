def my_long_word(n, text):
    words = []
    current_word = ""
    for char in text:
        if char == " " or char == "," or char == ".":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    result_words = []
    for word in words:
        length = 0
        for _ in word:
            length += 1
        if length > n:
            result_words.append(word)
    result = ""
    for i, word in enumerate(result_words):
        result += word
        if i < len(result_words) - 1:
            result += " "
    return result

text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
result = my_long_word(3, text)
print(result)