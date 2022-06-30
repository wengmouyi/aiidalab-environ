# -*- coding: utf-8 -*-
import os

import ipywidgets as ipw
import traitlets
from aiida.common import NotExistent
from aiida.engine import ProcessBuilderNamespace, ProcessState, submit
from aiida.orm import ProcessNode, WorkChainNode, load_code
from aiida.plugins import DataFactory

from aiidalab_widgets_base import (
    ComputationalResourcesWidget,
    ProcessMonitor,
    ProcessNodesTreeWidget,
    WizardAppWidgetStep,
)
from IPython.display import display


class input_settings(ipw.VBox):
    
    
    
    def __init__(self, **kwargs):
        self.solvent_model = ipw.Dropdown(
            options=["vacuum", "water", "water-cation", "water-anion"],
            value="vacuum",
            description="Solvent type:",
            disabled=False,
            style={"description_width": "initial"},
        )
        self.kpoints_distance = ipw.FloatText(
            value=0.05,
            step=0.05,
            description="K-points distance (1/Å):",
            disabled=False,
            style={"description_width": "initial"},
        )
        self.spin_type = ipw.Dropdown(
            options=[("Non-magnetic", "none"), ("Ferromagnetic", "collinear")],
            value="none",
            description="Magnetism:",
            style={"description_width": "initial"},
        )
        self.structure_type = ipw.Dropdown(
            options=["3D", "2D-x", "2D-y", "2D-z", "1D-x", "1D-y","1D-z","0D"],
            value="3D",
            description="Dimension of structure:",
            style={"description_width": "initial"},
        )
        
        super().__init__(
            children=[self.solvent_model,self.kpoints_distance, self.spin_type , self.structure_type,],
            **kwargs,
        )


class inputsteps(ipw.VBox, WizardAppWidgetStep):
    
    workchain_settings = traitlets.Instance(input_settings, allow_none=True)
    
    def __init__(self, **kwargs):
        self.workchain_settings = input_settings()
        #self.parameters = ipw.VBox(self.workchain_settings)
        
        self.tab = ipw.VBox(
            children=[
                self.workchain_settings,
            ],
            layout=ipw.Layout(min_height="250px"),
        )
        
        super().__init__(
            children=[self.tab,],
            **kwargs,
        )

    



