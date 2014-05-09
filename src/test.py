import unittest
from model import Model
import numpy as np




class Tests(unittest.TestCase):
    def test_up(self):
        print "UP"
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        print model.grid
        model.up()
        print model.grid
        self.assertTrue((np.array([[0,0,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == model.grid).all())

    def test_down(self):
        print "DOWN"
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        print model.grid
        model.down()
        print model.grid
        self.assertTrue((np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,2,0]]) == model.grid).all())

    def test_right(self):
        print "RIGHT"
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        print model.grid
        model.right()
        print model.grid
        self.assertTrue((np.array([[0,0,0,0],[0,0,0,2],[0,0,0,0],[0,0,0,0]]) == model.grid).all())

    def test_left(self):
        print "RIGHT"
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        print model.grid
        model.left()
        print model.grid
        self.assertTrue((np.array([[0,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]) == model.grid).all())




if __name__ == "__main__":
    unittest.main()