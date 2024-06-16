import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)
import streamlit as st

# Title
st.title("Price Prediction on Gurgaon Flats and Properties Dataset")

# Introduction
st.header("Introduction")
st.write("""
The real estate market in Gurgaon, India, has experienced significant growth and transformation over the past few decades. With an increasing number of residential properties being developed, predicting property prices accurately has become crucial for buyers, sellers, and real estate investors. This project focuses on developing a price prediction model for Gurgaon flats and properties using a comprehensive dataset scraped from 99acres.com. The project encompasses various stages of a typical data science workflow, including data scraping, preprocessing, exploratory data analysis (EDA), feature engineering, model selection, model evaluation, and deployment using Streamlit.
""")

# Data Scraping
st.header("Data Scraping")
st.write("""
The first step in this project was to collect data from 99acres.com, a prominent real estate website. We used Python libraries such as `Requests` and `BeautifulSoup` for web scraping. The primary challenge encountered during this phase was the frequent blocking of our IP by 99acres.com due to the high number of requests. To overcome this, we implemented a strategy of fetching data in batches of 10 pages at a time, saving each batch into a DataFrame, and then merging these DataFrames to create the final dataset. The raw data obtained included various attributes such as sector name, facilities, area, super built-up area, built-up area, and property links.
""")

# Data Preprocessing
st.header("Data Preprocessing")
st.write("""
Data preprocessing is a critical step to ensure that the dataset is clean and suitable for analysis. The preprocessing steps included:
1. **Outlier Detection and Handling:** We identified outliers in the dataset by visual inspection and statistical methods. Outliers were then assessed to determine if they represented actual data points or anomalies, and necessary corrections were made.
2. **Handling Missing Values:** Missing values in the dataset were filled using appropriate techniques such as mean, median, or mode imputation.
3. **Feature Engineering:** The 'area' column was split into 'super built-up area' and 'built-up area.' Additionally, the facilities provided by the flats were rated according to their importance, and prices were converted into crores using a custom function named `lakh_to_crore`.
""")

# EDA
st.header("Exploratory Data Analysis (EDA)")
st.write("""
EDA was performed to understand the relationships between different features and the target variable (price). Key steps included:
1. **Correlation Analysis:** Using heatmaps to identify correlations between features and the target variable.
2. **Distribution Analysis:** Examining the distribution of numerical and categorical features.
3. **Pairwise Analysis:** Investigating the relationship between pairs of features.
4. **Pandas Profiling:** Generating a comprehensive report to summarize the dataset's characteristics.
""")

# Feature Engineering
st.header("Feature Engineering")
st.write("""
Feature engineering was applied to enhance the predictive power of the model. This involved:
1. **Transformation:** Converting skewed features to a normal distribution using logarithmic or square root transformations.
2. **Encoding:** Applying ordinal and nominal encoding to categorical variables.
3. **Scaling:** Standardizing numerical features using `StandardScaler` from scikit-learn.
""")

# Model Selection and Implementation
st.header("Model Selection and Implementation")
st.write("""
Various machine learning algorithms were explored for predicting property prices. The models considered included:
1. **Linear Regression**
2. **Random Forest Regressor**
3. **Gradient Boosting Regressor**
4. **AdaBoost Regressor**
5. **MLP Regressor**
6. **XGBoost Regressor**

We used scikit-learn's pipeline to streamline the preprocessing and modeling steps. Cross-validation was performed to evaluate the models' performance, and the Random Forest Regressor emerged as the best model with an R2 score of 0.900529 and an MSE of 0.4536.
""")

# Model Evaluation
st.header("Model Evaluation")
st.write("""
The performance of the selected model (Random Forest Regressor) was evaluated using metrics such as R2 score and Mean Squared Error (MSE). The high R2 score indicated that the model could explain 90% of the variance in the property prices, making it a reliable predictor.
""")

# Streamlit Deployment
st.header("Streamlit Deployment")
st.write("""
To make the model accessible and user-friendly, we deployed it using Streamlit, a popular open-source app framework for data science projects. The Streamlit app includes three main modules:
1. **Prediction Module:** Allows users to input property features and get price predictions.
2. **Data Visualization Module:** Provides visual insights into the dataset through charts and graphs.
3. **Recommender System Module:** Recommends properties based on user preferences.

The Streamlit app enhances user interaction and provides valuable insights, making it a practical tool for real estate stakeholders.
""")

# Conclusion
st.header("Conclusion")
st.write("""
This project demonstrates the application of data science techniques to predict real estate prices accurately. By leveraging data scraping, preprocessing, feature engineering, and advanced machine learning models, we developed a robust price prediction model for Gurgaon properties. The deployment of the model using Streamlit further adds value by making the tool accessible to end-users. While the model performs well, future work could involve incorporating more features, exploring additional algorithms, and enhancing the recommender system for better user experience.
""")

# References
st.header("References")
st.write("""
1. [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
2. [Streamlit Documentation](https://docs.streamlit.io/)
3. [99acres.com](https://www.99acres.com/)
""")

# Appendices
st.header("Appendices")
st.write("""
1. Github Repo Link for App: https://github.com/devrahul9119/Capstone-Project-App-Gurgaon-Properties-Dataset.git
2. Github Repo Link for Datasets : https://github.com/devrahul9119/Capstone-Project-on-Gurgaon-Flats-Dataset.git
""")

st.sidebar.title("Select a Webpage above.")