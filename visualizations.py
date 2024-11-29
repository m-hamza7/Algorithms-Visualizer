
import networkx as nx
import matplotlib.pyplot as plt

def visualize_closest_pair(points, closest_pair, distance):
    """
    Visualizes the closest pair of points.
    
    :param points: List of all points [(x1, y1), (x2, y2), ...].
    :param closest_pair: The closest pair of points [(x1, y1), (x2, y2)].
    :param distance: The distance between the closest pair of points.
    """
    x_coords, y_coords = zip(*points)
    
    # Plot all points
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, label="Points", color="blue")
    
    # Highlight closest pair
    closest_x, closest_y = zip(*closest_pair)
    plt.scatter(closest_x, closest_y, color="red", label="Closest Pair", zorder=5)
    plt.plot(closest_x, closest_y, color="green", linestyle="--", linewidth=2, label=f"Distance: {distance:.2f}")
    
    # Labels and legend
    plt.title("Closest Pair Visualization")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.show()

def visualize_karatsuba_tree(tree):
    """
    Visualizes the recursion tree for Karatsuba multiplication.
    
    :param tree: Dictionary representing the recursion tree.
                 Example: {"inputs": (123, 456), "result": 56088, "children": [...]}
    """
    G = nx.DiGraph()
    pos = {}

    def add_nodes(tree, parent=None, depth=0, offset=0):
        node_label = f"{tree['inputs'][0]} x {tree['inputs'][1]} = {tree['result']}"
        node_id = id(tree)
        pos[node_id] = (offset, -depth)
        
        G.add_node(node_id, label=node_label)
        if parent is not None:
            G.add_edge(parent, node_id)
        
        # Add child nodes recursively
        num_children = len(tree.get("children", []))
        for i, child in enumerate(tree.get("children", [])):
            add_nodes(child, node_id, depth + 1, offset + (i - (num_children - 1) / 2) * 2)

    # Build graph
    add_nodes(tree)
    
    # Draw graph
    labels = nx.get_node_attributes(G, "label")
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color="lightblue", font_size=8, font_weight="bold", font_color="black")
    plt.title("Karatsuba Recursion Tree Visualization")
    plt.show()
