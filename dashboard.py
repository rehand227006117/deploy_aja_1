import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Dashboard Peminjaman Sepeda", layout="wide")

# Fungsi untuk memuat data dengan caching
@st.cache_data
def load_data():
    day = pd.read_csv("day_bersih.csv")
    hour = pd.read_csv("hour_bersih.csv")
    return day, hour

# Load data
day, hour = load_data()

# Judul
st.title("🚲 Dashboard Peminjaman Sepeda")

# Sidebar untuk navigasi
st.sidebar.header("Pilihan Analisis")
analisis = st.sidebar.radio("Pilih Analisis:", ["Week", "Musim", "Suhu", "Kondisi Cuaca"])

# ==================== ANALISIS TREND HARIAN ==================== #
if analisis == "Week":
    st.subheader("📊 Tren Peminjaman Sepeda: Weekday vs Weekend")

    weekday_count = day[day['category_days'] == 'weekdays']['count'].sum()
    weekend_count = day[day['category_days'] == 'weekend']['count'].sum()

    labels = ['Weekday', 'Weekend']
    sizes = [weekday_count, weekend_count]
    colors = ['skyblue', 'lightcoral']

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title('Perbandingan Peminjaman Sepeda (Weekday vs. Weekend)')
    ax.axis('equal')
    st.pyplot(fig)

    # Grafik batang
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(labels, sizes, color=colors)
    ax.set_title('Perbandingan Peminjaman Sepeda (Weekday vs. Weekend)')
    ax.set_xlabel('Kategori Hari')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

# ==================== ANALISIS MUSIM ==================== #
elif analisis == "Suhu":
    st.subheader("🌦️ Peminjaman Sepeda Berdasarkan Suhu")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x=day['temp'], y=day['casual'], alpha=0.5, ax=ax)
    ax.set_xlabel("Normalized Temperature (temp)")
    ax.set_ylabel("Total Rentals (casual)")
    ax.set_title("Hubungan Suhu dan Peminjaman Sepeda (Casual)")
    st.pyplot(fig)

    # Scatter plot 2: Temp vs Count
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x=day['temp'], y=day['count'], alpha=0.5, ax=ax)
    ax.set_xlabel("Normalized Temperature (temp)")
    ax.set_ylabel("Total Rentals (cnt)")
    ax.set_title("Hubungan Suhu dan Peminjaman Sepeda (Total)")
    st.pyplot(fig)

    # Scatter plot 3: Temp vs Registered
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x=day['temp'], y=day['registered'], alpha=0.5, ax=ax)
    ax.set_xlabel("Normalized Temperature (temp)")
    ax.set_ylabel("Total Rentals (registered)")
    ax.set_title("Hubungan Suhu dan Peminjaman Sepeda (Registered)")
    st.pyplot(fig)

    # Scatter plot 4: Atemp vs Casual
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x=day['atemp'], y=day['casual'], alpha=0.5, ax=ax)
    ax.set_xlabel("Normalized feeling temperature in Celsius (atemp)")
    ax.set_ylabel("Total Rentals (casual)")
    ax.set_title("Hubungan Suhu Terasa dan Peminjaman Sepeda (Casual)")
    st.pyplot(fig)

    # Scatter plot 5: Atemp vs Count
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x=day['atemp'], y=day['count'], alpha=0.5, ax=ax)
    ax.set_xlabel("Normalized feeling temperature in Celsius (atemp)")
    ax.set_ylabel("Total Rentals (cnt)")
    ax.set_title("Hubungan Suhu Terasa dan Peminjaman Sepeda (Total)")
    st.pyplot(fig)

    # Scatter plot 6: Atemp vs Registered
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x=day['atemp'], y=day['registered'], alpha=0.5, ax=ax)
    ax.set_xlabel("Normalized feeling temperature in Celsius (atemp)")
    ax.set_ylabel("Total Rentals (registered)")
    ax.set_title("Hubungan Suhu Terasa dan Peminjaman Sepeda (Registered)")
    st.pyplot(fig)

# ==================== ANALISIS Musim ==================== #
elif analisis == "Musim":
    st.subheader("📊 Tren Peminjaman Sepeda berdasarkan musim")
    # Hitung jumlah peminjaman berdasarkan musim
    season_counts = {
        "Spring": day[day['season'] == 'Spring'].sum(),
        "Summer": day[day['season'] == 'Summer'].sum(),
        "Fall": day[day['season'] == 'Fall'].sum(),
        "Winter": day[day['season'] == 'Winter'].sum(),
    }

    # Ekstrak data untuk pie chart
    labels = list(season_counts.keys())
    sizes_cr = [season_counts[season]['count'] for season in labels]
    sizes_casual = [season_counts[season]['casual'] for season in labels]
    sizes_registered = [season_counts[season]['registered'] for season in labels]
    colors = ['lightblue', 'lightblue', 'lightgreen', 'lightblue']

    # Fungsi untuk membuat pie chart
    def plot_pie_chart(sizes, title):
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title(title)
        ax.axis('equal')
        return fig

    st.subheader("Perbandingan Total Peminjaman Sepeda")
    st.pyplot(plot_pie_chart(sizes_cr, "Total Peminjaman Sepeda"))

    st.subheader("Perbandingan Peminjaman Sepeda Casual")
    st.pyplot(plot_pie_chart(sizes_casual, "Peminjaman Sepeda Casual"))

    st.subheader("Perbandingan Peminjaman Sepeda Registered")
    st.pyplot(plot_pie_chart(sizes_registered, "Peminjaman Sepeda Registered"))

# ==================== ANALISIS KONDISI CUACA ==================== #
elif analisis == "Kondisi Cuaca":
    st.subheader("🌤️ Peminjaman Sepeda Berdasarkan Kondisi Cuaca")

        # Hitung jumlah peminjaman berdasarkan kondisi cuaca
    clear_count = day[day['situation_of_weather'] == 'Clear']['count'].sum()
    mist_cloudy_count = day[day['situation_of_weather'] == 'Mist_Cloudy']['count'].sum()
    light_rain_count = day[day['situation_of_weather'] == 'Light_Rain']['count'].sum()
    heavy_rain_count = day[day['situation_of_weather'] == 'Heavy_Rain']['count'].sum()

    clear_count_casual = day[day['situation_of_weather'] == 'Clear']['casual'].sum()
    mist_cloudy_count_casual = day[day['situation_of_weather'] == 'Mist_Cloudy']['casual'].sum()
    light_rain_count_casual = day[day['situation_of_weather'] == 'Light_Rain']['casual'].sum()
    heavy_rain_count_casual = day[day['situation_of_weather'] == 'Heavy_Rain']['casual'].sum()

    clear_count_registered = day[day['situation_of_weather'] == 'Clear']['registered'].sum()
    mist_cloudy_count_registered = day[day['situation_of_weather'] == 'Mist_Cloudy']['registered'].sum()
    light_rain_count_registered = day[day['situation_of_weather'] == 'Light_Rain']['registered'].sum()
    heavy_rain_count_registered = day[day['situation_of_weather'] == 'Heavy_Rain']['registered'].sum()

    # Labels dan Data
    labels = ['Clear', 'Mist Cloudy', 'Light Rain/Snow', 'Heavy Rain/Snow']
    sizes = [clear_count, mist_cloudy_count, light_rain_count, heavy_rain_count]
    sizes_casual = [clear_count_casual, mist_cloudy_count_casual, light_rain_count_casual, heavy_rain_count_casual]
    sizes_registered = [clear_count_registered, mist_cloudy_count_registered, light_rain_count_registered, heavy_rain_count_registered]
    colors = ['lightgreen', 'lightcoral', 'lightblue', 'gray']

    # Plot 1: Total Peminjaman Sepeda
    st.subheader("Perbandingan Peminjaman Sepeda berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, sizes, color=colors)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Total Peminjaman Sepeda")
    st.pyplot(fig)

    # Plot 2: Peminjaman Casual
    st.subheader("Perbandingan Peminjaman Sepeda Casual berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, sizes_casual, color=colors)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Peminjaman Sepeda Casual")
    st.pyplot(fig)

    # Plot 3: Peminjaman Registered
    st.subheader("Perbandingan Peminjaman Sepeda Registered berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, sizes_registered, color=colors)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Peminjaman Sepeda Registered")
    st.pyplot(fig)

