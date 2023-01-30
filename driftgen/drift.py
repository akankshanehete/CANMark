import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


class Drift:
    def __init__(self, drift_type: str, drift_scale: float, transition_period=0) -> None:
        self.drift_type = drift_type
        self.drift_scale = drift_scale
        self.transition_period = transition_period
        self.start = None
        self.end = None
