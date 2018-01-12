def reverse_word(words):
    list_of_words = words.split()
    reverse_list = list()
    for item in list_of_words:
        reverse_list.insert(0, item)
    reverse_list = ' '.join(reverse_list)
    return reverse_list


words = input("\nWrite some words here: \n")
print('\n', reverse_word(words))
