import sys
import unittest

import numpy as np

import pyinduct as pi
import pyinduct.shapefunctions
from pyinduct.shapefunctions import cure_interval, visualize_shapefunctions

if any([arg == 'discover' for arg in sys.argv]):
    show_plots = False
else:
    # show_plots = True
    show_plots = False

if show_plots:
    import pyqtgraph as pg
    app = pg.QtGui.QApplication([])


class VisualisationTestCase(unittest.TestCase):
    def test_lag1st(self):
        dz = pi.Domain(bounds=(0, 1), num=10)
        nodes, funcs = cure_interval(pi.LagrangeFirstOrder, dz.bounds, node_count=5)
        pi.register_base("lag1st", funcs)
        visualize_shapefunctions("lag1st", 0)


class CureTestCase(unittest.TestCase):

    def test_init(self):
        self.assertRaises(TypeError, pyinduct.shapefunctions.cure_interval, np.sin, [2, 3])
        self.assertRaises(TypeError, pyinduct.shapefunctions.cure_interval, np.sin, (2, 3))
        self.assertRaises(ValueError, pyinduct.shapefunctions.cure_interval, pyinduct.shapefunctions.LagrangeFirstOrder,
                          (0, 2))
        self.assertRaises(ValueError, pyinduct.shapefunctions.cure_interval, pyinduct.shapefunctions.LagrangeFirstOrder,
                          (0, 2), 2, 1)

    def test_smoothness(self):
        func_classes = [pi.LagrangeFirstOrder, pi.LagrangeSecondOrder]
        derivatives = {pi.LagrangeFirstOrder: range(0, 2),
                       pi.LagrangeSecondOrder: range(0, 3)}
        tolerances = {pi.LagrangeFirstOrder: [5e0, 1.5e2],
                      pi.LagrangeSecondOrder: [1e0, 1e2, 9e2]}

        for func_cls in func_classes:
            for order in derivatives[func_cls]:
                self.assertGreater(tolerances[func_cls][order], self.shape_generator(func_cls, order))

