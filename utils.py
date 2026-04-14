import tensorflow as tf

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

def load_data(train_dir, valid_dir):
    train = tf.keras.preprocessing.image_dataset_from_directory(
        train_dir,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    val = tf.keras.preprocessing.image_dataset_from_directory(
        valid_dir,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    normalization = tf.keras.layers.Rescaling(1./255)

    train = train.map(lambda x, y: (normalization(x), y))
    val = val.map(lambda x, y: (normalization(x), y))

    return train, val