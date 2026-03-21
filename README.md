# Student Math Score Predictor

Predicts a student's math score based on their background — things like parental education, lunch type, test prep, and their reading/writing scores. Built as a proper end-to-end ML pipeline with a Flask web interface on top.

---

## How it works

The pipeline has three stages:

- **Data Ingestion** — reads the raw dataset and splits it into train/test sets
- **Data Transformation** — numerical features get standard scaled, categorical ones get one-hot encoded, all handled via sklearn pipelines
- **Model Training** — trains 7 models with GridSearchCV, picks the best one by R² score, and saves it as a `.pkl` file

At prediction time, the saved model and preprocessor get loaded and the user's input runs straight through.

---

## Models compared

Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost, CatBoost, AdaBoost — all tuned with cross-validation. Best model wins.

---

## Stack

Python · scikit-learn · XGBoost · CatBoost · Flask · pandas · dill · Gunicorn

---

## Run it locally

```bash
git clone https://github.com/JainulTrivedi55555/Student-Math-Score-Predictor-End-to-End-ML-Pipeline.git
cd Student-Math-Score-Predictor-End-to-End-ML-Pipeline
pip install -r requirements.txt

# Train the model
python src/components/data_ingestion.py

# Start the app
python application.py
```

Then go to `http://localhost:5000`, fill in the form, and get a prediction.

---

## Project layout

```
├── application.py
├── setup.py
├── requirements.txt
├── render.yaml
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   ├── data/
│   │   └── stud.csv
│   └── catboost_info/
│       ├── catboost_training.json
│       ├── learn_error.tsv
│       └── time_left.tsv
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── catboost_info/
│   ├── catboost_training.json
│   ├── learn_error.tsv
│   └── time_left.tsv
│
└── .ebextensions/
    └── python.config
```
