def calculate_ponzi_risk(features, temporal_patterns=None, concentration=None, graph_metrics=None):
    if not features:
        return {"risk_score": 0, "risk_level": "Unknown"}

        # ---- Graph Structural Rules ----
    if graph_metrics:
        in_deg = graph_metrics.get("wallet_in_degree", 0)
        out_deg = graph_metrics.get("wallet_out_degree", 1)

        if out_deg > 0:
            ratio = in_deg / out_deg
        else:
            ratio = in_deg

        if in_deg > 30 and ratio > 5:
            score += 30
    
    score = 0
    if concentration:
        if concentration.get("concentration_flag"):
            score += 25

        if concentration.get("top3_outflow_percentage", 0) > 85:
            score += 15
    # ---- Static Behavioral Rules ----

    ratio = features.get("inflow_outflow_ratio")
    if ratio and ratio > 1.5:
        score += 20

    if features.get("unique_senders", 0) > 50:
        score += 15

    if features.get("unique_receivers", 0) < 5:
        score += 15

    if features.get("transactions_per_day", 0) > 10:
        score += 15

    if features.get("net_flow_eth", 0) > 100:
        score += 10

    # ---- Temporal Anomaly Rules ----

    if temporal_patterns:
        if temporal_patterns.get("inflow_spike_detected"):
            score += 5

        if temporal_patterns.get("outflow_spike_detected"):
            score += 10

        if (temporal_patterns.get("inflow_spike_detected") and 
            temporal_patterns.get("outflow_spike_detected")):
            score += 5

    # ---- Normalize ----
    if score > 100:
        score = 100

    # ---- Risk Level ----
    if score >= 70:
        level = "High Risk"
    elif score >= 40:
        level = "Medium Risk"
    else:
        level = "Low Risk"

    return {
        "risk_score": score,
        "risk_level": level
    }