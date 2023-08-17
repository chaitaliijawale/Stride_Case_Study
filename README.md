# Optimizing Logistics Efficiency in Stride Case Study

## Introduction
A Stride Case Study," aims to analyze Stride Logistics' shipment data using advanced analytics tools and techniques. The project's objectives are to provide valuable insights and data-driven decision-making support, improve operational efficiency, and enhance customer satisfaction. By leveraging various data sources, including customer data, shipping data, and financial data, we will identify trends, patterns, and correlations to drive cost reduction, optimize logistics operations, and contribute to the long-term growth and success of Stride Logistics.

* Analyze Stride Logistics' shipment data using advanced analytics tools.
* Provide valuable insights and data-driven decision-making support.
* Improve operational efficiency and reduce costs in logistics operations.
* Enhance customer satisfaction through data-driven optimizations.

## Team Details
<img width="800" alt="image" src="https://github.com/chaitalijawale08/Stide_Case_Study/assets/100806411/6f18a277-23e8-4031-ad8f-20902da2af33">

## Problem Statement
The Stride logistics industry faces challenges in optimizing operational efficiency and enhancing customer satisfaction due to limited insights derived from shipment data.
### Why?
* Limited visibility into delivery time and customer rating for performance evaluation.
* Inefficient query response management impacting customer experience.
* Difficulty in determining the impact of product importance on delivery time and customer ratings.

### What we are trying to solve?
<img width="892" alt="image" src="https://github.com/chaitalijawale08/Stide_Case_Study/assets/100806411/f4a01d43-af31-44bc-acbc-85417d46cda6">

## Development Plan

#### Phase 1: Exploratory Data Analysis
- Understand data dictionaries to grasp the meaning and structure of the dataset.
- Perform data checks, such as checking for missing values, data types, and descriptive statistics of categorical and numerical columns.
- Conduct univariate analysis to explore the distribution of individual variables.
- Perform bivariate analysis to investigate relationships between different variables.
- Summarize the findings and present them in graphical representations.
  
#### Phase 2: Feature Engineering, Correlation Analysis, and Machine Learning Modeling
- Introduce new features that are relevant to the problem and dataset.
- Evaluate the correlation between the target variable and the newly introduced features to select the most impactful ones.
- Explore and select multiple machine learning models and identify the best fit model based on evaluation metrics.
- Analyze the relationships between these factors and timely deliveries to provide further recommendations. For instance, you may identify certain weight ranges that are more prone to delays and suggest possible improvements in packaging or shipping methods.
  
#### Phase 3: Application Development
- Develop a Python Flask web application to enable user interaction.
- Users can upload an Excel sheet containing their data to the app.
- The application will perform analytical and machine learning operations on the uploaded sheet.
- Provide insights through exploratory data analysis, machine learning model results, accuracy measures, and business recommendations for current and future scenarios.

## Installation
Clone the github repository and navigate to the terminal (make sure thay python 3.9.* is already installed)

```
pip install -r requirements.txt
```
```
set FLASK_APP=app:app
```
```
flask run
```

## Live WebApp
Link - https://meetvakani.wixsite.com/stride-project

## Exploratory Data Analysis
### Numerical Columns:
Prior Purchases and Discount Offered columns have minor skewness.
Cost of the Product column follows an almost normal distribution.
Customer ratings and customer care calls have a balanced distribution.
Weight in grams follows a u-shaped uncertain distribution.
Reached on Time column has a binary distribution.
### Categorical Columns:
Deliveries for Warehouse Block F have the highest number not delivered on time.
Shipments made by ships tend to run late.
Delivery delays are common for products with low and medium importance.
Female and male customers show similar delivery behavior.
### Bivariate Analysis:
Mode of Shipment:
Ship mode has the highest number of products not delivered on time.
Product Importance:
Deliveries are not on time for products of all importance levels, particularly high and low importance.
Warehouse Block:
Warehouse Block F has the highest number of products not delivered on time.
Weight Category:
Deliveries are generally on time for all weight categories except "wcat6" and "wcat7."
Discount Category:
The majority of products fall into "dcat1" with varied delivery results.

![image](https://github.com/chaitalijawale08/Stride_Case_Study/assets/100806411/6718c9ae-bcba-4aad-a22a-0b4f31757dfc)


## Feature Engineering(Total 20 features)
- Mode_of_Shipment_encoded: Encoded values of the "Mode_of_Shipment" column, mapping "Ship" to 1, "Flight" to 2, and "Road" to 3.
- Customer_rating_category: Categorization of customer ratings into 'VeryLow', 'Low', 'Average', 'Standard', and 'High' for analysis.
- Prior_purchases_category: Categorization of prior purchases into 'Very Low', 'Low', 'Medium', and 'High' to assess the impact of customer engagement.
- Product_importance_category: Retention of original product importance categories for analysis.
- Gender_encoded: Encoding of gender into numerical values (0 for Female, 1 for Male).
- Interaction_CustomerRating_Discount: Interaction between customer rating and discount offered.
- Interaction_CustomerCalls_Rating: Interaction between customer care calls and customer rating.
- Shipping_speed: Calculation of shipping speed based on product weight and customer care calls.
- Total_interactions: Sum of customer care calls and prior purchases to measure customer engagement.
- Expected_delivery_time: Calculation of expected delivery time based on mode of shipment.
- Product_importance_avg_delivery: Calculation of average delivery performance for each product importance category.
- ShippingMode_avg_delivery: Calculation of average delivery performance for each shipping mode.
- Interaction_Weight_Discount: Interaction between product weight and discount offered.
- High_product_importance_and_high_rating: Identification of high product importance with customer rating 5.
- Weight_category: Categorization of product weights into 'Light', 'Medium', and 'Heavy'.
- Discount_category: Categorization of discount percentages into 'Low', 'Medium', and 'High'.
- Product_Value: Calculation of product value based on cost and weight.
- Customer_Loyalty: Categorization of customer prior purchases into 'New', 'Regular', and 'Frequent'.
- Customer_Satisfaction_Score: Calculation of average score of customer rating and delivery time.
- Delivery_Time_per_Weight: Calculation of delivery time per weight of the product.

![image](https://github.com/chaitalijawale08/Stride_Case_Study/assets/100806411/b430043b-5c84-4636-acb1-711e967a8d1b)


## Machine Learning model
- Naive Bayes: A probabilistic classification algorithm based on Bayes' theorem, commonly used for text classification and problems with high-dimensional feature spaces.
- Logistic Regression: A widely used classification algorithm for binary classification problems, modeling the probability of a binary outcome by fitting a logistic function to input features.
- K-Nearest Neighbours (KNN): A non-parametric classification algorithm that classifies data points based on the majority class of their K nearest neighbors. Suitable for small to medium-sized datasets.
- Support Vector Machine (SVM): A powerful classification algorithm that finds an optimal hyperplane to separate data points of different classes, effective in high-dimensional spaces.
- Decision Tree: A tree-based classification algorithm that recursively splits the dataset based on features to create a tree-like structure. Prone to overfitting on deep trees.
- Random Forest: An ensemble learning method that builds multiple decision trees and combines their predictions for more accurate results. Reduces overfitting.
- XGBOOST (Extreme Gradient Boosting): A gradient boosting algorithm known for its high performance and efficiency, which optimizes a loss function to improve prediction accuracy.
![image](https://github.com/chaitalijawale08/Stride_Case_Study/assets/100806411/a69a9fc2-aaad-4755-92ba-b25928029781)

## Final result
1. Upload the csv
2. All data related operations will be performed including data preprocessing and ML.
3. Dashboard will be created with top features and model accuracy will be displayed
4. Questions will be answered by selecting the right model.
5. Recommendations will be displayed depending on the accuracy.

   https://github.com/chaitalijawale08/Stride_Case_Study/assets/100806411/80955409-3804-4b57-9ad7-94e32be115d4


## Conclusion
A Stride Case Study" project has been successfully completed, providing valuable insights to enhance Stride Logistics. By analyzing data, we answered crucial questions about delivery, customer satisfaction, and queries, offering practical recommendations that improved operations. Throughout the project, the collaboration between our team and Stride Logistics was evident, resulting in a well-structured journey of data exploration, modeling, and evaluation. The project's success showcases the impactful potential of data analytics and quality engineering management, guiding the logistics industry towards data-driven improvements.
