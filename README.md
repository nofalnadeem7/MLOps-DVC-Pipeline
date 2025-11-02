# MLOps-DVC-Pipeline
This is a project to implement a test run of DVC end to end pipeline 


🧠 Gender Prediction Pipeline with DVC and MLOps Principles

This project demonstrates a simple Machine Learning workflow using DVC (Data Version Control)
, where we predict gender based on age using a basic classification model. The goal is to showcase reproducible pipelines and experiment tracking with only 5 rows of sample data.

📁 Project Structure
├── data/
│   ├── sample_data.csv        # Raw input data
│   ├── prepared_data.csv      # Cleaned data (output of prepare.py)
│   └── features.csv           # Final features for training (output of feature.py)
├── models/
│   └── model.pkl              # Trained ML model
├── metrics/
│   └── metrics.json           # Model evaluation metrics
├── src/
│   ├── prepare.py             # Prepare raw data
│   ├── feature.py             # Feature engineering
│   ├── train.py               # Model training
│   └── evaluate.py            # Model evaluation and metrics
├── params.yaml                # Experiment parameters
├── dvc.yaml                   # DVC pipeline stages
├── dvc.lock                   # DVC pipeline lock file
├── data.dvc                   # DVC tracking for data folder
└── README.md                  # Instructions & documentation

🚀 Workflow Overview

This pipeline has four DVC stages:

Prepare
Cleans raw data, removing null values, and saves a cleaned version.

Feature Engineering
Converts categorical labels to numerical values and selects important columns (Age and Gender).

Train
Trains a Random Forest model on the features and saves it as model.pkl.

Evaluate
Tests model performance, prints evaluation metrics, and saves accuracy & classification report in a JSON file.

Each stage depends on the previous one and is fully reproducible using DVC.

🔧 Install Dependencies

Clone the repo and install required packages:

git clone <your-repo-url>
cd <your-project-folder>
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

🔄 Initialize DVC (first time only)
dvc init


To track data with DVC:

dvc add data/  # Creates data.dvc
git add data.dvc .gitignore
git commit -m "Track data folder with DVC"

▶️ Run the Full Pipeline

Run all pipeline stages in order:

dvc repro


If files or scripts change, DVC will rerun only the stages affected.

🧪 Track Experiments

You can run experiments and compare metrics easily:

dvc exp run
dvc exp show


To save an experiment as a Git commit:

dvc exp apply <exp-name>
git add .
git commit -m "Save experiment results"

📊 View Metrics

DVC stores evaluation metrics in metrics/metrics.json.

To see the tracked metrics:

dvc metrics show


This gives a quick comparison between experiment runs.

🧹 Clean Up Cache (Optional)

If you want to clear unnecessary cache and artifacts:

dvc gc -w

✅ Conclusion

This project demonstrates a minimal but fully functional ML pipeline with:

Version-controlled data and code

Reproducible stages with DVC

Metrics tracking and experiment management

Feel free to extend the dataset, add visualizations, or automate deployment as you explore more MLOps concepts!

👨‍💻 Author

Built by Nofal Nadeem as part of learning DVC and MLOps fundamentals.
