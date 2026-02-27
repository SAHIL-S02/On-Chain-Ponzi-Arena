import pandas as pd
import numpy as np

def detect_temporal_patterns(transactions, wallet_address):
    if not transactions:
        return {}

    df = pd.DataFrame(transactions)

    df["value"] = df["value"].astype(float) / 1e18
    df["timeStamp"] = pd.to_datetime(df["timeStamp"].astype(int), unit="s")

    wallet_address = wallet_address.lower()

    inflow_df = df[df["to"].str.lower() == wallet_address]
    outflow_df = df[df["from"].str.lower() == wallet_address]

    inflow_daily = inflow_df.groupby(inflow_df["timeStamp"].dt.date)["value"].sum()
    outflow_daily = outflow_df.groupby(outflow_df["timeStamp"].dt.date)["value"].sum()

    inflow_spike = False
    outflow_spike = False

    # Require at least 7 days of activity
    if len(inflow_daily) >= 7:
        mean = inflow_daily.mean()
        std = inflow_daily.std()
        if std > 0 and inflow_daily.max() > mean + (2 * std):
            inflow_spike = True

    if len(outflow_daily) >= 7:
        mean_out = outflow_daily.mean()
        std_out = outflow_daily.std()
        if std_out > 0 and outflow_daily.max() > mean_out + (2 * std_out):
            outflow_spike = True
    print("Inflow mean:", mean if len(inflow_daily) >= 7 else "NA")
    print("Inflow std:", std if len(inflow_daily) >= 7 else "NA")
    print("Inflow max:", inflow_daily.max() if len(inflow_daily) >= 7 else "NA")

    print("Outflow mean:", mean_out if len(outflow_daily) >= 7 else "NA")
    print("Outflow std:", std_out if len(outflow_daily) >= 7 else "NA")
    print("Outflow max:", outflow_daily.max() if len(outflow_daily) >= 7 else "NA")

    return {
        "inflow_spike_detected": inflow_spike,
        "outflow_spike_detected": outflow_spike
    }