
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt

def create_rectangular_prism(length, width, height):
    """
    Create a rectangular prism using PythonOCC.
    
    :param length: Length of the prism
    :param width: Width of the prism
    :param height: Height of the prism
    :return: The created shape
    """
    return BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), length, width, height).Shape()
