#coding=utf8

########################################################################
###                                                                  ###
### Created by Martin Genet, 2012-2016                               ###
###                                                                  ###
### University of California at San Francisco (UCSF), USA            ###
### Swiss Federal Institute of Technology (ETH), Zurich, Switzerland ###
### École Polytechnique, Palaiseau, France                           ###
###                                                                  ###
########################################################################

import numpy
import vtk

import myVTKPythonLibrary as myVTK

########################################################################

def rotatePoints(
        old_points,
        C,
        R,
        verbose=0):

    myVTK.myPrint(verbose, "*** rotatePoints ***")

    n_points = old_points.GetNumberOfPoints()

    new_points = vtk.vtkPoints()
    new_points.SetNumberOfPoints(n_points)

    old_point = numpy.empty(3)
    for k_point in xrange(n_points):
        old_points.GetPoint(k_point, old_point)
        #print old_point

        new_point = C + numpy.dot(R, old_point - C)
        #print new_point

        new_points.InsertPoint(k_point, new_point)

    return new_points
