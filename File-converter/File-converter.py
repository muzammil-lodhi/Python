import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File Converter & Cleaner", layout="wide")

st.title("📁 File Converter & Cleaner")
st.write("Upload your CSV and Excel files to clean the data and convert formats effortlessly.")

# File uploader
files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

# If files are uploaded
if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()

        # Read the file
        if ext == "csv":
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.subheader(f"🔍 Preview: {file.name}")
        st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"Fill missing values - {file.name}"):
            numeric_cols = df.select_dtypes(include="number")
            df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())
            st.success("✅ Missing values filled successfully.")
            st.dataframe(df.head())

        # Select columns
        selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=list(df.columns))
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart
        if st.checkbox(f"📊 Show Chart - {file.name}"):
            numeric_data = df.select_dtypes(include="number")
            if not numeric_data.empty:
                st.bar_chart(numeric_data.iloc[:, :2])
            else:
                st.warning("⚠️ No numeric data available to show chart.")

        # Format choice
        format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Download button
        if st.button(f"Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.rsplit(".", 1)[0] + ".csv"
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.rsplit(".", 1)[0] + ".xlsx"

            output.seek(0)
            st.download_button("📥 Download File", file_name=new_name, data=output, mime=mime)
            st.success("✅ Processing Completed")

        


        
        

    