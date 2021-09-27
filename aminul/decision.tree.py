import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import beluga
from tyty import pipeline


train_data, test_data, train_labels, test_labels = pipeline.full_pipeline(
    feature_columns=["Gender", "EarSide", "Age"]
)

model = LogisticRegression(penalty="l1", solver="liblinear")

train_pred, test_pred, trained_model = pipeline.modelling_pipeline(
    model, train_data, train_labels, test_data
)

beluga.metrics.summary(train_labels, train_pred, conditions=True)
beluga.metrics.summary(test_labels, test_pred, conditions=True)
