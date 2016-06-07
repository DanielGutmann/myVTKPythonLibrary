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

import os
import vtk

import myVTKPythonLibrary as myVTK

########################################################################

def readImage(
        filename,
        verbose=0):

    myVTK.myPrint(verbose, "*** readImage: "+filename+" ***")

    assert (os.path.isfile(filename)), "Wrong filename (\""+filename+"\"). Aborting."

    if ('vtk' in filename):
        image_reader = vtk.vtkImageDataReader()
    elif ('vti' in filename):
        image_reader = vtk.vtkXMLImageDataReader()
    else:
        assert 0, "File must be .vtk or .vti. Aborting."

    image_reader.SetFileName(filename)
    image_reader.Update()
    image = image_reader.GetOutput()

    myVTK.myPrint(verbose-1, "n_points = "+str(image.GetNumberOfPoints()))

    return image
