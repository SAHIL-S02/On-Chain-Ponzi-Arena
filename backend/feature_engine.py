import pandas as pd
from datetime import datetime

def extract_wallet_features(transactions, wallet_address):
    if not transactions:
        return {}

    df = pd.DataFrame(transactions)

    # Convert value from Wei to ETH
    df["value"] = df["value"].astype(float) / 1e18

    # Convert timestamp
    df["timeStamp"] = df["timeStamp"].astype(int)
    df["datetime"] = df["timeStamp"].apply(
        lambda x: datetime.utcfromtimestamp(x)
    )

    wallet_address = wallet_address.lower()

    # Inflow = to wallet
    inflow = df[df["to"].str.lower() == wallet_address]["value"].sum()

    # Outflow = from wallet
    outflow = df[df["from"].str.lower() == wallet_address]["value"].sum()

    # Unique interactions
    unique_senders = df["from"].nunique()
    unique_receivers = df["to"].nunique()

    # Avg transaction size
    avg_tx_value = df["value"].mean()

    # Transaction frequency (per day)
    time_span_days = (
        (df["datetime"].max() - df["datetime"].min()).days or 1
    )
    tx_per_day = len(df) / time_span_days

    features = {
        "total_inflow_eth": round(inflow, 4),
        "total_outflow_eth": round(outflow, 4),
        "net_flow_eth": round(inflow - outflow, 4),
        "inflow_outflow_ratio": round(
            inflow / outflow, 4
        ) if outflow > 0 else None,
        "unique_senders": unique_senders,
        "unique_receivers": unique_receivers,
        "avg_tx_value_eth": round(avg_tx_value, 4),
        "transactions_per_day": round(tx_per_day, 2)
    }

    return features