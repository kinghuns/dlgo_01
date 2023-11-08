import unittest
import sys
from goboard_slow import GoString
from gotypes import Player, Point

class TestGoString(unittest.TestCase):
    new_string = None
    new_string = GoString(Player.black, 
                              [Point(1,1), Point(1,2)],
                              [Point(0,1), Point(0,2), Point(1,0), Point(1,3), Point(2,1), Point(2,2)])
    # def setUp(self):
        
    
    def test_merging(self):
        '''
        Test merging of two strings
        '''
        #1. reate two strings
        #2. merge them
        #3. check the merged string's properties
        pass

    def test_liberties(self):
        '''
        Test liberties of a string
        '''
        #1. create a string
        # new_string = None
        # new_string = GoString(Player.black, 
        #                       [Point(1,1), Point(1,2)],
        #                       [Point(0,1), Point(0,2), Point(1,0), Point(1,3), Point(2,1), Point(2,2)])
        #2. remove a liberty
        #3. check the number of liberties
        print(self.new_string.num_liberties)
        # print(sys.path)
        self.assertEqual(self.new_string.num_liberties, 6)
        #self.assertEqual(new_string.num_liberties, 1)

    def test_remove_liberty(self):
        '''
        Test removing a liberty
        '''
        #1. create a string
        #2. remove a liberty
        #3. check the number of liberties
        #1. create a string
        
        #2. remove a liberty
        #3. check the number of liberties
        print(self.new_string.num_liberties)
        self.new_string.remove_liberty(Point(0,2))
        #self.assertEqual(new_string.num_liberties, 2)
        self.assertEqual(self.new_string.num_liberties, 5)
        self.new_string.add_liberty(Point(0,2))

    def test_add_liberty(self):
        '''
        Test adding a liberty
        '''
        #1. create a string
        #2. add a liberty
        self.new_string.add_liberty(Point(0,3))
                #3. check the number of liberties
        self.assertEqual(self.new_string.num_liberties, 7)
        self.new_string.remove_liberty(Point(0,3))

    def test_occupied_points(self):
        '''
        Test occupied points of a string
        '''
        #1. create a string
        #2. check the number of occupied points
        pass

    def test_equality(self):
        '''
        Test equality of two strings
        '''
        #1. create two strings
        #2. check equality
        pass

    def test_inequality(self):
        '''
        Test inequality of two strings
        '''
        #1. create two strings
        #2. check inequality
        pass
    
if __name__ == '__main__':
    unittest.main()