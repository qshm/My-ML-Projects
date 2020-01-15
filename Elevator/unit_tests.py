import unittest
import numpy as np

class MyTest(unittest.TestCase):

    def __init__(self, testName, extraArg1, extraArg2):
        super(MyTest, self).__init__(testName)  # calling the super class init varies for different python versions.  This works for 2.7
        self.myExtraArg1 = extraArg1
        self.myExtraArg2 = extraArg2

    def setUp(self):
        print('setup')

    def test_something(self):
        self.assertEquals(self.myExtraArg1,self.myExtraArg2)

    def runTest(self):
        print('test completed')

# call your test
suite = unittest.TestSuite()


for rand1, rand2 in zip(np.random.randint(0,2,3), np.random.randint(0,2,3)):
    print(rand1, rand2)
    suite.addTest(MyTest('test_something', rand1, rand2))


unittest.TextTestRunner(verbosity=1).run(suite)