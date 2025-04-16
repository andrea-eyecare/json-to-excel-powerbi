
# 📂 JSON to Excel Converter for Power BI

This Streamlit app allows users to upload nested or structured JSON files and automatically convert them into clean, flat Excel files, optimized for Power BI.

## ✅ Features

- Automatically detects JSON structure
- Flattens nested lists (e.g., `proposedLevels`) and hierarchical cost dictionaries
- Cleans column names (Power BI friendly: lowercase, no spaces or special characters)
- Produces one downloadable Excel sheet with consistent formatting

## 🚀 How to Use

1. Go to [your deployed app URL here]
2. Upload your `.json` file
3. Preview the flattened data table
4. Click **Download Excel File** to save a Power BI–ready `.xlsx`

## 🛠️ Supported JSON Structures

### 1. Proposed Levels Format
```json
{
  "data": [
    {
      "level": 1,
      "minRange": 1000,
      "avgRange": 2000,
      "maxRange": 3000,
      "proposedLevels": [
        {"proposedLevel": 2, "cost": 1500},
        {"proposedLevel": 3, "cost": 2500}
      ]
    }
  ]
}
```

### 2. Hierarchical Cost Format
```json
{
  "data": {
    "longTermRoads": {
      "renew": {
        "paved": 10000,
        "granular": 2000
      },
      "operate": {
        "paved": 500,
        "granular": 300
      }
    }
  }
}
```

## 📦 To Run Locally

```bash
pip install streamlit pandas openpyxl
streamlit run app_powerbi_universal_fixed.py
```

## 🌐 Hosted on Streamlit Cloud

> Deployed at: https://your-username-your-repo-name.streamlit.app
