import pandas as pd
import networkx as nx

def analyze_wallet_graph(transactions, wallet_address):
    if not transactions:
        return {}

    df = pd.DataFrame(transactions)
    df["value"] = df["value"].astype(float) / 1e18

    wallet_address = wallet_address.lower()

    # Create directed graph
    G = nx.DiGraph()

    for _, row in df.iterrows():
        sender = row["from"].lower()
        receiver = row["to"].lower()
        value = row["value"]

        if sender and receiver:
            if G.has_edge(sender, receiver):
                G[sender][receiver]["weight"] += value
            else:
                G.add_edge(sender, receiver, weight=value)

    # Centrality measures
    degree_centrality = nx.degree_centrality(G)
    in_degree = G.in_degree(wallet_address)
    out_degree = G.out_degree(wallet_address)

    return {
        "graph_nodes": G.number_of_nodes(),
        "graph_edges": G.number_of_edges(),
        "wallet_in_degree": in_degree,
        "wallet_out_degree": out_degree,
        "wallet_degree_centrality": round(degree_centrality.get(wallet_address, 0), 4)
    }