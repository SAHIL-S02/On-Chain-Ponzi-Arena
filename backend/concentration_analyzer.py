import pandas as pd

def calculate_outflow_concentration(transactions, wallet_address):
    if not transactions:
        return {}

    df = pd.DataFrame(transactions)
    df["value"] = df["value"].astype(float) / 1e18

    wallet_address = wallet_address.lower()

    # Filter only outgoing transactions
    outflow_df = df[df["from"].str.lower() == wallet_address]

    if outflow_df.empty:
        return {
            "top3_outflow_percentage": 0,
            "concentration_flag": False
        }

    total_outflow = outflow_df["value"].sum()

    # Group by receiver
    grouped = outflow_df.groupby("to")["value"].sum()

    top3_sum = grouped.sort_values(ascending=False).head(3).sum()

    percentage = (top3_sum / total_outflow) * 100 if total_outflow > 0 else 0

    if len(outflow_df) < 10:
        return {
            "top3_outflow_percentage": round(percentage, 2),
            "concentration_flag": False
        }

    unique_receivers = grouped.count()

    return {
        "top3_outflow_percentage": round(percentage, 2),
        "concentration_flag": percentage > 70 and unique_receivers <= 5
    }