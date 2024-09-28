# Задача "Найдёт везде":
class WordsFinder:
    def __init__(self, *file_names :str):
        self._file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self._file_names:
            with open(file_name, "r", encoding="utf-8") as explicit_file:
                lst_words = []
                for line in explicit_file.readlines():  #explicit_file содержит список строк всего файла
                    line = line.strip().lower()
                    for char in (",", ".", ";", ":", "?", "!", "=", " - "):
                        line = line.replace(char, " ")
                    # l = []
                    # for word in line:
                    #     if word:
                    #         l.append(word)
                    lst_words.extend([l for l in line.split(" ") if l])
            all_words[file_name] = lst_words
        return all_words

    def find(self, word):
        more_words = self.get_all_words()
        result = {}
        for file, words in more_words.items():
            if word.lower in words:
                result[file] = words.index(word.lower())
        return result

    def count(self, word):
        more_words = self.get_all_words()
        result = {}
        for file, words in more_words.items():
            if word.lower in words:
                result[file] = words.count(word.lower())
        return result


finder2 = WordsFinder('test_file.txt', "Rudyard_Kipling_If.txt", "Walt_Whitman_O_Captain_My_Captain!.txt", "Mother_Goose_Monday`s_Child.txt")
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
