# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
import MDAnalysis as mda
import numpy as np
import pytim  
from pytim.datafiles import *

u       = mda.Universe(WATER_GRO,WATER_GRO)
g       = u.select_atoms('all')
radii=pytim_data.vdwradii(G43A1_TOP)
interface =pytim.ITIM(u,max_layers=4,molecular=True,multiproc=True,cluster_cut=3.5)
pytim.lap()
interface.assign_layers()
pytim.lap()
interface.writepdb('layers.pdb')
