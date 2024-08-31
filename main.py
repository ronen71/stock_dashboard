import pandas as pd
import streamlit as st

from data_loader import load_data

def main():
    st.title("This is a dashboard")
    df = load_data()

    st.subheader("Select Date Range")
    df['Date'] = pd.to_datetime(df['Date']) 
    start_date = st.date_input("Start date", df['Date'].min())
    end_date = st.date_input("End date", df['Date'].max())

    range_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    range_df = range_df.reset_index(drop=True)
    st.table(range_df)


if __name__ == '__main__':
    main()
