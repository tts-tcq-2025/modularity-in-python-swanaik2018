from test_color_utils import test_number_to_pair, test_pair_to_number
from reference_manual import print_reference_manual

def run_tests():
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed!')

if __name__ == '__main__':
    run_tests()
    print_reference_manual()
