#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:56:22 2020

@author: michelmake
"""


class Element:

    def __init__(self, connectivity, rng):

        self.connectivity = connectivity
        self.rng = rng

    def rotate(self, fixed_node):
        """

        Parameters
        ----------
        fixed_node : Int
           Node that is fixed and will not be part of rotation

        Raises
        ------
        ValueError
            The fixed_node must be in the given connectivity list. Hence
            0 < fixed_node < 5 must hold for tetrahedral elements.

        Returns
        -------
        TYPE
            This function rotatates a tetrahedal element while keeping one of
            its nodes fixed. "fixed_node" is the fixed node. Rotation is
            counter clockwise. Rotate twice to obtain clockwise rotation.
        """

        # Check input values
        if not 0 < fixed_node < 4:
            error = 'Fixed_node {} not in range 1 to 4'.format(
                fixed_node)
            raise ValueError(error)

        # Exclude fixed node before rotation
        rotating_nodes = self.connectivity[:fixed_node-1] + \
            self.connectivity[fixed_node:]

        # Rotate non-fixed nodes
        rotated_nodes = rotating_nodes[1:] + rotating_nodes[:1]

        # Concatenate all nodes and return result
        return rotated_nodes[:fixed_node-1] + \
            [self.connectivity[fixed_node-1]] + \
            rotated_nodes[fixed_node-1:]
