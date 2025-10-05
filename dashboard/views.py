from django.shortcuts import render
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


def home(request):
    dfs = sns.get_dataset_names()
    return render(request, 'dashboard/home.html', {'dfs':dfs})
