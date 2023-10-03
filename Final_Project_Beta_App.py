import streamlit as st
import pandas as pd
import pickle
from PIL import Image

st.image(Image.open('Fig 1.jpeg'))

st.title('Final Project Portugal Bank Telemarketing Campaign for Deposito')
st.text('Digunakan untuk memprediksi apakah nasabah cederung membuka deposito atau tidak')

st.title('A. Feature')
st.text('Silahkan masukan fitur nasabah  yang akan diprediksi')

if 'model' not in st.session_state:
    model = pickle.load(open('Final Project Beta.sav', 'rb'))
    st.session_state['model'] = model


age = st.number_input('Umur nasabah', value = 17, step=1)

if age > 98 or age < 17:
    st.write('Masukan rentang nilai dari 17-98 tahun, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Umur nasabah adalah adalah', age)
    st.write('---')


campaign = st.number_input('Jumlah kontak nasabah pada campaign terkini', value = 1, step=1)

if campaign > 56 or campaign < 1:
    st.write('Masukan rentang nilai dari 1-56, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Nasabah telah dikontak pada campaign terkini sebanyak', campaign)
    st.write('---')


previous = st.number_input('Jumlah kontak nasabah pada campaign terdahulu', value = 0, step=1)

if previous > 7 or previous < 0:
    st.write('Masukan rentang nilai dari 0-7, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Nasabah telah dikontak pada campaign terdahulu sebanyak', previous)
    st.write('---')


emp_var_rate = st.number_input('Indeks employment variation rate', value = 0.0)

if emp_var_rate > 1.4 or emp_var_rate < -3.4:
    st.write('Masukan rentang nilai dari -3.4-1.4, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Employment Variation Rate sebesar', round(emp_var_rate,1))
    st.write('---')


job = st.selectbox(
    'Pekerjaan nasabah',
    ('admin.', 'blue-collar', 'entrepreneur', 'housemaid','management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed'))

st.write('Nasabah bekerja sebagai', job)
st.write('---')


marital = st.selectbox(
    'Status nasabah',
    ('divorced', 'married', 'single'))

st.write('Nasabah berstatus', marital)
st.write('---')


education = st.selectbox(
    'Pendidikan nasabah',
    ('basic.4y.', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree'))

st.write('Pendidikan nasabah terakhir', education)
st.write('---')


contact = st.selectbox(
    'Media kontak',
    ('cellular', 'telephone'))

st.write('Nasabah dikontak melalui', contact)
st.write('---')


month = st.selectbox(
    'Bulan kontak',
    ('apr', 'aug', 'dec', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep'))

st.write('Nasabah dikontak bulan', month)
st.write('---')


day_of_week = st.selectbox(
    'Hari kontak',
    ('fri', 'mon', 'thu', 'tue', 'wed'))

st.write('Nasabah dikontak hari', day_of_week)
st.write('---')


contact_prev_campaign = st.selectbox(
    'Apakah nasabah pernah dikontak campaign terdahulu?',
    ('contacted', 'not contacted'))

st.write('Nasabah', contact_prev_campaign)
st.write('---')


poutcome = st.selectbox(
    'Hasil campaign terdahulu',
    ('failure', 'nonexistent', 'success'))

st.write('Hasil campaign terdahulu adalah', poutcome)
st.write('---')


st.title('B. Rekap Data Input')
rekap = pd.DataFrame()
rekap['age'] = [age]
rekap['job'] = [job]
rekap['marital'] = [marital]
rekap['education'] = [education]
rekap['contact'] = [contact]
rekap['month'] = [month]
rekap['day_of_week'] = [day_of_week]
rekap['campaign'] = [campaign]
rekap['previous'] = [previous]
rekap['poutcome'] = [poutcome]
rekap['emp_var_rate'] = [emp_var_rate]
rekap['contact_prev_campaign'] = [contact_prev_campaign]

st.dataframe(data=rekap)

st.title('C. Prediksi')
if st.button('Prediksi nasabah'):

    if age < 0 or campaign < 0 or previous < 0:
        st.write('Nilai fitur tidak bisa negatif')
    else:
        hasil = st.session_state['model'].predict(rekap)
        st.write(f'Hasil prediksi tersebut bahwa nasabah masuk ke kelas {hasil}')
else:
    st.write('Masukan nilai fitur')


st.write('Kelas 1 -> cenderung membuka deposito | Kelas 0 -> cenderung tidak membuka depostio')