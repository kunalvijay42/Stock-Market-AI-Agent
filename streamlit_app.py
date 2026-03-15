import streamlit as st
from crew import stock_crew

st.set_page_config(page_title="Stock Market AI Agent", page_icon="📈")

st.title("📈 Stock Market AI Agent")
st.write(
    "Enter a stock ticker symbol (e.g. AAPL, TSLA) and run the AI crew to get analysis + trading suggestions."
)

stock_symbol = st.text_input("Stock symbol", value="AAPL", max_chars=10)

if st.button("Run analysis"):
    if not stock_symbol.strip():
        st.error("Please enter a stock symbol.")
    else:
        with st.spinner("Running AI crew... this may take a few seconds."):
            try:
                result = stock_crew.kickoff(inputs={"stock": stock_symbol.strip().upper()})
                st.success("✅ Completed")
                st.subheader("Agent Output")
                st.write(result.raw)
            except Exception as e:
                st.error("Failed to run the stock AI crew.")
                st.exception(e)

st.markdown("---")