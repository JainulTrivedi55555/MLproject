# Student Math Score Predictor

A machine learning web app that predicts a student's math score based on demographic and academic background. Built as a full end-to-end ML pipeline — from raw data and exploratory analysis all the way to a deployed Flask web application.

What It Does
You plug in a few details about a student — their gender, ethnicity, parental education level, lunch type, whether they completed a test prep course, and their reading and writing scores — and the app predicts what their math score is likely to be.
The interesting part isn't just the prediction itself, but how the project is structured. Instead of a single messy notebook, everything is broken into proper components: data ingestion, transformation, model training, and a prediction pipeline. The kind of structure you'd actually see in a real ML engineering role.

Tech Stack

Python 3.10
scikit-learn — preprocessing pipelines, model training, GridSearchCV
XGBoost / CatBoost — gradient boosted models for comparison
pandas / numpy — data handling
Flask — web interface
dill — serializing the trained model and preprocessor
Gunicorn — production server
Render / AWS Elastic Beanstalk — deployment configs included for both


Project Structure
├── application.py               # Flask app entry point
├── src/
│   ├── components/
│   │   ├── data_ingestion.py    # Reads raw data, splits into train/test
│   │   ├── data_transformation.py  # Preprocessing pipeline (scaling, encoding)
│   │   └── model_trainer.py     # Trains & evaluates 7 models, saves the best
│   ├── pipeline/
│   │   ├── train_pipeline.py    # Orchestrates the training flow
│   │   └── predict_pipeline.py  # Loads saved model and runs inference
│   ├── utils.py                 # Shared helpers (save/load objects, evaluate models)
│   ├── exception.py             # Custom exception handling
│   └── logger.py                # Logging setup
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── templates/
│   ├── index.html
│   └── home.html                # Prediction form
├── artifacts/                   # Saved model.pkl and preprocessor.pkl
├── requirements.txt
└── render.yaml / .ebextensions/ # Deployment configs

Models Trained
Seven regression models are trained and compared using GridSearchCV with cross-validation. The best-performing one (by R² on the test set) is saved automatically:
ModelTuned via GridSearchCVLinear Regression—Decision TreecriterionRandom Forestn_estimatorsGradient Boostinglearning_rate, subsample, n_estimatorsXGBoostlearning_rate, n_estimatorsCatBoostdepth, learning_rate, iterationsAdaBoostlearning_rate, n_estimators

How to Run It Locally
1. Clone the repo
bashgit clone https://github.com/JainulTrivedi55555/Student-Math-Score-Predictor-End-to-End-ML-Pipeline.git
cd Student-Math-Score-Predictor-End-to-End-ML-Pipeline
2. Install dependencies
bashpip install -r requirements.txt
3. Train the model
bashpython src/components/data_ingestion.py
This runs the full pipeline — ingests data, transforms features, trains all 7 models, and saves the best one to artifacts/.
4. Start the web app
bashpython application.py
Then open http://localhost:5000 in your browser, fill in the form, and hit predict.

Input Features
FeatureTypeGendermale / femaleRace / EthnicityGroup A–EParental Level of Educationhigh school → master's degreeLunch Typestandard / free or reducedTest Preparation Coursenone / completedReading Score0–100Writing Score0–100
Output: Predicted math score (0–100)

Deployment
The repo includes configs for two deployment options:
Render — via render.yaml, starts with gunicorn application:applicatio
