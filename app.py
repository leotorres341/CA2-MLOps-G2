import streamlit as st
import joblib

# === 1. Cargar modelo ===
def load_model():
    model = joblib.load("linear_regression_model.pkl")
    return model

model = None
try:
    model = load_model()
    st.success("✅ Modelo cargado correctamente")
except Exception as e:
    st.error("❌ Error cargando el modelo. Verifica el archivo .pkl")
    st.stop()

# === 2. Interfaz de usuario ===
st.sidebar.header("✍️ Ingrese datos del envío")
longitude = st.sidebar.number_input("Longitude", -180.0, 180.0, 0.0)
humidity = st.sidebar.number_input("Humidity", 0, 100, 50)

# === 3. Predicción ===
if st.button("Calcular tiempo de envío"):
    if model is not None:
        input_data = [[longitude, humidity]]
        prediction = model.predict(input_data)
        st.subheader(f"⏱️ Predicción del tiempo de envío: **{prediction[0]:.2f} minutos**")
    else:
        st.error("El modelo no está disponible.")