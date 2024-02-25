import shutil
import itertools
from copy import deepcopy
from pathlib import Path

from nltk.tree import ParentedTree
from pyparsing import Word, OneOrMore, StringEnd, ParseException


def delete_cache(input_path):
    for path in input_path.iterdir():
        if path.is_dir() and path.name == '__pycache__':
            shutil.rmtree(path)
        elif path.is_dir():
            delete_cache(path)


def parse_subtree(input_string: str):
    """
    This method is written with pyparsing library that
    simplifies the work with regular expressions.

    This method checks the combination of labels of the first-line children of a NP subtree.
    This combination must comply with the pattern "NP + delimiter (',' or 'CC') + NP"

    :param input_string:
    :return:
    """

    parser_unit = Word('NP') + \
        OneOrMore(
        OneOrMore(Word('CC' + ',')) +
        Word('NP')
    ) + \
        StringEnd()
    parsed_string = parser_unit.parse_string(input_string).asList()
    return parsed_string


def extract_NP_subtrees(p_tree: ParentedTree):
    """
    This method searches for all NP subtrees, gets in the variable 'child_positions'
    all relative positions of the first-line children of the subtree, gets labels of that children
    and checks the compliance of the combination of the labels with the pattern "NP + delimiter (',' or 'CC') + NP".
    Then it gets the absolute positions of the children if these comply.

    :param p_tree:
    :return:
    """

    abs_positions_list = []

    for subtree in p_tree.subtrees():
        if subtree.label() == 'NP':
            child_positions = list(filter(lambda x: len(x) == 1, subtree.treepositions()))
            subtree_labels = [subtree[pos].label() for pos in child_positions]

            try:
                parse_subtree(' '.join(subtree_labels))
                tree_position = subtree.treeposition()
                abs_positions_list.append([tree_position + pos for pos in child_positions
                                           if p_tree[tree_position + pos].label() == 'NP'])
            except ParseException:
                continue

    return abs_positions_list


def create_combinations(positions_list: list):
    """
    This method takes a list of NP-children positions and
    creates a list of all possible combinations of that positions:
    [(0,1), (2,3)] --> [((0,1), (2,3)), ((2,3), (0,1))]

    :param positions_list:
    :return:
    """
    combinations = list(itertools.permutations(positions_list))
    return combinations


def unite_combinations(combinations_list: list):
    """
    This method makes the combinations of positions of different NP subtrees:

    [
        [((0,1), (2,3)), ((2,3), (0,1))], [((5,6), (7,8)), ((7,8), (5,6))]
    ]
    ---->
    [
        (((0,1), (2,3)), ((5,6), (7,8))), (((0,1), (2,3)), ((7,8), (5,6))),
        (((2,3), (0,1)), ((5,6), (7,8))), (((2,3), (0,1)), ((7,8), (5,6)))
    ]

    :param combinations_list:
    :return:
    """

    return list(itertools.product(*combinations_list))


def normalize_original_list(combinations_list: list):
    """
    In this method the original positions of NP-children got from the method 'extract_NP_subtrees'
    are being normalized: the tuples of position of different NP-subtrees are unified in the list of tuples.
    This is important for the further removes of the subtrees.

    [[((0,1), (2,3)), ((5,6), (7,8))]] -->
    [[(0,1), (2,3), (5,6), (7,8)], [(0,1), (2,3), (7,8), (5,6)]]

    :param combinations_list:
    :return:
    """

    normalized_list = []
    for combination in combinations_list:
        normalized_list += combination

    return normalized_list


def normalize_target_list(combinations_list: list):
    """
    In this method the result of the 'unite_combinations' method are being normalized:
    the tuples of position of different NP-subtrees are unified in the list of tuples.

    [(((0,1), (2,3)), ((5,6), (7,8))), (((0,1), (2,3)), ((7,8), (5,6)))] -->
    [[(0,1), (2,3), (5,6), (7,8)], [(0,1), (2,3), ((7,8), (5,6)]]

    :param combinations_list:
    :return:
    """

    normalized_list = []
    for combination in combinations_list:
        normalized_combination = []
        for item in combination:
            normalized_combination += item
        normalized_list.append(normalized_combination)

    return normalized_list


def create_trees(p_tree: ParentedTree, original_positions: list, target_positions: list, limit: int):
    """
    This method creates new syntax trees based on the different possible
    combinations of the NP-subtrees. The number of such new trees is limited with a 'limit' param.

    :param p_tree:
    :param original_positions:
    :param target_positions:
    :param limit:
    :return:
    """

    list_of_trees = []

    for combination in target_positions[:limit]:
        tree = deepcopy(p_tree)
        for i, pos in enumerate(combination):
            if original_positions[i] != pos:
                tree[original_positions[i]] = deepcopy(p_tree[pos])
        list_of_trees.append({"tree": str(tree).replace('\n', '').replace(' ', '')})

    return list_of_trees


def main():
    input_tree = '(S(NP(NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))(, ,)(CC or)(NP (NNP Barri) (NNP Gòtic)))(, ,)(VP(VBZ has)(NP(NP (JJ narrow) (JJ medieval) (NNS streets))(VP(VBN filled)(PP(IN with)(NP(NP (JJ trendy) (NNS bars))(, ,)(NP (NNS clubs))(CC and)(NP (JJ Catalan)(NNS restaurants))))))))'
    p_tree = ParentedTree.fromstring(input_tree)

    positions_list = extract_NP_subtrees(p_tree)
    normalized_original_positions = normalize_original_list(positions_list)

    combinations = [create_combinations(positions) for positions in positions_list]
    normalized_target_positions = normalize_target_list(unite_combinations(combinations))

    list_of_trees = create_trees(p_tree, normalized_original_positions, normalized_target_positions, 5)

    for tree in list_of_trees:
        print(tree)


if __name__ == '__main__':
    main()
    delete_cache(Path(__file__).parent.parent)
