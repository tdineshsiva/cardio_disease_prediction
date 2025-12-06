# Cardio Disease Prediction using XGBClassifier and Streamlit

This project predicts the risk of cardiovascular disease using machine learning. It uses the XGBClassifier algorithm trained on the health.csv dataset and includes a Streamlit web application where users enter medical details to get an instant prediction about heart disease risk.

## Features
- Heart disease risk prediction using machine learning
- Streamlit web app for easy user interaction
- Fast and accurate predictions powered by XGBClassifier
- Clean medical input form with BMI calculation support
- Scalable model that can be deployed locally or on cloud

## Technologies Used
- Python
- XGBoost (XGBClassifier)
- Streamlit
- Pandas, NumPy
- Scikit-Learn

## How to Run
Install required packages:  
pip install -r requirements.txt  

Run the Streamlit web app:  
streamlit run app.py  

Enter the following health information in the app and click “Predict”:  
- Age  
- Gender  
- Height & Weight (BMI auto-calculated if coded)  
- Blood Pressure (Systolic / Diastolic)  
- Cholesterol  
- Glucose  
- Smoking, Alcohol consumption, Physical activity

The model will display one of the following:
- **High Risk of Cardiovascular Disease**
- **Low Risk of Cardiovascular Disease**

## Dataset Information
The project uses the health.csv dataset containing medical, physical, and lifestyle parameters related to cardiovascular disease. The dataset was cleaned and preprocessed before training to improve prediction accuracy.

## Applications
- Cardiology diagnosis assistance
- Early heart disease screening
- Health-risk assessment systems
- AI-powered medical analytics

## Citation (BibTeX)
If you reference this project in academic work or research publications, please cite the following paper by the author:

@article{dinesh2025crop,
  title={Sustainable Crop Yield Forecasting Using Advanced Machine Learning Techniques Based on Comprehensive Analysis of Soil Health Parameters and Environmental Factors},
  author={Dinesh, T and Siva Balan, A},
  journal={International Journal of Advanced Engineering and Management},
  volume={1},
  number={1},
  pages={13},
  year={2025},
  doi={10.65379/tpsn2013/ijaemsv01i01p4}
}

DOI Link: https://doi.org/10.65379/tpsn2013/ijaemsv01i01p4


If this project helped you, please star the repository to support the work.
