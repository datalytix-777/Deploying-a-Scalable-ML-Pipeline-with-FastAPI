# Model Card for Census Income Classifier

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Caleb  Hill created the model. It is a Random Forest Classifier using a sample of 100 and a random state of 42 for reproducibility. 

## Intended Use
This model should be used to predict if an individual makes over 50k a year. 

## Training Data
The data was obtained from the UCI Irvine Machine Learning Repository (https://archive.ics.uci.edu/dataset/20/census+income). The target class is salary.
The original data set has 32,561 rows, and a 80-20 split was used for the test and training datasplit respectively. The data was prepared for training by using one hot encoding for the categorical features and a label binarizer for the labels.

## Evaluation Data
Evaluation was performed on the 20% of the data that was withheld from testing from the original dataset. This data was also prepared for training by using one hot encoding for the categorical features and a label binarizer for the labels and contains the same class distrobutions as the original and training datasets.

## Metrics (General)
The model was evaluated using precision, recall, and an F1 score:
- **Precision**: 0.74 
- **Recall**: 0.64 
- **F1**: 0.69

This reflects a holistic look at the 20% test splits performance.
### Performance On Categorical Slices (Deepdive)
In an effort to review the data's fairness we analyzed model performance across slices of categorical data

Key observations include:
- **Occupation**: 
  - `Exec-managerial` had a high F1 score of 0.77
  - `Farming-fishing` had a low F1 score of 0.31
- **Education**:
  - `Doctorate`: F1 score of 0.88
  - `7th-8th`: F1 score of 0.00
- **Sex**:
  - `Male`: F1 = 0.70
  - `Female`: F1 = 0.60
- **Race**:
  - `White`: F1 = 0.69
  - `Black`: F1 = 0.67
  - `Asian-Pac-Islander`: F1 = 0.75

Some slices have very low sample sizes (Cambodia, Columbia, ect.) and reported perfect F1 scores as a result, this is likely unreliable. These results may assist in future efforts to address fairness concerns.

## Ethical Considerations
Risk: This models results could unintentionally affirm a viewpoint that the attributes in this dataset are the only or best predictors of someone's income. We know this is not the case.
Mitigation Strategy: Based on this, some interventions may need performed to correct the biases in the dataset.

## Caveats and Recommendations
Our target is greatly unbalanced with the majority of individuals, about 76%, earning <=50k. It is also important to note that about 86% of all persons described in this data are white and about 67% are male. Due to these imbalances it may be prudent to remediate this in the future via tuning, different sampling strategies, ect., although it may only mitigate rather than resolve the underlying fairness issues.  