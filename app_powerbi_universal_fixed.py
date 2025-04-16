
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Universal JSON to Excel Converter for Power BI", layout="centered")
st.title("📂 Universal JSON to Excel Converter for Power BI")

st.markdown("Upload any JSON file and this app will flatten and format it for easy analysis in Power BI.")

def clean_column_names(df):
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace(r"[^\w_]", "", regex=True)
        .str.lower()
    )
    return df

def flatten_proposed_levels_structure(json_data):
    flattened_rows = []
    for entry in json_data.get("data", []):
        base = {
            "current_level": entry.get("level"),
            "min_range": entry.get("minRange"),
            "avg_range": entry.get("avgRange"),
            "max_range": entry.get("maxRange"),
        }
        for proposed in entry.get("proposedLevels", []):
            row = base.copy()
            row["proposed_level"] = proposed.get("proposedLevel")
            row["cost"] = proposed.get("cost")
            flattened_rows.append(row)
    df = pd.DataFrame(flattened_rows)
    df = clean_column_names(df)
    return df

def flatten_nested_costs_structure(json_data):
    rows = []
    for category, details in json_data.get("data", {}).items():
        if not isinstance(details, dict):
            continue
        for action, surfaces in details.items():
            if not isinstance(surfaces, dict):
                continue
            for surface, value in surfaces.items():
                rows.append({
                    "category": category,
                    "action": action,
                    "surface": surface,
                    "value": value
                })
    df = pd.DataFrame(rows)
    df = clean_column_names(df)
    return df

def detect_structure_and_flatten(json_data):
    if "data" in json_data and isinstance(json_data["data"], list):
        if any("proposedLevels" in item for item in json_data["data"]):
            return flatten_proposed_levels_structure(json_data)
    if "data" in json_data and isinstance(json_data["data"], dict):
        return flatten_nested_costs_structure(json_data)
    return pd.DataFrame([{"error": "Unsupported JSON structure"}])

uploaded_file = st.file_uploader("Upload your JSON file", type="json")

if uploaded_file is not None:
    try:
        json_data = json.load(uploaded_file)
        df_flat = detect_structure_and_flatten(json_data)

        st.success("✅ JSON successfully flattened for Power BI!")
        st.dataframe(df_flat.head())

        excel_filename = "PowerBI_Universal_Output.xlsx"
        df_flat.to_excel(excel_filename, index=False, sheet_name="data")

        with open(excel_filename, "rb") as f:
            st.download_button("📥 Download Excel File", f, file_name=excel_filename)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
