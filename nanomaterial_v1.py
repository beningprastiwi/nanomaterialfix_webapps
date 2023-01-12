import streamlit as st

st.snow()

st.title('MENGHITUNG DEGRADASI NANOMATERIAL')

blanko = st.number_input('Masukan Nilai Absorbansi Blanko')
sampel = st.number_input('Masukan Nilai Absorbansi Sampel')

tombol1 = st.button('Persentase Degradasi')

if tombol1:
    persentase_degradasi = ((blanko-sampel)/blanko)*100
    st.success(f'Persentase Degradasi sebesar {persentase_degradasi}')
    

st.title('JENIS NANOMATERIAL BERPORI BERDASARKAN DIAMETER PORI NANOMATERIAL')
diameter = st.number_input('Masukkan Ukuran Diameter  ')

tombol2 = st.button('Klik untuk mengetahui jenis nanomaterial')
if tombol2:

    if diameter>=0 and diameter<2:
        st.success('Microporous')
    elif diameter>=2 and diameter<50:
        st.success('Mesoporous')
    elif diameter>=50 and diameter<100:
        st.success('Macroporous')
    else:
        st.success('range data salah,masukkan diameter yang sesuai!!')
        

