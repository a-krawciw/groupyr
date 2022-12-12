# CSC 2515 Final Project Code Guide
Please use the link below to find the different
aspects of this project that were modified.

[https://github.com/a-krawciw/groupyr/tree/csc2515/class_proj
](https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py)

## Cross Validation for Unweighted Models
This jupyter notebook contains the primary processing for
unweighted models.
Additionally, it creates the correlation matrix.


[https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/CSC2515_FinalProject_SourceCode.ipynb
](https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py)

## groupyr Modifications to Support Weighted Logistic Regression

The `groupyr` library was modified to add
weighted logistic regression. Two source files were changed. The direct links to the changes are given below.

Main WeightedLogisticSGL Class:
[https://github.com/a-krawciw/groupyr/blob/3097241e97c22e03708e98685c65acfabe2b6b94/groupyr/logistic.py#L1220
](https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py)

Proximal Gradient Descent Operator:
[https://github.com/a-krawciw/groupyr/blob/523179f7fdfbd7f3eaa957d22b52aeaf61c4747a/groupyr/_base.py#L339
](https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py)

## Cross Validation with Weighted Models
The weighted logistic regression experiments were performed seperately.
Additionally, this script contains the code to run the OvR experiment.
The plot for regularization strength is generated at the end as well.

[https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/weighted_logistic_analysis.ipynb
](https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py)

## TSNE Plot
[https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py](https://github.com/a-krawciw/groupyr/blob/csc2515/class_proj/TSNE_Visualization.py)