# try:
#     %tensorflow_version 2.0
# except Exception:
#     pass
import tensorflow as tf

import tensorflow_hub as hub

from tensorflow.keras import layers
import bert




import tensorflow as tf
import tensorflow_hub as hub
import bert
from tensorflow.keras.models import Model
from tqdm import tqdm
import numpy as np
from collections import namedtuple

print("TensorFlow Version:", tf.__version__)
print("Hub version: ", hub.__version__)
