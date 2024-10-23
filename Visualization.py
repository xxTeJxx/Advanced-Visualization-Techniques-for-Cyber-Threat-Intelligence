# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from google.colab import drive
import os

drive.mount('/content/drive')

folder_path = '/content/drive/My Drive/CSE-CIC-IDS2018/'

parquet_files = [
    'Web2-Friday-23-02-2018_TrafficForML_CICFlowMeter.parquet',
    'Web1-Thursday-22-02-2018_TrafficForML_CICFlowMeter.parquet',
    'Infil2-Thursday-01-03-2018_TrafficForML_CICFlowMeter.parquet',
    'Infil1-Wednesday-28-02-2018_TrafficForML_CICFlowMeter.parquet',
    'DoS2-Friday-16-02-2018_TrafficForML_CICFlowMeter.parquet',
    'DoS1-Thursday-15-02-2018_TrafficForML_CICFlowMeter.parquet',
    'DDoS2-Wednesday-21-02-2018_TrafficForML_CICFlowMeter.parquet',
    'DDoS1-Tuesday-20-02-2018_TrafficForML_CICFlowMeter.parquet',
    'Bruteforce-Wednesday-14-02-2018_TrafficForML_CICFlowMeter.parquet',
    'Botnet-Friday-02-03-2018_TrafficForML_CICFlowMeter.parquet'
]

dataframes = [pd.read_parquet(os.path.join(folder_path, file)) for file in parquet_files]
complete_data = pd.concat(dataframes, ignore_index=True)

print("First few rows of the dataset:")
print(complete_data.head())
print("\nDescriptive Statistics:")
print(complete_data.describe())
print("\nColumn Names:")
print(complete_data.columns)

sns.set(style='whitegrid')

# Check the data types of each column
print(complete_data.dtypes)


plt.figure(figsize=(10, 6))
sns.histplot(complete_data['Flow Duration'], bins=30, kde=True)
plt.title('Distribution of Flow Duration', fontsize=16)
plt.xlabel('Flow Duration (in microseconds)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=complete_data, x='Label', order=complete_data['Label'].value_counts().index, palette='viridis')
plt.title('Distribution of Attack Types', fontsize=16)
plt.xlabel('Attack Type', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.show()

print("Data Types of Each Column:")
print(complete_data.dtypes)

label_encoder = LabelEncoder()
complete_data['Label'] = label_encoder.fit_transform(complete_data['Label'])

print("Unique Values After Encoding:")
print(complete_data['Label'].unique())


label_mapping = {
    0: 'Benign',
    1: 'DoS',
    2: 'DDoS',
    3: 'Port Scan',
    4: 'Brute Force',
    5: 'Botnet',
    6: 'Infiltration',
    7: 'Web Attack',
    8: 'SQL Injection',
    9: 'XSS',
    10: 'Malicious File',
    11: 'DDOS Attack',
    12: 'Password Guessing',
    13: 'Information Theft',
    14: 'Other Attacks'
}

complete_data['Label'] = complete_data['Label'].map(label_mapping)


plt.figure(figsize=(12, 6))
sns.countplot(data=complete_data, x='Label', palette='viridis')
plt.title('Distribution of Attack Types', fontsize=20)
plt.xlabel('Attack Type', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='Label', y='Flow Duration', data=complete_data, palette='Set2')
plt.title('Flow Duration by Attack Type', fontsize=20)
plt.xlabel('Attack Type', fontsize=14)
plt.ylabel('Flow Duration (in microseconds)', fontsize=14)
plt.xticks(rotation=45)
plt.show()

sample_data = complete_data.sample(frac=0.1)  # Adjust the fraction as needed


plt.figure(figsize=(12, 12))
sns.pairplot(sample_data[['Flow Duration', 'Total Fwd Packets', 'Flow Bytes/s', 'Label']],
             hue='Label', diag_kind='kde', height=2.5)
plt.suptitle('Pairplot of Selected Features (Sample)', y=1.02)
plt.show()



numeric_data = complete_data.select_dtypes(include='number')


top_features = numeric_data.corr().nlargest(10, 'Flow Duration').index


plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data[top_features].corr(), annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Top Feature Correlations', fontsize=20)
plt.show()



plt.figure(figsize=(14, 6))
plt.plot(complete_data['Flow Duration'], label='Flow Duration', color='b')
plt.title('Flow Duration Over Time', fontsize=20)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Flow Duration', fontsize=14)
plt.legend()
plt.show()


