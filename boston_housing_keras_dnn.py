import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import boston_housing as bh
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from tqdm.keras import TqdmCallback
from tensorflow.keras.callbacks import ModelCheckpoint
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px

''' Global Configuration Settings '''

class CFG:
    
    def __init__(self):
        self.n_epochs = 200
        self.lr = 0.01
        self.batch_size = 64
        self.seed = 221

cfg = CFG()

''' Data Split '''

# Split dataset into training and test sets
(X_train, y_train), (X_test, y_test) = bh.load_data(path='boston_housing.npz',
                                                    test_split=0.2,
                                                    seed=113)

# Split test data into validation dataset and test dataset
X_valid, X_test, y_valid, y_test = tts(X_test,y_test,
                                       test_size = 0.4,
                                       random_state = cfg.seed)

print('Dataset Splitting:')
print(f'Training Data Shape: {X_train.shape}')
print(f'Validation Data Shape: {X_valid.shape}')
print(f'Test Data Shape: {X_test.shape}')

''' Neural Network '''

class nn(keras.Model):
    
    def __init__(self, dropout = 0.1):
        super().__init__()
        
        self.input_layer = keras.Sequential([
            #layers.BatchNormalization(input_shape = [13]),
            layers.Dense(32, 
                         input_shape = [13]),
            layers.Activation('relu'),
            layers.Dropout(dropout),
            layers.BatchNormalization()
        ])
        
        self.h1 = keras.Sequential([
            layers.Dense(64),
            layers.Activation('relu'),
            layers.Dropout(dropout),
            layers.BatchNormalization()
        ])
        
        self.h2 = keras.Sequential([
            layers.Dense(32),
            layers.Activation('relu'),
            layers.Dropout(dropout),
            layers.BatchNormalization()
        ])
        
        self.output_layer = keras.Sequential([
            layers.Dense(1)
        ])
        
    def call(self, x, training = False):
        x = self.input_layer(x)
        x = self.h1(x)
        x = self.h2(x)
        return self.output_layer(x)
    
''' Compile Neural Network '''
    
# Instantiate Neural Network
model = nn()

# define loss function & optimiser

model.compile(optimizer = keras.optimizers.Adam(learning_rate = cfg.lr), 
              loss = keras.losses.MeanSquaredError(),
              metrics = ['mse'])

''' Train Neural Network '''

# Callbacks during training

checkpoint = ModelCheckpoint(filepath='/kaggle/working/net.ckpt',
                             monitor='val_loss',
                             mode='min',
                             save_best_only=True)

callbacks = [checkpoint,
             TqdmCallback(verbose=0)] 
             
# Train Model 

history = model.fit(
    X_train, y_train,                     # Training Data
    validation_data = (X_valid, y_valid), # Validation data 
    batch_size = cfg.batch_size,          # Batch Size each epoch
    epochs = cfg.n_epochs,                # Number of iterations
    verbose=0,                            # silent output
    callbacks = callbacks                 # callbacks during training
)

# Plot Training Data

plot_keras_metric(history,['mse'],        # list all metrics
                  show_loss=True,         # show loss functions
                  type_id = 'line',
                  fsize=[400,1000],
                  vwindow = [0,200])
