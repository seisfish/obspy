# -*- coding: utf-8 -*-
"""
The obspy.imaging.radiation_pattern test suite.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

import unittest

import matplotlib.pyplot as plt
from obspy.core.event import plot_3drpattern
from mpl_toolkits.mplot3d import Axes3D


class RadPatternTestCase(unittest.TestCase):
    """
    Test cases for radiation_pattern.
    """

    def test_farfield(self):
        """
        Tests to plot P/S wave farfield radiation pattern
        """
        #some possible moment tensors:

        #mt = [0.91, -0.89, -0.02, 1.78, -1.55, 0.47]
        #RTP convention, Peru 2001/6/23 20:34:23:
        #mt = [2.245, -0.547, -1.698, 1.339, -3.728, 1.444]
        #mt = [1., -0.5, -0.5, 0., 0, 0.1]
        mt = [-1., 0.5, 0.5, 0., 0, 0.]
        #mt = [0., 0., 0., 0., 1, 0.]

        plot_3drpattern(mt, kind='p_sphere')

def suite():
    return unittest.makeSuite(RadPatternTestCase, 'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
