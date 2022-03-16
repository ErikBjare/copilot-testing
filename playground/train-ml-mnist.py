# from io import BytesIO
import struct
import gzip

import requests

# download mnist.gz dataset to mnist.gz
url = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
r = requests.get(url)

with open("mnist.gz", "wb") as f:
    f.write(r.content)

# extract
with gzip.open("mnist.gz", "rb") as f:
    with open("mnist.bin", "wb") as f2:
        f2.write(f.read())

# load mnist.bin
with open("mnist.bin", "rb") as f:
    magic, n, rows, cols = struct.unpack(">IIII", f.read(16))
    print(magic, n, rows, cols)
    data = f.read()


# convert to numpy array
import numpy as np

data = np.frombuffer(data, dtype=np.uint8)
data = data.reshape(-1, 28 * 28)

# import keras stuff
from keras.models import Sequential
from keras.layers import Dense, Activation

# set up the model
model = Sequential()
model.add(Dense(units=64, input_dim=784))
model.add(Activation("relu"))
model.add(Dense(units=10))
model.add(Activation("softmax"))

# train the model
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
model.fit(
    data,
    np.eye(10)[np.random.randint(0, 10, size=data.shape[0])],
    epochs=10,
    batch_size=32,
)

# evaluate the model
score = model.evaluate(
    data, np.eye(10)[np.random.randint(0, 10, size=data.shape[0])], batch_size=32
)
print(score)
