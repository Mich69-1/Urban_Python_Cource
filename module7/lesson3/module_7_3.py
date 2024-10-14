# Домашнее задание по теме "Оператор "with"

class WordsFinder:
    __REMOVE_SMB = ',', '.', '=', '!', '?', ';', ':', ' - '

    def __init__(self, *file_names):
        self.__file_names = file_names

    def get_all_words(self):
        result_dict = dict()
        for file_name in self.__file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for rm in self.__REMOVE_SMB:
                    content = content.replace(rm, '')
                result_dict[file_name] = content.split()
        return result_dict

    def find(self, word_to_find):
        result_dict = dict()
        for name, words in self.get_all_words().items():
            word_pos = 0
            for word in words:
                word_pos += 1
                if word_to_find.lower() == word:
                    result_dict[name] = word_pos
                    break
        if result_dict:
            return result_dict
        else:
            return 'Слово не найдено'

    def count(self, word_to_count):
        result_dict = dict()
        for name, words in self.get_all_words().items():
            word_cnt = 0
            for word in words:
                if word_to_count.lower() == word:
                    word_cnt += 1
            if word_cnt > 0:
                result_dict[name] = word_cnt
        if result_dict:
            return result_dict
        else:
            return 'Слово не найдено'


finder2 = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
print(finder2.count('If'))  # 14 слов 'if' в тексте всего
