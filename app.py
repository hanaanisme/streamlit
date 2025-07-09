import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul
st.title("Analisis Customer Churn - Telco Dataset")

# Load data lokal 
try:
    df = pd.read_csv("Telco_customer_churn (1).csv")
    st.success("Data berhasil dimuat.")
except FileNotFoundError:
    st.error("File 'Telco_customer_churn.csv' tidak ditemukan di folder ini.")
    st.stop()

# 1. Checkbox untuk preview
if st.checkbox("Tampilkan 10 data teratas"):
    st.write(df.head(10))

# 2. Selectbox filter gender 
gender_option = st.selectbox("Pilih gender pelanggan:", df["Gender"].unique())
filtered_df = df[df["Gender"] == gender_option]

# 3. Slider tenure filter
min_tenure = st.slider(
    "Minimum Tenure (bulan)", 
    min_value=int(df["Tenure Months"].min()),
    max_value=int(df["Tenure Months"].max()),
    value=0
)
filtered_df = filtered_df[filtered_df["Tenure Months"] >= min_tenure]

# 4. Radio untuk memilih tampilan ringkas 
summary_choice = st.radio(
    "Tampilkan ringkasan data berdasarkan:",
    options=["State", "Payment Method", "Contract"]
)

if summary_choice == "State":
    st.write(filtered_df["State"].value_counts())
elif summary_choice == "Payment Method":
    st.write(filtered_df["Payment Method"].value_counts())
else:
    st.write(filtered_df["Contract"].value_counts())

# Visualisasi 1 
st.subheader("Persentase Customer yang Churn dan Tidak Churn")

churn_pct = filtered_df["Churn Label"].value_counts(normalize=True) * 100
fig1, ax1 = plt.subplots()
sns.barplot(x=churn_pct.index, y=churn_pct.values, palette=["green", "red"], ax=ax1)
ax1.set_ylabel("Persentase (%)")
ax1.set_ylim(0, 100)
ax1.set_title("Persentase Churn vs Tidak Churn")
st.pyplot(fig1)

# Visualisasi 2
st.subheader("5 Kota dengan Jumlah Customer Churn Terbanyak")

city_churn = (
    filtered_df.groupby(["City", "Churn Label"])
    .size()
    .unstack(fill_value=0)
)

top5_cities = city_churn.sort_values(by="Yes", ascending=False).head(5)

fig3, ax3 = plt.subplots(figsize=(10,5))
top5_cities.plot(kind="bar", stacked=True, ax=ax3, colormap="viridis")
ax3.set_ylabel("Jumlah Pelanggan")
ax3.set_title("5 Kota dengan Customer Churn dan Tidak Churn Terbanyak")
plt.xticks(rotation=45)
st.pyplot(fig3)

