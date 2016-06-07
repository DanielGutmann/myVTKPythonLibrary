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

def addPDataNormals(
        pdata,
        orient_outward=1,
        verbose=0):

    myVTK.myPrint(verbose, "*** addPDataNormals ***")

    poly_data_normals = vtk.vtkPolyDataNormals()
    poly_data_normals.ComputePointNormalsOff()
    poly_data_normals.ComputeCellNormalsOn()
    if (vtk.vtkVersion.GetVTKMajorVersion() >= 6):
        poly_data_normals.SetInputData(pdata)
    else:
        poly_data_normals.SetInput(pdata)
    poly_data_normals.Update()
    pdata = poly_data_normals.GetOutput()

    if (orient_outward):
        cell_centers = myVTK.getCellCenters(
            mesh=pdata,
            verbose=verbose-1)
        cell_center = numpy.empty(3)

        mesh_center = numpy.array(pdata.GetCenter())

        normals = pdata.GetCellData().GetNormals()
        normal = numpy.empty(3)

        cnt_pos = 0
        cnt_neg = 0
        for k_cell in xrange(pdata.GetNumberOfCells()):
            cell_centers.GetPoint(k_cell, cell_center)
            outward  = cell_center-mesh_center
            outward /= numpy.linalg.norm(outward)
            normals.GetTuple(k_cell, normal)
            proj = numpy.dot(outward, normal)
            if (proj > 0): cnt_pos += 1
            else:          cnt_neg += 1
        #print cnt_pos
        #print cnt_neg

        if (cnt_neg > cnt_pos):
            poly_data_normals.FlipNormalsOn()
            poly_data_normals.Update()
            pdata = poly_data_normals.GetOutput()

    return pdata
