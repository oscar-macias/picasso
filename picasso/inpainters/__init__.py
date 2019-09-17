# Copyright (c) 2018-2019 Giuseppe Puglisi.
# Full license can be found in the top level "LICENSE" file.
"""Inpainting models for use in analysis.


"""

# These are simply namespace imports for convenience.

from .deep_prior_inpainter import  DeepPrior

from .nearest_neighbours_inpainter import  NearestNeighbours

from .generative_inpainting_model  import InpaintCAModel

from .interfaces import HoleInpainter
