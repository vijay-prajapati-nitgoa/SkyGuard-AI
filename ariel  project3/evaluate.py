from sklearn.metrics import classification_report
import tensorflow as tf

model = tf.keras.models.load_model("models/transfer_model.h5")

test = tf.keras.preprocessing.image_dataset_from_directory(
    "test",
    image_size=(224,224),
    batch_size=32
)

y_true = []
y_pred = []

for x, y in test:
    preds = model.predict(x)
    y_true.extend(y.numpy())
    y_pred.extend((preds > 0.5).astype(int))

print(classification_report(y_true, y_pred))