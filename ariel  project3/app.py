import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("models/transfer_model.h5")

st.title("🛰️ Aerial Object Classification System")
st.write("Upload image → Bird or Drone")

file = st.file_uploader("Upload Image", type=["jpg","png"])

if file:
    image = Image.open(file).convert("RGB").resize((224,224))
    st.image(image)

    img = np.array(image)/255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]

    #  Now inside block
    if pred > 0.5:
        st.success(f"🚁 Drone ({pred:.2f})")
    else:
        st.success(f"🐦 Bird ({1-pred:.2f})")