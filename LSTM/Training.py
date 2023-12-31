import pandas as pd
import holidays
import sklearn
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, LSTM
import joblib
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import random
import holidays
import warnings

# Filter out unnecessary warnings
warnings.filterwarnings("ignore")

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)
random.seed(42)

def inverse_scale_single_array(scaler,single_array):
    """
    Inverse scales a single array using the provided scaler.
    
    Parameters:
    - scaler: The scaler object used for inverse scaling.
    - single_array: The array to be inverse scaled.
    
    Returns:
    - The inversely scaled array.
    """
    # scaler = joblib.load('data_scaler.pkl')
    reshaped_array = np.array(single_array).reshape(-1, 1)
    zeros = np.zeros((reshaped_array.shape[0], 2))
    combined_data = np.hstack((reshaped_array, zeros))
    actual_pred=scaler.inverse_transform(combined_data)
    return actual_pred[:,0]

def create_sequence_data(data, sequence_len):
    """
    Creates sequences of given length from the data for LSTM models.
    
    Parameters:
    - data: Input data array.
    - sequence_len: Length of sequences to be generated.
    
    Returns:
    - x: Feature sequences.
    - y: Target values for each sequence.
    """
    x,y=[],[] 
    for i in range(len(data[:,1])-sequence_len):
        x.append(data[i:i+sequence_len])
        y.append(data[:,0][i+sequence_len])
    return np.asarray(x), np.asarray(y)

def data_processing(data,sequence_length):
    """
    Processes the input data by adding features, scaling, and splitting.
    
    Parameters:
    - data: The input data DataFrame.
    - sequence_length: The length of sequences to be generated.
    
    Returns:
    - x_train, y_train: Training data sequences and targets.
    - x_test, y_test: Testing data sequences and targets.
    """
    df=data
    df['Date']=pd.to_datetime(df['Date'])
    df['Holidays']=df['Date'].apply(lambda x:x in holidays.US()).astype(int)
    df['days']=df['Date'].dt.weekday

    df.drop(columns=['Date','Product ID'],axis=1,inplace=True)
    data_scaler=sklearn.preprocessing.MinMaxScaler()
    df=data_scaler.fit_transform(df)
    df=data_scaler.inverse_transform(df)
    joblib.dump(data_scaler, 'data_scaler.pkl')

    train, test=train_test_split(df,test_size=0.2, shuffle=False,random_state=42)
    x_train , y_train=create_sequence_data(train,sequence_length)
    x_test , y_test=create_sequence_data(test,sequence_length)
    return x_train, y_train, x_test, y_test

def training1(data,sequence_length):
    """
    Processes the data and trains an LSTM model using MAE as the loss function.
    
    Parameters:
    - data: The input data DataFrame.
    - sequence_length: The length of sequences to be generated.
    
    Returns:
    - The trained LSTM model.
    """

    x_train, y_train, x_test, y_test=data_processing(data, sequence_length)

    EarlyStopping_1=tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=8)
    model_product1=Sequential([
        LSTM(50,activation='relu',return_sequences=True, input_shape=(x_train.shape[1],x_train.shape[2])),
        LSTM(128,activation='relu'),
        Dense(1)
    ])
    model_product1.compile(optimizer='adam',loss='mae')

    history=model_product1.fit(x_train,y_train,epochs=200,validation_data=(x_test,y_test),callbacks=[EarlyStopping_1],verbose=0)
    # Convert the history to a DataFrame
    df = pd.DataFrame(history.history)
    # Save the DataFrame to CSV
    df.to_csv('training_history.csv', index=False)
    return model_product1


sequence_length=1
# Define data file paths
data1="AA_Batteries_60Days_Data.csv"
data2="AAA_Batteries_60Days_Data.csv"
# Read data from CSV files
df1=pd.read_csv(data1)
df2=pd.read_csv(data2)
# Train the LSTM model for the first product
model_product1 =training1(df1,sequence_length)
# Save the trained model for the first product
model_product1.save('model_product1.keras')
# Train the LSTM model for the second product
model_product2=training1(df2,sequence_length)
# Save the trained model for the second product
model_product2.save('model_product2.keras')
