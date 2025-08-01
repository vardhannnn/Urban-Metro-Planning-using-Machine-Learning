# Urban Metro Planning using Machine Learning

## Introduction
Metro rail systems are essential for reducing congestion, emissions, and commute time in rapidly growing urban centers. Yet, determining where and when to expand metro infrastructure in a diverse and densely populated country like India remains a complex challenge. Existing studies and planning models are often city-specific and lack generalizability across varied urban geographies. Traditional top-down methods also fail to account for local variations in demographics, environmental risk, and transport accessibility. This project addresses that gap by proposing a scalable, district-level predictive framework for metro expansion planning across India.

## Project Overview
This project presents a machine learning-based framework to identify metro-eligible districts using a curated dataset of 629 records that integrates demographic, environmental, mobility, and disaster risk indicators, primarily sourced from Census 2011 and related data from the 2010s. The model forecasts whether a district is likely to require metro infrastructure by 2025, supporting data-driven and equitable infrastructure development. Through systematic preprocessing, feature selection, and class imbalance handling, the model enables scenario-based simulation for planning under various urban growth and environmental conditions. While the framework shows strong predictive performance, it is limited by the recency and granularity of input data. Future iterations aim to incorporate real-time mobility and economic indicators to improve forecasting accuracy.
<p>Although the target variable is framed around metro presence in 2025, the model itself is not time-bound. It learns generalizable patterns between district-level characteristics and metro viability. This means that even if input data from upcoming sources like the 2021 Indian Census (which is expected to be collected around 2025) is provided, the model can assess whether a district warrants metro development based on those updated conditions. It does not predict whether a metro will exist by that year, but whether one is justified given the input indicators. This enables forward-looking infrastructure assessments using the most recent demographic, environmental, and mobility projections.

## Dataset Description
The predictive model was trained on a custom-compiled dataset representing 629 districts across India. The dataset integrates demographic, environmental, mobility, and infrastructure indicators to capture the complexity of metro planning at the district level. Data was primarily sourced from the Census of India 2011, environmental monitoring reports, and transport-related open data from the 2010s.<p>
The final dataset included the following features:
<ol>
    <li>Population
    <li>Decadal Growth Rate
    <li>Average Commute Time
    <li>Average Trip Length
    <li>Air Quality Index (AQI)
    <li>Number of Households
    <li>Natural Calamity Risk
    <li>Airport Proximity
    <li>Current Infrastructure Adequacy
    <li>Metro Infrastructure Presence (Target Variable)
</ol>
We engineered <strong>Population Density</strong> due to the high correlation between Population and Number of Households. All features were preprocessed to address missing values, standardize scales, and encode categorical variables. Feature engineering and region-based imputation were applied where necessary. To address class imbalance in the target variable, the positive class (districts likely to receive metro infrastructure) was first augmented with controlled noise. After the dataset was split into training and testing subsets, SMOTETomek was applied to the training set to further balance the classes and remove borderline noise, improving the model’s ability to learn from minority cases.
<br>You can access the dataset <a href="https://github.com/vardhannnn/Urban-Metro-Planning-using-Machine-Learning/tree/main/Dataset%20of%20the%20Project">here</a>

## Methodology
The model development process followed a structured pipeline, from data preparation to evaluation:
<ol>
    <li><strong>Data Preparation</strong><br>A custom dataset of 629 Indian districts was compiled using publicly available sources such as Census 2011, AQI reports, disaster risk records, and government infrastructure data. For features not readily available in structured form, such as proximity to the nearest operational airport, manual searches using Google Maps were conducted to estimate distances from each district's administrative center. Missing values were handled using domain-aware imputations, and outliers were capped using interquartile range thresholds. <p>
    <li><strong>Data Preprocessing</strong><br>Initial formatting involved converting numeric values stored as strings (e.g., "1,234") into proper numerical types by removing commas. District name columns were dropped as they served only as identifiers. No missing values were found in the final dataset.
Categorical features such as disaster risk, infrastructure adequacy, and airport connectivity were encoded using integer and Boolean mappings based on their ordinal or binary nature. Standard scaling using StandardScaler was applied to the entire dataset only during SVM-based feature selection. During model training, standard scaling was also applied on the subset of features selected by each model, even in cases where it was not strictly required (e.g., tree-based models), to maintain uniformity in the training process.<p>
    <li><strong>Exploratory Data Analysis (EDA)</strong><br>EDA was conducted to understand feature behavior and guide preprocessing decisions. A correlation matrix was used to identify multicollinearity, revealing that the number of households was highly correlated with population and, therefore, dropped to avoid redundancy. The class distribution of the target variable was also analyzed, revealing a significant imbalance between metro and non-metro districts, which informed augmentation and sampling strategies. Visual inspection of feature values helped validate input ranges and led to necessary conversions, including encoding of categorical attributes and standardization of continuous ones. Additionally, a new feature, Population Density, was engineered from population and land area to better capture urban compactness.<p>
    <li><strong>Data Augmentation</strong><br>The original dataset had only 114 positive samples (districts with metro presence by 2025), making it significantly imbalanced when compared to 515 negative samples (districts with no metro presence by 2025). To address this, the positive class was first augmented by duplicating and perturbing the 114 “Yes” samples. For each numeric feature, small random noise (ranging from –30 to +50) was added using a uniform distribution to create variation. This effectively doubled the positive class to 228 entries before splitting the dataset.<p>
    <li><strong>Feature Selection</strong><br>Recursive Feature Elimination with Cross-Validation (RFECV) was used to rank features for each model individually, using the same algorithm as the model being trained, for instance, XGBoost as estimator for XGBoost, Random Forest for RFC. While RFECV provided model-specific feature rankings, the final selection was manually capped at the top five features to ensure consistency across models, improve interpretability, and avoid overfitting.<p>
    <li><strong>Model Training</strong><br>Each model followed an independent training pipeline. After feature selection, the selected features were used to create model-specific training and testing splits, utilizing stratified sampling to maintain class balance. Standard scaling was applied only to the selected features, and SMOTETomek was used for class balancing. In addition, Gaussian noise was added to the resampled data to increase variation and reduce overfitting. For each model, hyperparameters were optimized using RandomizedSearchCV with 5-fold stratified cross-validation, maximizing F1-score. The best model from each search was then calibrated using CalibratedClassifierCV to improve probability estimates. Finally, threshold tuning was carried out by evaluating model performance across probability thresholds from 0.30 to 0.70, selecting the cutoff that maximized the F1-score for predicting metro-ready districts.<p>
    <li><strong>Model Evaluation</strong><br>The model performance was evaluated using:
        <ul>
            <li>Precision, Recall, and F1-Score across a threshold range
            <li>Confusion Matrix
            <li>Classification Report
            <li>Precision-Recall Curve (preferred over ROC due to class imbalance)
        </ul>
</ol>

## Why We Chose Random Forest as the Final Model
Our objective was to recommend districts that genuinely require metro infrastructure while avoiding unnecessary expansion. For this reason, the F1-score for the metro-eligible ("Yes") class was the most important evaluation metric. It captures a balance between:
<ul>
    <li>Precision, which reduces false positives and avoids suggesting unsuitable districts
    <li>Recall, which ensures that districts in need are not overlooked
</ul>
While several models performed competitively, Random Forest provided the most balanced results. It achieved:
<ul>
    <li>The highest F1-score (68.70) for metro-eligible districts
    <li>Strong precision (72.58%), indicating reliable suggestions
    <li>Solid recall (65.22%), reducing the chance of missing key areas
    <li>The highest overall accuracy (81.61%) among all models
</ul>
These results made Random Forest the most appropriate model for supporting fair, data-driven, and sustainable metro planning across Indian cities.
<br>You can access the classification reports <a href="https://github.com/vardhannnn/Urban-Metro-Planning-using-Machine-Learning/tree/main/Diagrams/Classification%20Reports">here</a>

## Scenario Simulation
To test the model’s responsiveness to future developments and localized changes, we performed controlled “what-if” simulations by adjusting specific input features. These simulations aimed to assess how shifts in urban conditions would impact metro eligibility predictions. The scenarios included:
<ul>
    <li>Projected population growth in high-density districts
    <li>Improvements in air quality index (AQI) due to green policies
    <li>Planned upgrades to infrastructure, such as better airport connectivity or disaster preparedness
</ul>
For example, increasing the projected population and upgrading infrastructure in a Tier-2 district shifted its prediction from "No" to "Yes," suggesting the model’s sensitivity to future urban transformation.

These simulations demonstrated that the model is not only predictive but also adaptable, and can be used to inform sustainable and forward-looking metro planning.

## Limitations
While the project presents a novel and practical framework for metro infrastructure planning, several limitations should be acknowledged:
<ol>
    <li><strong>Feature assumptions: </strong>The features used were selected based on our understanding of metro planning, but they may not perfectly align with the criteria used by government planners or transport authorities.<p>
    <li><strong>Outdated Input Data: </strong>The primary features were derived from the 2011 Census and related datasets from the early 2010s. Although the model can accept newer inputs (such as the upcoming 2021 Census), its training was based on older patterns, which may not fully reflect recent urban developments.<p>
    <li><strong>Manual Data Sourcing: </strong>Features such as proximity to metro stations and airports were added through manual search instead of structured geospatial APIs. This limits automation and scalability.<p>
    <li><strong>Limited Feature Set: </strong>The model was built using only 10 features, out of which the top 5 were selected through feature selection methods. These may not represent the full range of factors typically considered in metro planning, such as land acquisition complexity, underground feasibility, or detailed financial and policy evaluations.<p>
    <li><strong>No Policy Modeling: </strong>The model does not incorporate state-wise government policies, budget constraints, or political factors. It is meant to offer a data-driven recommendation, but the final decision on metro construction depends on state and central authorities.<p>
    <li><strong>Deployment Incomplete: </strong>A Flask frontend was developed separately but remains unconnected to the model. The prediction system currently runs only through a command-line interface.
</ol>

## Future Work
The current framework offers a strong foundation, but there are several directions in which the project can be expanded, both in terms of technical sophistication and real-world applicability:
<ul>
    <li><strong>Feature Expansion: </strong>Introduce additional parameters such as projected economic growth, inter-modal transport accessibility, land availability, and environmental stress indicators using structured and scalable data sources.<p>
    <li><strong>Automated Feature Retrieval: </strong>Replace manual geographic lookups with APIs (such as Google Maps or OpenStreetMap) to automatically extract features like distance to airports or metro lines for any district.<p>
    <li><strong>Full Web Development: </strong>Complete and connect the Flask-based frontend for real-time metro eligibility predictions, allowing stakeholders to interact with the model via a user-friendly web interface.<p>
    <li><strong>Prediction Horizon Estimation: </strong>Extend the current binary classification model into a multi-class or regression-based system that can estimate the likely timeframe (e.g., by 2030, 2040, etc.) in which a district would benefit from metro development.
    <li><strong>Model Experimentation: </strong>Explore alternative algorithms, including neural networks and graph-based models, to better capture spatial or network-based relationships between urban centers and transit needs.
</ul>

## Technologies Used
The project leverages a range of programming languages, libraries, and tools:
<ol>
    <li>Programming Language:
        <ul>
            <li>Python
        </ul>
    <li>Machine Learning Frameworks:
        <ul>
            <li>Scikit-learn
            <li>XGBoost
        </ul>
    <li>Data Processing and Analysis:
        <ul>
            <li>Pandas
            <li>NumPy
            <li>Microsoft Excel
        </ul>
    <li>Model Selection and Hyperparameter Tuning:
        <ul>
            <li>RandomizedSearchCV
            <li>StratifiedKFold
            <li>Train-Test Split
        </ul>
    <li>Class Imbalance Handling:
        <ul>
            <li>Imbalanced-learn
        </ul>
    <li>Model Calibration and Feature Selection:
        <ul>
            <li>RFECV
            <li>CalibratedClassifierCV
        </ul>
    <li>Visualization:
        <ul>
            <li>Matplotlib
            <li>Seaborn
        </ul>
    <li>Model Evaluation:
        <ul>
            <li>Precision-Recall Curve
            <li>Confusion Matrix
            <li>Classification Report
        </ul>
    <li>Deployment:
        <ul>
            <li>Flask
        </ul>
    <li>Model Serialization:
        <ul>
            <li>Pickle
        </ul>
</ol>
        
## How to Use
You can interact with the model by running the notebook in Google Colab or executing the script locally via the command line.<br>
Option 1: Run on Colab
<ol>
    <li>Click on <a href= "https://github.com/vardhannnn/Urban-Metro-Planning-using-Machine-Learning/blob/main/Code%20File/Capstone.ipynb">link</a> to head to the colab notebook.
    <li>Run the code cells sequentially.
    <li>When prompted, enter the following inputs:
        <ul>
            <li>Risk of Calamity
            <li>Population
            <li>Average Commute Time (in minutes)
            <li>Average Trip Distance (in kilometers)
            <li>Airport within 100 kms
        </ul>
    <li>The model will return whether the district is likely to require a metro or not.
</ol>
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

## Contributors:
<a href="https://github.com/vardhannnn">Jaivardhan Tamminana</a>
<strong> • </strong>
<a href="https://github.com/cypher-sp">Soumesh Padhi</a>
<strong> • </strong>
<a href="https://github.com/vino-ppa">Vinothkumar Palaniappan</a>
<p>
To find the individual contributions of each person, click on the following link: <a href= "https://github.com/vardhannnn/Urban-Metro-Planning-using-Machine-Learning/tree/main/Project%20Contribution">Contributions</a> <p>

<p>
<strong>Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, please consider:
<ol>
<li>Forking the repository.
<li>Creating a new branch for your feature or fix (git checkout -b feature/YourFeatureName).
<li>Making your changes and ensuring the code adheres to best practices.
<li>Committing your changes (git commit -m 'Add new feature').
<li>Pushing to the branch (git push origin feature/YourFeatureName).
<li>Opening a Pull Request explaining your changes and their benefits.
</ol>
</strong>
<p>
Feel free to reach out to Jaivardhan Tamminana via 📧<strong>jaivardhantamminana@outlook.com</strong> for explanations and ideas around the models.

---

## License
This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License.  
You are free to use the materials for educational and research purposes, with **proper attribution**, but **commercial use is prohibited**.

🔗 https://creativecommons.org/licenses/by-nc/4.0/

---

⚠️ **Code Use Policy**

This project is provided **for academic reference and public understanding**.  
Reusing this code or its components in **college coursework, academic submissions, or commercial work without explicit credit and permission is prohibited**.

Unauthorized reuse may be considered a **violation of academic integrity policies** and may be reported to institutions or taken down under GitHub's **DMCA** guidelines.
