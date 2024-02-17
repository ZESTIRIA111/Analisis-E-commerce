import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


#==========================================================================


@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

def analisis_distribusi_pelanggan(customers_df):
    st.subheader("Grafik Pelanggan Berdasarkan Kode Pos dan Distribusinya di Berbagai Kota dan Negara Bagian")
    st.caption("**10122279 - Syadzwana Akbar Ramadhan**")
    st.subheader("Informasi Analisis")
    st.markdown("**Analisis Terhadap Banyaknya Pelanggan Berdasarkan Kode Pos dan Negara Bagian**")
    with st.expander("Tujuan Analisis Infomasi Tersebut"):
        st.write(
            "Menganalisis distribusi geografis pelanggan berdasarkan kode pos untuk memahami sebaran mereka di berbagai kota dan negara bagian.")
        st.write(
            "Menganalisis distribusi geografis pelanggan berdasarkan kode pos juga membantu dalam mengidentifikasi potensi pasar baru dan memperbaiki strategi pemasaran untuk meningkatkan penetrasi pasar di wilayah yang belum tergarap dengan baik.")

    # ===========================================================================
    st.markdown("---")
    st.subheader("Grafik 5 Kota Dengan Seller Paling Banyak")

    warna = ['green', 'lightgreen', 'lightgreen', 'lightgreen', 'yellow']
    # Menghitung jumlah pelanggan berdasarkan kode pos
    zip_code_counts = customers_df.groupby("customer_zip_code_prefix").size().reset_index(name='counts').head(10)

    # Tampilkan informasi dalam bentuk tabel
    st.write("Informasi Distribusi Pelanggan:")
    st.dataframe(zip_code_counts)

    # Plot grafik
    plt.figure(figsize=(10, 6))
    plt.bar(zip_code_counts["customer_zip_code_prefix"], zip_code_counts["counts"])
    plt.xlabel("Kode Pos Pelanggan")
    plt.ylabel("Jumlah Pelanggan")
    plt.title("Distribusi Pelanggan Berdasarkan Kode Pos")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Visualisasi"):
        st.write(
            "Grafik Pelanggan Berdasarkan Kode Pos : Grafik ini menunjukkan distribusi jumlah pelanggan berdasarkan kode pos. Kode pos yang paling banyak memiliki jumlah pelanggan adalah 1009, dengan total 7 pelanggan. Kota Sao Paulo, yang memiliki kode pos 1009, merupakan pusat utama aktivitas pelanggan Anda. Kota-kota lain seperti 1005 dan 1007 juga menunjukkan aktivitas pelanggan yang signifikan meskipun jumlahnya lebih sedikit.")
        st.write(
            "Informasi Distribusi Pelanggan (Top 5) : Tabel ini menampilkan 5 kode pos teratas beserta jumlah pelanggan di masing-masing kode pos. Kota Sao Paulo dengan kode pos 1009 memiliki jumlah pelanggan terbanyak, yaitu 7 pelanggan. Kota-kota lainnya seperti 1005 dan 1007 juga menunjukkan aktivitas pelanggan yang cukup signifikan, masing-masing dengan 6 dan 4 pelanggan.")

#------------10122296-----------
def analisis_penjual_terbanyak(seller_df):
    st.subheader("Analisis 10 Mayoritas Penjual Terbanyak")
    st.caption("**10122296 - Muhamad Taufik Arifin**")
    st.subheader("Informasi Analisis")
    st.markdown("**Analisis Terhadap 10 Kota Dengan Penjual Paling Banyak**")
    with st.expander("Tujuan Analisis Infomasi Tersebut"):
        st.write(
            "untuk memahami distribusi geografis penjual, mengidentifikasi pusat aktivitas penjualan, menyusun strategi pemasaran yang efektif, menentukan potensi pasar di berbagai wilayah, dan mengoptimalkan operasi distribusi dan logistik. Analisis ini membantu dalam memahami dinamika pasar secara keseluruhan dan mengambil keputusan strategis yang lebih baik dalam pengembangan bisnis e-commerce.")
    # ===========================================================================
    st.markdown("---")
    st.subheader("Grafik 10 Kota Dengan Penjual Paling Banyak")

    warna = ['green', 'lightgreen', 'lightgreen', 'lightgreen', 'yellow']

    # Menghitung jumlah penjual di berbagai kota
    seller_city = seller_df['seller_city'].value_counts()

    # Mengambil 10 mayoritas penjual terbanyak
    top_sellers = seller_city.head(10)
    # Tampilkan informasi dalam bentuk tabel
    st.write("Informasi 10 Mayoritas Penjual Terbanyak:")
    st.dataframe(top_sellers.reset_index().rename(columns={'index': 'Kota', 'seller_city': 'Jumlah Penjual'}))

    # Plot grafik
    plt.figure(figsize=(12, 6))
    plt.bar(top_sellers.index, top_sellers.values, color='skyblue')
    plt.xlabel("Kota")
    plt.ylabel("Jumlah Penjual")
    plt.title("10 Mayoritas Penjual Terbanyak")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Visualisasi"):
        st.write(
            "Dari data penjual dalam beberapa kota, kita dapat mengambil beberapa informasi penting. Sao Paulo menonjol sebagai kota dengan jumlah penjual terbanyak, mencapai 694 penjual, menunjukkan bahwa kota ini adalah pusat utama aktivitas penjualan. ")
        st.write(
            "Meskipun jumlahnya lebih rendah, Curitiba dan Rio de Janeiro dengan masing-masing 127 dan 96 penjual, juga menunjukkan aktivitas penjualan yang signifikan. Di sisi lain, Belo Horizonte dan Ribeirao Preto memiliki jumlah penjual yang lebih sedikit, yaitu 68 dan 52 penjual, menunjukkan potensi pertumbuhan yang besar. Strategi pemasaran yang tepat dapat membantu meningkatkan penetrasi pasar di kota-kota ini.")
        st.write(
            " Secara keseluruhan, data menunjukkan bahwa sebagian besar penjual berada di Sao Paulo, sementara kota-kota lainnya memiliki jumlah penjual yang jauh lebih sedikit. Dengan demikian, pemilik bisnis dapat menggunakan informasi ini untuk merencanakan strategi pemasaran yang lebih efektif dan meningkatkan penetrasi pasar serta pertumbuhan bisnis mereka.")


# Load dataset
customers_df = load_data("https://raw.githubusercontent.com/ZESTIRIA111/Analisis-E-commerce/main/customers_dataset.csv")
seller_df = load_data("https://raw.githubusercontent.com/ZESTIRIA111/Analisis-E-commerce/main/sellers_dataset.csv")

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)

if selected == 'Dashboard':
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2 = st.tabs(["Analisis distribusi pelanggan","Analisis Penjual Terbanyak"])
    with tab1:
        analisis_distribusi_pelanggan(customers_df)
    with tab2:
        analisis_penjual_terbanyak(seller_df)
