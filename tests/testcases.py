from nltk.tree import ParentedTree

tree_1 = ("(S(NP(NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))(, ,)(CC or)"
          "(NP (NNP Barri) (NNP Gòtic)))(, ,)(VP(VBZ has)(NP(NP (JJ narrow) "
          "(JJ medieval) (NNS streets))(VP(VBN filled)"
          "(PP(IN with)(NP(NP (JJ trendy) (NNS bars))(, ,)(NP (NNS clubs))"
          "(CC and)(NP (JJ Catalan)(NNS restaurants))))))))")

tree_2 = "(S (NP (NP (DT The) (JJ red) (NN car)) (CC and) (NP (DT the) (JJ blue) (NN car))) (VP (VBD collided)))"

tree_3 = ("(S (NP (DT The) (JJ young) (NN boy)) (VP (VBZ loves) (NP (NP (DT his) (NN cat)) "
          "(CC and) (NP (DT his) (NN dog)))))")

# ==========================test_parser==========================

parser_correct_cases = [
    ['NP , CC NP CC NP', ['NP', ',', 'CC', 'NP', 'CC', 'NP']],
    [' NP CC NP CC NP', ['NP', 'CC', 'NP', 'CC', 'NP']],
    [' NP , NP , NP ', ['NP', ',', 'NP', ',', 'NP']],
    [' NP , CC , NP , CC , NP ', ['NP', ',', 'CC', ',', 'NP', ',', 'CC', ',', 'NP']]
]

parser_raise_parse_exception_cases = [
    '123',
    'NP NP NP',
    'CC NP , CC',
    'NP CC NP CC',
    ' ',
    ''
]

# ==========================test_NP_extractor==========================

extractor_correct_cases = [
    [ParentedTree.fromstring(tree_1), [[(0, 0), (0, 3)], [(2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)]]],
    [ParentedTree.fromstring(tree_2), [[(0, 0), (0, 2)]]],
    [ParentedTree.fromstring(tree_3), [[(1, 1, 0), (1, 1, 2)]]],
]

extractor_raise_attr_error_cases = [
    '123',
    tree_1,
    tree_2,
    ' '
]

# ==========================test_combinations_processing==========================

# --------------------------create_combinations--------------------------

create_combinations_correct_cases = [
    [[(0, 1), (2, 3)], [((0, 1), (2, 3)), ((2, 3), (0, 1))]],
    [[(0, 0), (0, 3)], [((0, 0), (0, 3)), ((0, 3), (0, 0))]],
    [
        [(2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)],

        [((2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)),
         ((2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2)),
         ((2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4)),
         ((2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0)),
         ((2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2)),
         ((2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0))]
    ]
]

create_combinations_raise_type_error_cases = [
    5,
    10.1
]

# --------------------------unite_combinations--------------------------

unite_combinations_correct_cases = [
    [
        [[((0, 1), (2, 3)), ((2, 3), (0, 1))], [((5, 6), (7, 8)), ((7, 8), (5, 6))]],

        [
            (((0, 1), (2, 3)), ((5, 6), (7, 8))), (((0, 1), (2, 3)), ((7, 8), (5, 6))),
            (((2, 3), (0, 1)), ((5, 6), (7, 8))), (((2, 3), (0, 1)), ((7, 8), (5, 6)))
        ]
    ],

    [[(0, 1), (2, 3)], [(0, 2), (0, 3), (1, 2), (1, 3)]],
    [[(0, 0), (0, 3)], [(0, 0), (0, 3), (0, 0), (0, 3)]]
]

unite_combinations_raise_type_error_cases = [
    5,
    10.1
]

# --------------------------normalize_original_list--------------------------

normalize_original_list_correct_cases = [
    [[[(0, 0), (0, 2)]], [(0, 0), (0, 2)]],
    [[[(1, 1, 0), (1, 1, 2)]], [(1, 1, 0), (1, 1, 2)]],
    [
        [[(0, 0), (0, 3)], [(2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)]],
        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)]
    ]
]

normalize_original_list_raise_type_error_cases = [
    5,
    10.1
]

# --------------------------normalize_target_list--------------------------

tree_1_target_list = [(((0, 0), (0, 3)), ((2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4))),
                      (((0, 0), (0, 3)), ((2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2))),
                      (((0, 0), (0, 3)), ((2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4))),
                      (((0, 0), (0, 3)), ((2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0))),
                      (((0, 0), (0, 3)), ((2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2))),
                      (((0, 0), (0, 3)), ((2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0))),
                      (((0, 3), (0, 0)), ((2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4))),
                      (((0, 3), (0, 0)), ((2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2))),
                      (((0, 3), (0, 0)), ((2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4))),
                      (((0, 3), (0, 0)), ((2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0))),
                      (((0, 3), (0, 0)), ((2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2))),
                      (((0, 3), (0, 0)), ((2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0)))]

tree_1_expected_list = [[(0, 0), (0, 3), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)],
                        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2)],
                        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4)],
                        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0)],
                        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2)],
                        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0)],
                        [(0, 3), (0, 0), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)],
                        [(0, 3), (0, 0), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2)],
                        [(0, 3), (0, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 4)],
                        [(0, 3), (0, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0)],
                        [(0, 3), (0, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2)],
                        [(0, 3), (0, 0), (2, 1, 1, 1, 1, 4), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 0)]]

normalize_target_list_correct_cases = [
    [
        [(((1, 1, 0), (1, 1, 2)),), (((1, 1, 2), (1, 1, 0)),)],
        [[(1, 1, 0), (1, 1, 2)], [(1, 1, 2), (1, 1, 0)]]
    ],
    [
        [(((0, 0), (0, 2)),), (((0, 2), (0, 0)),)],
        [[(0, 0), (0, 2)], [(0, 2), (0, 0)]]
    ],

    [tree_1_target_list, tree_1_expected_list]
]

normalize_target_list_raise_type_error_cases = [
    5,
    10.1
]

# ==========================test_trees_creator==========================

expected_tree_1_list = [
    {
        'tree': '(S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)'
                '(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(JJtrendy)(NNSbars))(,,)'
                '(NP(NNSclubs))(CCand)(NP(JJCatalan)(NNSrestaurants))))))))'
    },
    {
        'tree': '(S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)'
                '(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(JJtrendy)(NNSbars))(,,)'
                '(NP(JJCatalan)(NNSrestaurants))(CCand)(NP(NNSclubs))))))))'
    },
    {
        'tree': '(S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)'
                '(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(NNSclubs))(,,)(NP(JJtrendy)'
                '(NNSbars))(CCand)(NP(JJCatalan)(NNSrestaurants))))))))'
    },
    {
        'tree': '(S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)'
                '(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(NNSclubs))(,,)(NP(JJCatalan)'
                '(NNSrestaurants))(CCand)(NP(JJtrendy)(NNSbars))))))))'
    },
    {
        'tree': '(S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)'
                '(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(JJCatalan)(NNSrestaurants))'
                '(,,)(NP(JJtrendy)(NNSbars))(CCand)(NP(NNSclubs))))))))'
    }
]

expected_tree_2_list = [
    {'tree': '(S(NP(NP(DTThe)(JJred)(NNcar))(CCand)(NP(DTthe)(JJblue)(NNcar)))(VP(VBDcollided)))'},
    {'tree': '(S(NP(NP(DTthe)(JJblue)(NNcar))(CCand)(NP(DTThe)(JJred)(NNcar)))(VP(VBDcollided)))'}
]

expected_tree_3_list = [
    {'tree': '(S(NP(DTThe)(JJyoung)(NNboy))(VP(VBZloves)(NP(NP(DThis)(NNcat))(CCand)(NP(DThis)(NNdog)))))'},
    {'tree': '(S(NP(DTThe)(JJyoung)(NNboy))(VP(VBZloves)(NP(NP(DThis)(NNdog))(CCand)(NP(DThis)(NNcat)))))'}
]

trees_creator_correct_cases = [
    [
        ParentedTree.fromstring(tree_1),
        [(0, 0), (0, 3), (2, 1, 1, 1, 1, 0), (2, 1, 1, 1, 1, 2), (2, 1, 1, 1, 1, 4)],
        tree_1_expected_list,
        5,
        expected_tree_1_list
    ],

    [
        ParentedTree.fromstring(tree_2), [(0, 0), (0, 2)], [[(0, 0), (0, 2)], [(0, 2), (0, 0)]], 5,
        expected_tree_2_list
    ],

    [
        ParentedTree.fromstring(tree_3), [(1, 1, 0), (1, 1, 2)], [[(1, 1, 0), (1, 1, 2)], [(1, 1, 2), (1, 1, 0)]], 5,
        expected_tree_3_list
    ]
]

trees_creator_raise_cases = [
    ['string', 5, 5, 0]
]

# (S(NP(NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))(, ,)(CC or)(NP (NNP Barri) (NNP Gòtic)))(, ,)(VP(VBZ has)(NP(NP (JJ narrow) (JJ medieval) (NNS streets))(VP(VBN filled)(PP(IN with)(NP(NP (JJ trendy) (NNS bars))(, ,)(NP (NNS clubs))(CC and)(NP (JJ Catalan)(NNS restaurants))))))))