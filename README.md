Aplikasi Streamlit ini digunakan untuk melakukan eksplorasi data churn pelanggan pada dataset Telco.

## Fitur Aplikasi

- **Preview Data**
  - Tampilkan 10 baris pertama dataset dengan checkbox.
- **Filter Data**
  - Pilih gender pelanggan menggunakan selectbox.
  - Filter minimum tenure (bulan) menggunakan slider.
- **Ringkasan Data**
  - Tampilkan ringkasan jumlah pelanggan berdasarkan *State*, *Payment Method*, atau *Contract* menggunakan radio button.
- **Visualisasi**
  - Barplot persentase churn vs tidak churn.
  - Visualisasi 5 kota dengan jumlah customer churn terbanyak.

## Cara Menjalankan

1. Pastikan sudah menginstal Streamlit:
pip install streamlit

2. Jalankan aplikasi:
streamlit run app.py

3. Pastikan file dataset `Telco_customer_churn (1).csv` berada di folder yang sama dengan file script.
Kalau nama file Python kamu beda, ganti app.py di atas sesuai nama file Python-mu.

4. Hasil deploy
https://as-ds32b-day40-mabdulhanan.streamlit.app

