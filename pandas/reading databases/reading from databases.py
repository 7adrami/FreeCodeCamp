import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

conn = sqlite3.connect("C:/Users/dell/Desktop/FreeCodeCamp/pandas/reading databases/chinook.db")
df = pd.read_sql("SELECT * FROM employees;", conn)
df.head()