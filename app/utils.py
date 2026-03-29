import pandas as pd


def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except:
        print("Error loading file, file must be csv")
        return None


def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=["Product", "Revenue"])

    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
    df = df.dropna(subset=["Revenue"])

    if "Quantity" in df.columns:
        df["Quantity"] = df["Quantity"].fillna(0)

    return df


def get_insights(df):
    return {
        "total_revenue": df["Revenue"].sum(),
        "top_product": df.groupby("Product")["Revenue"].sum().idxmax(),
    }


def get_chart_data(df):
    charts = {}

    # Product-wise revenue
    charts["product"] = df.groupby("Product")["Revenue"].sum()

    # Category-wise revenue
    if "Category" in df.columns:
        charts["category"] = df.groupby("Category")["Revenue"].sum()

    # Revenue trend (Date)
    if "Date" in df.columns:
        charts["trend"] = df.groupby("Date")["Revenue"].sum()

    return charts
