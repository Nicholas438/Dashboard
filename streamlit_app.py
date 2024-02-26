import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style='dark')

df = pd.read_csv("data.csv")
hours_df = pd.read_csv("hour.csv")


st.write("<h2 style='text-align: center;'>DASHBOARD BIKE SHARING 2011-2012</h2>", unsafe_allow_html=True)
st.markdown("<br><h3>Hi There!</h3>", unsafe_allow_html=True)
st.markdown("<h5>Welcome to the bike Sharing Dashboard!</h5>", unsafe_allow_html=True)
st.markdown("<p>Navigate through the sidebar to access summaries of the data!</p>", unsafe_allow_html=True)

st.sidebar.title("Dashboard Navigation")

rental_2011 = df[df['yr'] == 0]['cnt'].sum()
rental_2012 = df[df['yr'] == 1]['cnt'].sum()
total = rental_2011 + rental_2012
persentase = round((rental_2012 - rental_2011) / rental_2011 * 100)
persentase = str(persentase) + "%"

col1, col2,col3 = st.columns(3)

with col1:
    st.metric(label='Total Rental Sepeda', value=str(format(total,',d')))

with col2:
    st.metric(label='Jumlah Rental Tahun 2011', value=str(format(rental_2011,',d')))

with col3:
    st.metric(label='Jumlah Rental Tahun 2012', value=str(format(rental_2012,',d')), delta=persentase
        )

st.sidebar.write("<br><b>Dataset Information</b>", unsafe_allow_html=True)
if st.sidebar.checkbox("Show Dataset per day"):
    st.header("Dataset per day")
    st.write(df)
if st.sidebar.checkbox("Show Dataset per hour"):
    st.header("Data per hour" )
    st.write(hours_df)
if st.sidebar.checkbox("Statistics"):
    st.header("Statistics of days data" )
    st.write(df.describe())


st.sidebar.write("<br><b>Dataset Visualization</b>", unsafe_allow_html=True)
if st.sidebar.checkbox("Rental for the year"):
    st.header("Number of rental for the year 2011-2012")
    df_date = df[["cnt","dteday"]].copy()
    df_date['dteday'] = pd.to_datetime(df_date['dteday'].copy())
    # Set the 'datetime_column' as the index of the DataFrame if it's not already
    df_date.set_index('dteday', inplace=True)

    # Resample the datetime series on 15-day intervals and apply any desired aggregation function (e.g., count)
    result = df_date.resample('5D').mean()
    fig, ax = plt.subplots(figsize=(16, 8))
    plt.title("Number of Rental for the year 2011-2012", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    ax.plot(result.index,result['cnt'])
    st.pyplot(fig)
    
if st.sidebar.checkbox("Rental per month"):
    mean  =df.groupby('mnth')['cnt'].mean()
    idxmin = (mean.idxmin())
    idxmax = (mean.idxmax())
    colors = ["#D3D3D3" for i in range(len(mean))]
    colors[idxmin-1] = "#90CAF9"
    colors[idxmax-1] = "#003366"
    st.header("Number of Rental per month")
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.bar(df.groupby('mnth')['cnt'].mean().index, df.groupby('mnth')['cnt'].mean().values,color = colors)
    plt.title("Number of Rental per month", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
if st.sidebar.checkbox("Rental for each weather"):
    st.header("Number of Rental for each weather")
    fig, ax = plt.subplots(figsize=(10, 5))
    mean = df.groupby('weathersit')['cnt'].mean()

    idxmin = (mean.idxmin())
    idxmax = (mean.idxmax())
    colors = ["#90CAF9" if weather == idxmin else "#003366" if weather == idxmax else "#D3D3D3" for weather in mean.index]
    plt.bar(mean.index, mean.values,color = colors)
    plt.title("Number of Rental for each weather)", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
if st.sidebar.checkbox("Rental on temperature"):
    st.header("Number of Rental based on temperature")
    df_temp = df[["cnt","temp"]]
    df_temp = df_temp.assign(temp_rounded = lambda x: (round(((x['temp'])*47)-8)*20)/20)
    df_temp.describe()
    fig, ax = plt.subplots(figsize=(10, 5))
    stats = df_temp.groupby('temp_rounded')['cnt'].mean()
    plt.plot(stats.index, stats.values)
    plt.title("Number of Rental for temperature", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
if st.sidebar.checkbox("Rental for each season"):
    st.header("Number of Rental for each season")
    fig, ax = plt.subplots(figsize=(10, 5))
    stats = df.groupby('season')['cnt'].mean()
    idxmin = (stats.idxmin())
    idxmax = (stats.idxmax())
    colors = ["#90CAF9" if weather == idxmin else "#003366" if weather == idxmax else "#D3D3D3" for weather in stats.index]
    plt.bar(stats.index, stats.values, color = colors)
    plt.title("Number of Rental for each season", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
if st.sidebar.checkbox("Rental for holiday"):
    st.header("Number of Rental for holiday")
    fig, ax = plt.subplots(figsize=(10, 5))
    stats = df.groupby('holiday')['cnt'].mean()
    idxmin = (stats.idxmin())
    idxmax = (stats.idxmax())
    colors = ["#90CAF9" if weather == idxmin else "#003366" if weather == idxmax else "#D3D3D3" for weather in stats.index]
    plt.bar(stats.index, stats.values,color = colors)
    plt.title("Number of Rental for holiday", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
if st.sidebar.checkbox("Rental per hr"):
    st.header("Number of Rental for holiday")
    fig, ax = plt.subplots(figsize=(10, 5))
    stats = hours_df.groupby('hr')['cnt'].mean()
    idxmin = (stats.idxmin())
    idxmax = (stats.idxmax())
    colors = ["#90CAF9" if weather == idxmin else "#003366" if weather == idxmax else "#D3D3D3" for weather in stats.index]
    plt.bar(stats.index, stats.values,color = colors)
    plt.title("Number of Rental for each hr", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
if st.sidebar.checkbox("Rental for each weekday"):
    st.header("Number of Rental for holiday")
    fig, ax = plt.subplots(figsize=(10, 5))
    stats = df.groupby('weekday')['cnt'].mean()
    idxmin = (stats.idxmin())
    idxmax = (stats.idxmax())
    colors = ["#90CAF9" if weather == idxmin else "#003366" if weather == idxmax else "#D3D3D3" for weather in stats.index]
    plt.bar(stats.index, stats.values,color = colors)
    plt.title("Number of Rental for each weekday", loc="center", fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)