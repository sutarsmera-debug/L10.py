def count_words_with_loop(text_string):
    word_count = 0
    in_word = False
    for char in text_string:
        if char.isspace():
            in_word = False
        elif not in_word:
            in_word = True
            word_count += 1
    return word_count

sample_text = "no one can touch us if they tried"
print(f"Word count: {count_words_with_loop(sample_text)}")


