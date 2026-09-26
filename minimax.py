# minimax.py

import math


# ---------------------------------------------------------
# MINIMAX
# ---------------------------------------------------------

def minimax(node, depth, maximizing_player, path="Root"):
    """
    Performs Minimax on a complete binary tree.

    node format:
        {
            "value": value,
            "children": [...]
        }
    """

    # Leaf node
    if depth == 0 or not node["children"]:
        return node["value"], 1, []


    visited = 1
    best_path = []

    if maximizing_player:

        best_value = -math.inf

        for i, child in enumerate(node["children"]):

            value, count, child_path = minimax(
                child,
                depth - 1,
                False,
                path + f" -> {i}"
            )

            visited += count

            if value > best_value:
                best_value = value
                best_path = [i] + child_path

        return best_value, visited, best_path

    else:

        best_value = math.inf

        for i, child in enumerate(node["children"]):

            value, count, child_path = minimax(
                child,
                depth - 1,
                True,
                path + f" -> {i}"
            )

            visited += count

            if value < best_value:
                best_value = value
                best_path = [i] + child_path

        return best_value, visited, best_path


# ---------------------------------------------------------
# ALPHA BETA PRUNING
# ---------------------------------------------------------

def alpha_beta(
    node,
    depth,
    maximizing_player,
    alpha=-math.inf,
    beta=math.inf,
    path="Root"
):

    # Leaf node
    if depth == 0 or not node["children"]:
        return node["value"], 1, [], []


    visited = 1
    pruned = []
    best_path = []

    if maximizing_player:

        best_value = -math.inf

        for i, child in enumerate(node["children"]):

            value, count, child_path, child_pruned = alpha_beta(
                child,
                depth - 1,
                False,
                alpha,
                beta,
                path + f" -> {i}"
            )

            visited += count
            pruned.extend(child_pruned)

            if value > best_value:
                best_value = value
                best_path = [i] + child_path

            alpha = max(alpha, best_value)

            # PRUNING
            if beta <= alpha:

                for remaining in range(i + 1, len(node["children"])):
                    pruned.append(
                        path + f" -> {remaining}"
                    )

                break

        return best_value, visited, best_path, pruned

    else:

        best_value = math.inf

        for i, child in enumerate(node["children"]):

            value, count, child_path, child_pruned = alpha_beta(
                child,
                depth - 1,
                True,
                alpha,
                beta,
                path + f" -> {i}"
            )

            visited += count
            pruned.extend(child_pruned)

            if value < best_value:
                best_value = value
                best_path = [i] + child_path

            beta = min(beta, best_value)

            # PRUNING
            if beta <= alpha:

                for remaining in range(i + 1, len(node["children"])):
                    pruned.append(
                        path + f" -> {remaining}"
                    )

                break

        return best_value, visited, best_path, pruned


# ---------------------------------------------------------
# CREATE BINARY TREE
# ---------------------------------------------------------

def create_tree(values):

    nodes = []

    for value in values:
        nodes.append({
            "value": value,
            "children": []
        })

    # Build tree bottom-up
    for i in range(len(nodes) - 1, -1, -1):

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i]["children"].append(nodes[left])

        if right < len(nodes):
            nodes[i]["children"].append(nodes[right])

    return nodes[0]