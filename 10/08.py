import pandas as pd
import pycaret
gpa = pd.read_csv("http://logopt.com/data/SATGPA.csv", index_col=0, dtype={'MathSAT':float, 'VerbalSAT':float})
from pycaret.regression import *
reg=setup(gpa,target="GPA")
best_model = compare_models(fold=5)
predict_model(best_model)
plot_model(best_model)