import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import datetime

# 1. Konfigurasi Tampilan Halaman Web
st.set_page_config(page_title="Crypto Forecast AI", page_icon="📈", layout="wide")
st.title("📈 Dashboard Prediksi Harga Kripto (Time Series Forecasting)")
st.markdown("""
Aplikasi ini memprediksi tren harga aset kripto di masa depan menggunakan algoritma **Meta Prophet** dan data historis *real-time* yang ditarik langsung dari Yahoo Finance.
""")
st.write("---")

# 2. Membuat Menu Interaktif di Bilah Samping (Sidebar)
st.sidebar.header("⚙️ Pengaturan Analisis")
kripto_pilihan = st.sidebar.selectbox("Pilih Koin Kripto:", ["BTC-USD", "ETH-USD", "SOL-USD"])
durasi_prediksi = st.sidebar.slider("Durasi Prediksi ke Depan (Hari):", min_value=30, max_value=365, value=90)

# 3. Fungsi Otomatis untuk Mengunduh Data Live
@st.cache_data # Fitur Streamlit agar tidak perlu download ulang data yang sama setiap tombol diklik
def ambil_data_live(ticker):
    hari_ini = datetime.date.today().strftime("%Y-%m-%d")
    # Menarik data dari tahun 2020 sampai hari ini
    data_mentah = yf.download(ticker, start="2020-01-01", end=hari_ini)
    
    # Merapikan struktur data sesuai syarat algoritma Prophet
    df_rapi = data_mentah.reset_index()
    df_rapi = df_rapi[['Date', 'Close']]
    df_rapi.columns = ['ds', 'y']
    return df_rapi

# Eksekusi penarikan data
data_kripto = ambil_data_live(kripto_pilihan)

# Menampilkan data 5 hari terakhir di halaman utama
st.subheader(f"📊 Data Historis Terakhir {kripto_pilihan}")
st.dataframe(data_kripto.tail(5), use_container_width=True)

st.write("---")

# 4. Tombol untuk Menjalankan Kecerdasan Buatan (AI)
if st.button("Jalankan Prediksi AI Sekarang", type="primary"):
    with st.spinner("🤖 AI sedang membaca pola tren dan siklus musiman kripto... Mohon tunggu..."):
        
        # Menginisialisasi dan melatih model Prophet secara instan
        model = Prophet(daily_seasonality=True)
        model.fit(data_kripto)
        
        # Membuat timeline masa depan dan memprediksinya
        masa_depan = model.make_future_dataframe(periods=durasi_prediksi)
        hasil_prediksi = model.predict(masa_depan)
        
        # 5. Menampilkan Grafik Interaktif Plotly
        st.subheader(f"🔮 Hasil Proyeksi Harga {kripto_pilihan} untuk {durasi_prediksi} Hari ke Depan")
        
        grafik_interaktif = plot_plotly(model, hasil_prediksi)
        st.plotly_chart(grafik_interaktif, use_container_width=True)
        
        # Keterangan Tambahan
        st.info("""
        💡 **Cara Membaca Grafik:**
        * **Titik-titik Hitam:** Harga penutupan asli di masa lalu.
        * **Garis Biru Tua:** Arah tren harga rata-rata yang diprediksi AI.
        * **Bayangan Biru Muda:** Rentang batas atas dan batas bawah (toleransi ketidakpastian pasar).
        """)