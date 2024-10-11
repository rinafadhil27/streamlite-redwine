import pickle
import streamlit as st


# Memuat model
model = pickle.load(open('redwine.sav', 'rb'))

# Judul aplikasi
st.title('Prediksi Kualitas Anggur Merah')

# Input fitur
fixed_acidity = st.number_input('Fixed Acidity')
volatile_acidity = st.number_input('Volatile Acidity')
citric_acid = st.number_input('Citric Acid')
residual_sugar = st.number_input('Residual Sugar')
chlorides = st.number_input('Chlorides')
free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide')
total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide')
density = st.number_input('Density')
ph = st.number_input('pH')
sulphates = st.number_input('Sulphates')
alcohol = st.number_input('Alcohol')

# Buat DataFrame untuk input
input_data = pd.DataFrame({
    'fixed acidity': [fixed_acidity],
    'volatile acidity': [volatile_acidity],
    'citric acid': [citric_acid],
    'residual sugar': [residual_sugar],
    'chlorides': [chlorides],
    'free sulfur dioxide': [free_sulfur_dioxide],
    'total sulfur dioxide': [total_sulfur_dioxide],
    'density': [density],
    'pH': [ph],
    'sulphates': [sulphates],
    'alcohol': [alcohol]
})

# Menampilkan tombol untuk memprediksi
if st.button('Prediksi Kualitas'):
    prediction = model.predict(input_data)
    st.write(f'Prediksi Kualitas Anggur: {prediction[0]}')

