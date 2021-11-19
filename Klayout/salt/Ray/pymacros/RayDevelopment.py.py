import pya
import numpy as np


class InnerLeads(pya.PCellDeclarationHelper):
    """
    The PCell declaration for the CrossRingLabeled
    """

    def __init__(self):

        # Important: initialize the super class
        super(InnerLeads, self).__init__()

        # declare the parameters
        self.param("l", self.TypeLayer, "Layer", default=pya.LayerInfo(1, 0))

        self.param("w1", self.TypeDouble, "Width 1", default=2.0)
        self.param("w2", self.TypeDouble, "Width 2", default=1)
        self.param("l", self.TypeDouble, "length", default=50)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "InnerLeads(L=%s)" % (str(self.l))

    def produce_impl(self):

        pts = [
            pya.DPoint(-0.5*self.w1, self.l),
            pya.DPoint(0.5*self.w1, self.l),
            pya.DPoint(0.5*self.w2, 0),
            pya.DPoint(-0.5*self.w2, 0),
        ]

        pad = pya.DPolygon(pts,)
        # for i in range(self.n_p):
        #    tt = pya.DCplxTrans(1,  i*angle, False, 0,0)
        self.cell.shapes(self.l_layer).insert(pad)


class RayDev(pya.Library):
    """
    The library where we will put the PCell into 
    """

    def __init__(self):

        # Set the description
        self.description = "Ray De's PCell Library"

        # Create the PCell declarations

        # self.layout().register_pcell("OverlayAlignMarkArray", OverlayAlignMarkArray())

        self.layout().register_pcell("InnerLeads", InnerLeads())
        # Register us with the name "SerpentineLib".
        self.register("RayDev")


# Instantiate and register the library
RayDev()
