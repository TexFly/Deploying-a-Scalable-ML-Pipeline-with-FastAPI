# Model Card
Develop a classification model on publicly available Census Bureau data and write code to monitor the model performance on various data slices. Deploy the model using the FastAPI package.
## Model Details
The model type used is Logistical Regression. 
## Intended Use
This project is intended for testing and hobbyist use, not suitable for official applications.
## Training Data
The training data is represented by the 80% of the source dataset which includes the following columns:
Age, Workclass, Fnlgt, Education, Marital Status, Occupation, Relationship, Race, Sex, Capital Gain, Capital Loss, Hours per Week, Native Country, Salary (target), Evaluation Data (20%) 
The dataset is publicly available at the Census Bureau data here: https://archive.ics.uci.edu/dataset/20/census+income
The dataframe has a shape of 32,561 (rows) x 15 (columns).
## Evaluation Data
The evaluation data is represented by the 20% of the same dataset used for training, which is publicly available at the Census Bureau data here: https://archive.ics.uci.edu/dataset/20/census+income
## Metrics
The metrics used are precision, recall, and F1. The performance results are:
Precision: 0.7255 | Recall: 0.2775 | F1: 0.4015
## Ethical Considerations
Although anonymized, the dataset includes sensitive details such as work class, occupation, race, country of origin, and gender. The model is not suitable for making individual determinations; its sole purpose is educational. Precision scores for data slices based on "Race" and "Sex" were found to be reasonable.
## Caveats and Recommendations
The model could benefit from more extensive and accurate data, especially regarding salary limitations (>50k and >=50k). The "Country of Origin" column had numerous American values but lacked sufficient diversity to provide reliable predictions.

