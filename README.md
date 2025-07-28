# Urban_Metro_Planning
Metro Line Prediction Using Machine Learning Model
This project, developed by Jaivardhan Tamminana and Soumesh Padhi under the supervision of Dr. Ebenezer Juliet S, aims to optimize urban metro planning by leveraging machine learning to address critical challenges such as traffic congestion and carbon emissions in rapidly urbanizing Indian cities. The core idea is to integrate data-driven insights with urban transportation planning to predict the need for new metro lines and expansions.

Project Overview
Rapid urbanization in India has intensified transportation challenges, leading to severe traffic congestion and increased carbon emissions. Traditional urban planning methods struggle to keep pace with these demands, highlighting the need for innovative solutions like metro rail systems. This project integrates advanced machine learning (ML) techniques into metro planning to analyze extensive datasets, predict future traffic dynamics, and optimize metro routes for sustainable urban development.


Motivation
The project is motivated by the urgent need to combat traffic congestion and carbon emissions in Indian cities. Metro rail systems offer a promising solution, but their planning is complex. By incorporating ML models, the project provides a cutting-edge approach to analyze vast datasets (traffic flow, carbon emission levels, passenger demand) and simulate various scenarios for data-driven decision-making, ensuring efficient and environmentally friendly urban transportation.

Scope
The project focuses on analyzing datasets including traffic density, vehicular emission statistics, and urban infrastructure details to strategically plan and expand metro lines across various districts in India. The ML model forecasts future transport demands and their environmental implications, trained on data from major cities like Chennai, Delhi, and Bangalore, which serve as ideal case studies due to their high urbanization and congestion issues. The goal is to create a scalable and replicable framework for metro planning.


Problem Statement
Current metro planning often overlooks district-level traffic patterns and emissions and underutilizes advanced machine learning for precise prediction. This project addresses these gaps by building an ML model that provides data-informed insights for metro line planning, coordinating infrastructure efficiency, and contributing to the reduction of traffic congestion and carbon emissions.

Features

Machine Learning Model Development: Develops an ML model that incorporates traffic congestion and carbon emission data to optimize metro line planning at a district level.

Predictive Accuracy: Achieves high predictive accuracy in forecasting traffic congestion and emission levels, validated using historical data from Chennai, Delhi, and Bangalore.

Data-Driven Insights: Utilizes diverse datasets including population density, environmental risks (earthquakes, floods, wind hazards), socio-economic influences, commute time, and transportation connectivity to inform planning decisions.

Scalable Framework: Designed to be a scalable and replicable framework adaptable for metro planning in various urban centers across India.

Interactive Interface: Includes functions for user input (get_input()) and prediction (predict()) to forecast metro line requirements based on specified features.

Comprehensive Data Processing: Features robust data cleaning, transformation, feature selection, and data augmentation techniques.

Technologies Used
The project leverages a range of programming languages, libraries, and tools:
Programming Languages: Python (primary) 

Machine Learning Frameworks:

Scikit-learn 
TensorFlow / PyTorch 
XGBoost / LightGBM 

Data Processing & Analysis:

Pandas 
NumPy 

Databases:
PostgreSQL / MySQL (for structured data) 

Web Scraping(Future feature): Selenium, Beautiful Soup, Scrapy 

Visualization: Matplotlib, Seaborn (implied by common ML practices)

Deployment: Flask (for web interface/API integration) 

Model Serialization: Pickle 

Installation
To set up the project locally, follow these steps:

Clone the repository:

Bash

git clone https://github.com/vardhannnn/Urban-Metro-Planning-using-Machine-Learning.git
cd Urban-Metro-Planning-using-Machine-Learning
Create a virtual environment (recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
Ensure you have all the necessary libraries installed. A requirements.txt file would typically list these. Based on the document, key libraries include:

Bash

pip install pandas numpy scikit-learn tensorflow xgboost matplotlib seaborn flask
(Note: Some specific database connectors or API keys might be required based on the actual implementation, which are not detailed in the report but are good to consider for a real project.)

Usage
The project involves data collection, pre-processing, model training, and prediction.

Data Collection and Pre-processing:

Gather relevant datasets from government sources, transport departments, and open datasets (traffic congestion, public transport, population, demographics, air quality, average trip time, commute length).

Clean data by handling missing values, removing outliers, and transforming data (e.g., normalization, feature selection).

Integrate merged datasets for analysis.

Model Training and Validation:

The model (Random Forest Classifier, which was identified as the best performing model ) is trained on historical data from cities like Chennai, Delhi, and Bangalore.

The model predicts metro ridership, traffic congestion, and air quality, with performance evaluated using metrics like accuracy, F1 score, and mean squared error.


Prediction:

The get_input() function takes user inputs for key features:

Risk of Natural Calamity: Low, Medium, or High (translated to 0, 1, or 2) 
Population: Total population of the district (numerical) 
Average Commute Time: In minutes (numerical) 
Average Trip Distance: In km (numerical) 
Airport Presence: Boolean (whether an airport is within 100 km) 

The predict() function processes these inputs using a pre-trained, calibrated Random Forest model to determine if a metro line is required in the specified district.

Example of how the model takes input (conceptual, exact implementation would depend on the Flask app):

Python

# Assuming a Flask API endpoint or direct function call
# Example of input data structure
input_data = {
    "natural_disaster_risk": "Medium", # or "Low", "High"
    "population": 1500000,
    "average_commute_time_minutes": 45,
    "average_trip_distance_km": 15,
    "airport_within_100km": True
}

# This would then be fed to the prediction function
# result = predict(input_data)
# print(result) # Output: "Metro line is required" or "Metro line is not required"

Contributions
Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, please consider:

Forking the repository.

Creating a new branch for your feature or fix (git checkout -b feature/YourFeatureName).

Making your changes and ensuring the code adheres to best practices.

Committing your changes (git commit -m 'Add new feature').

Pushing to the branch (git push origin feature/YourFeatureName).

Opening a Pull Request explaining your changes and their benefits.

📧 Contact
Created by Jaivardhan Tamminana.
Feel free to reach out at jaivardhan118@gmail.com
