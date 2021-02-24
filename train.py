import os
import time
import argparse
import numpy as np
import tensorflow  as tf
import matplotlib.pyplot as plt

try:
    # Should be optional if --log is not set
    import wandb
except:
    wandb = None

# def build_model(config):