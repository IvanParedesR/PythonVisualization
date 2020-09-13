# Introduction to Visualization with Python – Basic and Customized Plotting

# AOpen a jupyter notebook and load the pandas and seaborn libraries:
#Load pandas library

import pandas as pd
import seaborn as sns

#URL of the dataset
diamonds_url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/diamonds.csv"
#Yes, we can read files from a URL straight into a pandas DataFrame!
diamonds_df = pd.read_csv(diamonds_url)
# Since the dataset is available in seaborn, we can alternatively read it in using the following line of code
diamonds_df = sns.load_dataset('diamonds')
diamonds_df_specific_cols = pd.read_csv(diamonds_url, usecols=['carat','cut','color','clarity'])

#Yes, we can read files from a URL straight into a pandas DataFrame!
diamonds_df = pd.read_csv(diamonds_url)
# Since the dataset is available in seaborn, we can alternatively read it in using the following line of code
diamonds_df = sns.load_dataset('diamonds')
