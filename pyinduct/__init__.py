# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
from .control import ControlLaw, Controller
from .core import Function, normalize_base
from .placeholder import (Scalars, ScalarTerm, IntegralTerm, FieldVariable, SpatialDerivedFieldVariable,
                          TemporalDerivedFieldVariable, Product, TestFunction, Input)
from .registry import register_base, deregister_base, get_base, is_registered
from .shapefunctions import cure_interval, LagrangeFirstOrder, LagrangeSecondOrder
from .simulation import (Domain, EvalData, SimulationInput, SimulationInputSum, WeakFormulation, simulate_system,
                         process_sim_data, evaluate_approximation)
from .trajectory import SmoothTransition, gevrey_tanh
from .utils import find_roots
from .visualization import PgAnimatedPlot, PgSurfacePlot

__author__ = "Stefan Ecklebe, Marcus Riesmeier"
__email__ = "stefan.ecklebe@tu-dresden.de, marcus.riesmeier@umit.at"
__version__ = '0.4.0'
