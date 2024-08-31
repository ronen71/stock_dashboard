import pandas as pd
import streamlit as st

from data_loader import load_data

def main():
    st.title("주식 데이터 시각화")
    df = load_data()

    st.subheader("Select Date Range")
    df['Date'] = pd.to_datetime(df['Date']) 
    start_date = st.date_input("시작일", df['Date'].min())
    end_date = st.date_input("종료일", df['Date'].max())

    range_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    range_df = range_df.reset_index(drop=True)
    st.table(range_df)

    st.subheader("거래량 변동 차트")
    st.line_chart(range_df.set_index('Date')['Volume'])


if __name__ == '__main__':
    main()
