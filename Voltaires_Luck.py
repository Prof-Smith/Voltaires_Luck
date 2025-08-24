streamlit_code = """
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title='Voltaire Bond Lottery Simulation', layout='wide')

st.title("Voltaire's Bond Lottery Exploitation")

st.markdown("""### Introduction
In 18th-century France, Voltaire discovered a mathematical flaw in a government bond lottery. The lottery allowed bondholders to enter for a fixed fee, regardless of the bond's market value. Voltaire and mathematician La Condamine exploited this by buying undervalued bonds and repeatedly winning large prizes.

This app simulates that scenario with fictional bonds. You can edit the bond values, simulate a lottery draw, and analyze expected returns.""")

st.markdown("### Edit Bond Table")

# Editable bond table
data = {
    "Bond ID": [f"B{i}" for i in range(1, 21)],
    "Face Value": [random.choice([5, 10, 20, 50, 100]) for _ in range(20)],
    "Market Price": [round(random.uniform(1, 95), 2) for _ in range(20)],
    "Entry Fee": [10]*20,
    "Lottery Prize": [100]*20
}
edited_df = pd.DataFrame(data)
edited_df = st.data_editor(edited_df, num_rows="dynamic")

st.markdown("### Simulate Lottery Draw")
if st.button("Draw Winning Bond"):
    winning_bond = random.choice(edited_df["Bond ID"].tolist())
    st.success(f"Winning Bond: {winning_bond}")

st.markdown("### Expected Returns")
edited_df["Expected Return"] = edited_df["Lottery Prize"] * (1/20) - edited_df["Entry Fee"]
st.dataframe(edited_df)

st.markdown("""### Strategy Discussion
- Which bonds offer the highest expected return?
- How would you allocate a budget to maximize profit?
- What changes would prevent exploitation like Voltaire's?""")
"""

with open("voltaire_lottery_app.py", "w") as f:
    f.write(streamlit_code)

print("Corrected Streamlit app 'voltaire_lottery_app.py' has been created.")

## Installation
