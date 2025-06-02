import ssl

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

ssl._create_default_https_context = ssl._create_unverified_context


def load_and_preprocess_data():

    (x_train, y_train), (x_test, y_test) = mnist.load_data()


    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0


    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    return (x_train, y_train), (x_test, y_test)


def build_model():
    model = models.Sequential([
        layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(100, activation='relu'),
        layers.Dense(10, activation='softmax')  # 输出10类
    ])
    return model


def train_and_evaluate():
    (x_train, y_train), (x_test, y_test) = load_and_preprocess_data()

    model = build_model()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=10, batch_size=64, verbose=2)


    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test accuracy: {test_acc:.4f}")


    model.save("mnist_model.h5")


if __name__ == "__main__":
    train_and_evaluate()
