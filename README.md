# 📈 Live Crypto Time Series Forecasting Dashboard

Aplikasi cerdas berbasis web yang mampu memproyeksikan harga cryptocurrency (Bitcoin, Ethereum, Solana) di masa depan dengan menganalisis komponen tren historis secara otomatis.

## 🎯 Masalah Finansial & Bisnis yang Diselesaikan
Pasar cryptocurrency memiliki tingkat volatilitas yang sangat tinggi. Bagi trader, investor, maupun institusi finansial, menentukan arah tren jangka menengah hingga panjang sangat sulit jika hanya mengandalkan insting.

**Solusi:** Proyek ini mengimplementasikan analisis deret waktu (*Time Series Forecasting*) menggunakan algoritma **Meta Prophet** untuk memecah data harga menjadi komponen tren makro dan pola musiman harian/mingguan/tahunan. Sistem ini bertindak sebagai alat bantu keputusan (*decision-support tool*) kuantitatif dalam strategi investasi.

## 🛠️ Fitur & Teknologi Utama
* **Real-time Data Sourcing:** Mengintegrasikan library `yfinance` untuk menarik data penutupan pasar secara langsung saat aplikasi dijalankan.
* **Meta Prophet Algorithm:** Pemodelan matematika aditif untuk menangani data non-linear dengan efek musiman (*seasonality*) yang kuat.
* **Interactive Visualization:** Menggunakan `Plotly` untuk menghasilkan grafik kaya fitur yang dapat di-zoom secara dinamis oleh pengguna.
* **Streamlit Framework:** Membangun antarmuka web yang responsif dengan baris kode Python yang minimalis.# crypto-price-time-series-forecasting
