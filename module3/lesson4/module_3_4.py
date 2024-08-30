# Самостоятельная работа по уроку "Произвольное число параметров".

def single_root_words(root_word, *other_words):
    same_words = []
    for c_word in other_words:
        if c_word.lower().rfind(root_word.lower()) != -1 or root_word.lower().rfind(c_word.lower()) != -1:
            same_words.append(c_word)
    return same_words


print(single_root_words('дубин', 'Дуб', 'дубинка', 'Длинношеее', 'Дубинин'))
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
