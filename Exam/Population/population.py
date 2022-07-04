"""
Exam task 3 Population Main
"""
import json
from binary_search_tree import BST


def population(path):
    """
    Create 3 Binary Search Tree with population data:
    (people percentage ,year) by settlements
    """
    trees = {'Кути': BST(), 'КутиСтарі': BST(), 'Брустури': BST()}
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)['Косівщина']
    for line in data:
        percentage = (line['гр-кат.']/(line['гр-кат.'] + line['лат.'] +
                      line['вірм.'] + line['жид.'] + line['акат.']))*100
        trees[line['населений пункт']].add((percentage, line['рік']))
    return trees


def years_more_percent(tree: BST, flag_perc: float) -> list[str]:
    """
    Return list with years when percentage was more than flag
    """
    return [data[1] for data in tree.more_than((flag_perc, '1919'))]


if __name__ == '__main__':
    state_trees = population('Population/Kosiv_state.json')
    result1 = years_more_percent(state_trees['Кути'], 90)
    result2 = years_more_percent(state_trees['КутиСтарі'], 90)
    result3 = years_more_percent(state_trees['Брустури'], 90)
    print(result1, result2, result3)
