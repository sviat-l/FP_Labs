"""
Palindrom check implemented with stack ADT
"""

from arraystack import ArrayStack  # or from linkedstack import LinkedStack

class Palindrome:
    """ Palindrome class """
    @staticmethod
    def read_file(file_path):
        """ Read file on stated path and get words from it"""
        with open(f'{file_path}', 'r', encoding= 'utf-8') as file:
            all_words = [line.strip().split()[0] for line in file]
        return all_words

    @staticmethod
    def write_file(file_path, words):
        """ write correct words to the file on stated path """
        with open(f'{file_path}', 'w', encoding='utf-8') as file:
            file.write('\n'.join(words))

    @staticmethod
    def find_palindromes(read_file_path, write_file_path):
        """ find all palindromes from yhe read
        file and save them into the file with stated path
        """
        all_words = Palindrome.read_file(read_file_path)
        palindrome_list = []
        for word in all_words:
            # add first half to the stack
            letters_stack = ArrayStack()
            for i in range(len(word)//2):
                letters_stack.push(word[i])
            # compare last stack letters with word second half
            is_palindrome = True
            for j in range((len(word)+1)//2, len(word)):
                if letters_stack.pop() != word[j]:
                    is_palindrome = False
                    break
            if is_palindrome:
                palindrome_list.append(word)

        Palindrome.write_file(write_file_path, palindrome_list)
        return palindrome_list

if __name__ == "__main__":
    Palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    Palindrome.find_palindromes("words.txt", "palindrome_en.txt")
