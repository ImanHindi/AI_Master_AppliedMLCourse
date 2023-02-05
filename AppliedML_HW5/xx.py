import tensorflow as tf
from tensorflow import keras
from keras import layers,utils
# Build the model
input_wide = layers.Input(shape=[5]) # features 0 to 4
input_deep = layers.Input(shape=[6]) # features 2 to 7
norm_layer_wide = layers.Normalization()
norm_layer_deep = layers.Normalization()
norm_wide = norm_layer_wide(input_wide)
norm_deep = norm_layer_deep(input_deep)
hidden1 = layers.Dense(30, activation="relu")(norm_deep)
hidden2 = layers.Dense(30, activation="relu")(hidden1)
concat = layers.concatenate([norm_wide, hidden2])
output = layers.Dense(1)(concat)
aux_output = layers.Dense(1)(hidden2)

model = keras.Model(inputs=[input_wide, input_deep],
outputs=[output, aux_output])

model = keras.Sequential([
layers.Flatten(input_shape=[28, 28]),
layers.Dense(300, activation="relu"),
layers.Dense(100, activation="relu"),
layers.Dense(10, activation="softmax")
])

keras.utils.plot_model(
model,
"my_model.png",
show_shapes=True)

