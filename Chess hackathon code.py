import chess.pgn
import networkx as nx
import matplotlib.pyplot as plt

# Function to add edges to the graph based on game outcomes
def add_game_to_graph(graph, game):
    white = game.headers["White"]
    black = game.headers["Black"]
    result = game.headers["Result"]
    # Add edges for both winner and loser; ignore draws
    if result == '0-1':
        graph.add_edge(white, black)  # White lost to Black
        graph.add_edge(black, white, win=True)  # Black won against White
    elif result == '1-0':
        graph.add_edge(black, white)  # Black lost to White
        graph.add_edge(white, black, win=True)  # White won against Black

# Create a directed graph
player_graph = nx.DiGraph()

# Open the PGN file
with open(r"C:\small_pgn\selected_10000_games.pgn") as pgn:
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        add_game_to_graph(player_graph, game)

# Function to find a connection and visualize it
def find_connection_and_visualize(graph, start_player, target_player):
    try:
        path = nx.shortest_path(graph, start_player, target_player)
        subgraph = graph.subgraph(path)
        plt.figure(figsize=(10, 6))
        nx.draw(subgraph, with_labels=True, node_color='lightblue', 
                node_size=2000, edge_color='gray', linewidths=2, 
                font_size=15, arrows=True, arrowstyle='->', 
                arrowsize=10)
        plt.title(f"Connection from {start_player} to {target_player}")
        plt.show()
        return path
    except nx.NetworkXNoPath:
        print(f"No connection found between {start_player} and {target_player} based on game outcomes.")
        return None

# Example usage
start_player = "Evill"
#target_player = "zinder2"
#target_player = "Hakopasa"
target_player = "Incinerator"

connection = find_connection_and_visualize(player_graph, start_player, target_player)