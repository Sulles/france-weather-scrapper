# Visualize all stitches
# TODO: colors

import plotly.express as px

from config import *
from util import *

# grab all stitching data as a pd.DataFrame
stitching_data = pd.read_csv(STITCHING_GUIDE_FILE_NAME, index_col=0)

# create px.bar figure
fig = px.bar(stitching_data, height=800, title="Stitching Data")
fig.show()
