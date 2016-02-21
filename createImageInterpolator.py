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

import vtk

import myVTKPythonLibrary as myVTK

########################################################################

def createImageInterpolator(
        image,
        verbose=1):

    myVTK.myPrint(verbose, "*** createImageInterpolator ***")

    interpolator = vtk.vtkImageInterpolator()
    interpolator.Initialize(image)
    interpolator.Update()

    return interpolator

