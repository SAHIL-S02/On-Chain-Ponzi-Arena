from eth_connection import is_connected
from transaction_fetcher import get_wallet_transactions
from feature_engine import extract_wallet_features
from risk_engine import calculate_ponzi_risk
from temporal_analyzer import detect_temporal_patterns
from concentration_analyzer import calculate_outflow_concentration
from graph_analyzer import analyze_wallet_graph
if __name__ == "__main__":
    print("Ethereum Connected:", is_connected())

    test_wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

    txs = get_wallet_transactions(test_wallet)

    print(f"Fetched {len(txs)} transactions")

    features = extract_wallet_features(txs, test_wallet)

    print("\nWallet Behavioral Features:")
    for k, v in features.items():
        print(f"{k}: {v}")
    
    temporal = detect_temporal_patterns(txs, test_wallet)

    print("\nTemporal Analysis:")
    for k, v in temporal.items():
        print(f"{k}: {v}")
    concentration = calculate_outflow_concentration(txs, test_wallet)

    print("\nOutflow Concentration Analysis:")
    for k, v in concentration.items():
        print(f"{k}: {v}")
    

    print("\nTemporal Analysis:")
    for k, v in temporal.items():
        print(f"{k}: {v}")
    
    graph_metrics = analyze_wallet_graph(txs, test_wallet)

    print("\nGraph Analysis:")
    for k, v in graph_metrics.items():
        print(f"{k}: {v}")
        
    risk = calculate_ponzi_risk(features, temporal, concentration, graph_metrics)

    print("\nPonzi Risk Assessment:")
    print("Risk Score:", risk["risk_score"])
    print("Risk Level:", risk["risk_level"])
    temporal = detect_temporal_patterns(txs, test_wallet)