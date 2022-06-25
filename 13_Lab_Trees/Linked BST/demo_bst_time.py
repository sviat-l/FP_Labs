""" Compare time of list search and different BST's"""
from time import time
from linkedbst import LinkedBST
import random


def get_words(path):
    """ Open file and create list with words"""
    with open(path, 'r', encoding = 'utf-8') as file:
        words = [line.strip() for line in file]
    return words

def get_check_words(all_words):
    """ Return list with 10 000 words find them in data structures """
    return [random.choice(all_words) for _ in range(10000)]

def consistent_tree(data):
    """ Create tree with adding nodes consicuently by list order"""
    tree = LinkedBST()
    for word in data:
        tree.add(word)
    return tree

def random_tree(data):
    """ Create and return tree with nodes added randomly """
    tree = LinkedBST()
    while data:
        tree.add(data.pop(random.choice(data)))
    return tree

def balanced_tree(data):
    """ Create balanced binary tree with items from data"""
    tree = LinkedBST()
    for word in data:
        tree.add(word)
    return tree.rebalance()

def demo_bst(words_path):
    """ Run search algorithms and compare time"""
    all_words = get_words(words_path)
    test_cases = get_check_words(all_words)
    st_time = time()
    string_names = ['sorted list', 'consistent binary tree', 'random binary tree', 'balanced binary tree']

    DATA_STRUCTURES = [all_words, consistent_tree(all_words), random_tree(all_words), balanced_tree(all_words)]
    for i in range(4):
        data = DATA_STRUCTURES[i]
        st_time = time()
        for word in test_cases:
            if word in data:
                continue
        taken_time = time() - st_time
        print(f'Time to find 10000 items in {string_names[i]}: {taken_time:.2f}')

if __name__ == '__main__':
    demo_bst('words.txt')