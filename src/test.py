import unittest
from model import Model
import numpy as np

class DirectionTests(unittest.TestCase):
    def test_up(self):
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        model.up()
        self.assertTrue((np.array([[0,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]) == model.grid).all())

    def test_down(self):
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        model.down()
        self.assertTrue((np.array([[0,0,0,0],[0,0,0,2],[0,0,0,0],[0,0,0,0]]) == model.grid).all())

    def test_right(self):
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        model.right()
        self.assertTrue((np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,2,0]]) == model.grid).all())

    def test_left(self):
        model = Model()
        model.grid = np.array([[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]])
        model.left()
        self.assertTrue((np.array([[0,0,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == model.grid).all())




if __name__ == "__main__":
    unittest.main()