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

def writeImage(
        image,
        filename,
        verbose=0):

    myVTK.myPrint(verbose, "*** writeImage: "+filename+" ***")

    if ('vtk' in filename):
        image_writer = vtk.vtkImageWriter()
    elif ('vti' in filename):
        image_writer = vtk.vtkXMLImageDataWriter()
    else:
        assert 0, "File must be .vtk or .vti. Aborting."

    myVTK.myPrint(verbose-1, "n_points = "+str(image.GetNumberOfPoints()))

    image_writer.SetFileName(filename)
    if (vtk.vtkVersion.GetVTKMajorVersion() >= 6):
        image_writer.SetInputData(image)
    else:
        image_writer.SetInput(image)
    image_writer.Update()
    image_writer.Write()
