import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv("Weather_Resources_List.csv")

st.set_page_config(page_title="Weather Resource Directory", layout="wide")
st.title("🌤️ Weather Resource Directory")
st.markdown("Use the filters below to browse a list of helpful weather websites and tools.")

# Filter options
gov_filter = st.selectbox("Show Only:", ["All", "Official (.gov)", "Unofficial (non-gov)"])
search = st.text_input("Search by Name or Description")

filtered_df = df.copy()

if gov_filter == "Official (.gov)":
    filtered_df = filtered_df[filtered_df["official.gov yes or no"].str.lower() == "yes"]
elif gov_filter == "Unofficial (non-gov)":
    filtered_df = filtered_df[filtered_df["official.gov yes or no"].str.lower() == "no"]

if search:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(search, case=False, na=False) |
        filtered_df["description"].str.contains(search, case=False, na=False)
    ]

# Display entries
for _, row in filtered_df.iterrows():
    st.markdown(f"### [{row['name']}]({row['website']})")
    st.markdown(f"**Official Source:** {row['official.gov yes or no']}")
    st.markdown(row["description"])
    st.markdown("---")
