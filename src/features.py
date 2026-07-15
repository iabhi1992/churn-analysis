import pandas as pd


def add_features(df):
    """Engineer churn prediction features from raw customer data."""
    df["days_since_purchase"] = (
        pd.Timestamp.now() - pd.to_datetime(df["last_purchase_date"])
    ).dt.days
    df["avg_order_value"] = df["total_spend"] / df["order_count"].replace(0, 1)
    df["is_high_value"] = df["total_spend"] > df["total_spend"].median()
    return df
