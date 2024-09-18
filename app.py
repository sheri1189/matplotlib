import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    df = pd.read_csv('sample_csv.csv', header=0)
    df.columns = df.columns.str.strip()
    return df


def main():
    st.title("Impounds Data Visualization")
    df = load_data()
    if 'Impound Date' in df.columns or 'Balance Due' in df.columns:
        df['Impound Date'] = pd.to_datetime(
            df['Impound Date'], errors='coerce')
        df['Balance Due'] = df['Balance Due'].replace(
            {'\$': '', ',': ''}, regex=True).astype(float)
        daily_balance = df.groupby(df['Impound Date'].dt.date)[
            'Balance Due'].sum()
        plt.figure(figsize=(10, 6))
        plt.plot(daily_balance.index, daily_balance.values, marker='o')
        plt.title('Total Balance Due Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Balance Due ($)')
        plt.xticks(rotation=45)
        plt.grid()
        st.pyplot(plt)
    else:
        st.write("Column 'Impound Date' does not exist.")


if __name__ == "__main__":
    main()
