import unittest
import os
from typing import List
#
# path_dir = '../VPES_Auto'
# file_list = os.listdir(path_dir)
# print(file_list)
# var = path_dir.find('.py') is not -1
# print(var)
#
# testmodules = [var]
# suite = unittest.TestSuite()
#
# for t in testmodules:
#     try:
#         # If the module defines a suite() function, call it to get the suite.
#         mod = __import__(t, globals(), locals(), ['suite'])
#         suitefn = getattr(mod, 'suite')
#         suite.addTest(suitefn())
#     except (ImportError, AttributeError):
#         # else, just load all the test cases from the module.
#         suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
#
# unittest.TextTestRunner().run(suite)



def load_tests(loader, tests, pattern):

    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('../VPES_Auto', pattern='C*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()