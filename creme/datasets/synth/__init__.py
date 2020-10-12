"""Synthetic datasets.

Each synthetic dataset is an infinite generator.

"""
from .agrawal import Agrawal
from .anomaly_sine import AnomalySine
from .friedman import Friedman
from .hyper_plane import Hyperplane
from .led import LED
from .led import LEDDrift
from .logical import Logical
from .mixed import Mixed
from .random_rbf import RandomRBF
from .random_rbf import RandomRBFDrift
from .random_tree import RandomTree
from .sea import SEA
from .sine import Sine
from .stagger import STAGGER
from .waveform import Waveform


__all__ = [
    'Agrawal',
    'AnomalySine',
    'Friedman',
    'Hyperplane',
    'LED',
    'LEDDrift',
    'Logical',
    "Mixed",
    "RandomRBF",
    "RandomRBFDrift",
    "RandomTree",
    'SEA',
    'Sine',
    'STAGGER',
    'Waveform'
]
