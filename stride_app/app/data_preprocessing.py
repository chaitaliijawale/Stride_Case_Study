import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler #scaling 
import logging

def load_data(file_path):
    df = pd.read_csv(file_path)
    print('Given dataset is loaded.')
    return df

def perform_feature_engineering(df):
    mode_mapping = {'Ship': 1, 'Flight': 2, 'Road': 3}
    df['Mode_of_Shipment_encoded'] = df['Mode_of_Shipment'].map(mode_mapping)

    rating_mapping = {1: 'VeryLow', 2: 'Low', 3: 'Average', 4: 'Standard', 5: 'High'}
    df['Customer_rating_category'] = df['Customer_rating'].map(lambda x: rating_mapping[x])

    df['Customer_rating_category'] = pd.Categorical(df['Customer_rating_category'], categories=['VeryLow', 'Low', 'Average','Standard', 'High'], ordered=True)

    df['Prior_purchases_category'] = pd.cut(df['Prior_purchases'], bins=[-1, 2, 5, 10, np.inf], labels=['Very Low', 'Low', 'Medium', 'High'])

    df['Gender_encoded'] = df['Gender'].map({'F': 0, 'M': 1})

    df['Interaction_CustomerRating_Discount'] = df['Customer_rating'] * df['Discount_offered']

    df['Interaction_CustomerCalls_Rating'] = df['Customer_care_calls'] * df['Customer_rating']

    df['Shipping_speed'] = df['Weight_in_gms'] / df['Customer_care_calls']

    df['Total_interactions'] = df['Customer_care_calls'] + df['Prior_purchases']

    expected_delivery_time = {'Ship': 4, 'Flight': 2, 'Road': 6}  # Assuming days
    df['Expected_delivery_time'] = df['Mode_of_Shipment'].map(expected_delivery_time)
    df['CustomerCare_vs_ExpectedTime'] = df['Customer_care_calls'] - df['Expected_delivery_time']


    product_importance_avg_delivery = df.groupby('Product_importance')['Reached.on.Time_Y.N'].mean().reset_index()
    product_importance_avg_delivery.columns = ['Product_importance', 'ProductImportance_avg_delivery']
    df = df.merge(product_importance_avg_delivery, on='Product_importance', how='left')

    shipping_mode_avg_delivery = df.groupby('Mode_of_Shipment')['Reached.on.Time_Y.N'].mean().reset_index()
    shipping_mode_avg_delivery.columns = ['Mode_of_Shipment', 'ShippingMode_avg_delivery']
    df = df.merge(shipping_mode_avg_delivery, on='Mode_of_Shipment', how='left')

    df['Interaction_Weight_Discount'] = df['Weight_in_gms'] * df['Discount_offered']

    df['Customer_rating_and_delivery_time'] = df['Customer_rating'] * df['Reached.on.Time_Y.N']
    df['Product_importance_and_delivery_time'] = df['Product_importance'] * df['Reached.on.Time_Y.N']
    df['High_product_importance_and_high_rating'] = ((df['Product_importance'] == 'high') & (df['Customer_rating'] == 5)).astype(int)

    weight_bins = [0, 2000, 4000, float('inf')]
    weight_labels = ['Light', 'Medium', 'Heavy']
    df['Weight_category'] = pd.cut(df['Weight_in_gms'], bins=weight_bins, labels=weight_labels)

    discount_bins = [0, 10, 30, 100]
    discount_labels = ['Low', 'Medium', 'High']
    df['Discount_category'] = pd.cut(df['Discount_offered'], bins=discount_bins, labels=discount_labels)

    df['Product_Value'] = df['Cost_of_the_Product'] * df['Weight_in_gms']

    customer_loyalty_bins = [0, 2, 5, np.inf]
    customer_loyalty_labels = ['New', 'Regular', 'Frequent']
    df['Customer_Loyalty'] = pd.cut(df['Prior_purchases'], bins=customer_loyalty_bins, labels=customer_loyalty_labels)

    df['Customer_Satisfaction_Score'] = (df['Customer_rating'] + df['Reached.on.Time_Y.N']) / 2

    df['Delivery_Time_per_Weight'] = df['Weight_in_gms'] / df['Expected_delivery_time']

    print("Feature Engineering is done.")
    return df


def encode_categorical_columns(dataframe):
    df = dataframe.copy()
    label_encoder = LabelEncoder()
    encoded_columns = []
    for column in df.columns:
        if df[column].dtype != 'int64' and 'float64':
            df[column + '_encoded'] = label_encoder.fit_transform(df[column])
            encoded_columns.append(column + '_encoded')
            df.drop(column, axis=1, inplace=True)
    
    print("Data Encoding is done.")
    return df, encoded_columns


def scale_dataframe(df, columns_to_exclude=[]):
    if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("All columns should be numerical for scaling.")
    print('The variable, name is of type:', type(df))
    scaler = StandardScaler()
    df_to_scale = df.drop(columns=columns_to_exclude)
    scaled_df = pd.DataFrame(scaler.fit_transform(df_to_scale), columns=df_to_scale.columns)
    for col in columns_to_exclude:
        scaled_df[col] = df[col]
    print("Data Scaling is done.")
    return scaled_df

def perform_data_preprocessing(df):
    df = scale_dataframe(df, columns_to_exclude=['Reached.on.Time_Y.N'])
    print("Data preprocessing steps are done.")
    return df


def run_data_preprocessing(file_path):
    df = load_data(file_path)
    print("Performing Feature Engineering..")
    fearure_df = perform_feature_engineering(df)
    print("Performing Data Encoding..")
    final_encoded_df, encoded_columns = encode_categorical_columns(fearure_df)
    print("This many columns are Encoded -> :", encoded_columns)
    print("Performing Data Scaling..")
    df = perform_data_preprocessing(final_encoded_df)
    return df
