# tree_visualizer.py

import matplotlib.pyplot as plt
import networkx as nx


def create_graph(node, graph=None, parent=None, node_id=0,
                 depth=0, path="Root",
                 pruned_paths=None):

    if graph is None:
        graph = nx.DiGraph()

    if pruned_paths is None:
        pruned_paths = []

    current_id = node_id

    # Node label
    if depth == 0:
        label = f"MAX\n{node['value']}"
    else:
        if depth % 2 == 1:
            label = f"MIN\n{node['value']}"
        else:
            label = f"MAX\n{node['value']}"

    graph.add_node(
        current_id,
        label=label,
        path=path
    )

    if parent is not None:
        graph.add_edge(parent, current_id)

    next_id = current_id + 1

    for i, child in enumerate(node["children"]):

        child_path = path + f" -> {i}"

        graph, next_id = create_graph(
            child,
            graph,
            current_id,
            next_id,
            depth + 1,
            child_path,
            pruned_paths
        )

    return graph, next_id


def draw_tree(root, pruned_paths=None):

    if pruned_paths is None:
        pruned_paths = []

    graph, _ = create_graph(
        root,
        pruned_paths=pruned_paths
    )

    labels = nx.get_node_attributes(
        graph,
        "label"
    )

    paths = nx.get_node_attributes(
        graph,
        "path"
    )

    plt.figure(figsize=(14, 8))

    # Tree layout
    pos = nx.spring_layout(
        graph,
        seed=42,
        k=2.5
    )

    node_colors = []

    for node in graph.nodes:

        node_path = paths[node]

        is_pruned = False

        for p in pruned_paths:

            if node_path == p or node_path.startswith(p):

                is_pruned = True
                break

        if is_pruned:
            node_colors.append("lightcoral")
        else:
            node_colors.append("lightblue")

    nx.draw_networkx_edges(
        graph,
        pos,
        arrows=False,
        width=2
    )

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_color=node_colors,
        node_size=2200,
        edgecolors="black",
        linewidths=2
    )

    nx.draw_networkx_labels(
        graph,
        pos,
        labels=labels,
        font_size=9,
        font_weight="bold"
    )

    plt.axis("off")

    return plt.gcf()