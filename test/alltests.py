from test.explorerstests import BfsExplorerTests
from test.graphtests import *
from test.utilstests import UtilsTests


def run_all_tests():
    # Run only the tests in the specified classes
    test_classes_to_run = [MatrixDefinedGraphTests,
                           ListDefinedGraphTests,
                           UtilsTests,
                           BfsExplorerTests]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    return runner.run(big_suite)


if __name__ == '__main__':
    results = run_all_tests()
