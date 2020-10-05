pip install pandas

import pandas as pd
import io
import re
import h5py
import numpy as np

df = pd.read_csv(io.StringIO(uploaded['data.csv'].decode('utf-8')), sep = ',')
df