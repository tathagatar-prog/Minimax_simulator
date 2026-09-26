# app.py

import streamlit as st

from minimax import (
    create_tree,
    minimax,
    alpha_beta
)

from tree_visualizer import draw_tree


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Minimax & Alpha-Beta Simulator",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🤖 Minimax & Alpha-Beta Pruning Simulator")

st.markdown(
    """
    ### Artificial Intelligence Game Search Simulator

    Enter the values of the leaf nodes and visualize how
    **Minimax** and **Alpha-Beta Pruning** make decisions.
    """
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.header("⚙️ Tree Configuration")


algorithm = st.sidebar.radio(
    "Select Algorithm",
    [
        "Minimax",
        "Alpha-Beta Pruning"
    ]
)


depth = st.sidebar.number_input(
    "Tree Depth",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)


# Number of leaves
number_of_leaves = 2 ** depth


st.sidebar.info(
    f"Required leaf values: {number_of_leaves}"
)


# ---------------------------------------------------------
# LEAF VALUES
# ---------------------------------------------------------

st.subheader("📊 Enter Leaf Node Values")

default_values = []

for i in range(number_of_leaves):

    default_values.append(
        i + 1
    )


values_text = st.text_input(
    "Enter values separated by spaces",
    value=" ".join(
        map(str, default_values)
    )
)


# ---------------------------------------------------------
# RUN BUTTON
# ---------------------------------------------------------

run = st.button(
    "▶️ Run Algorithm",
    use_container_width=True
)


# ---------------------------------------------------------
# PROCESS
# ---------------------------------------------------------

if run:

    try:

        values = list(
            map(
                int,
                values_text.split()
            )
        )

    except ValueError:

        st.error(
            "❌ Please enter only integer values."
        )

        st.stop()


    if len(values) != number_of_leaves:

        st.error(
            f"❌ Please enter exactly "
            f"{number_of_leaves} values."
        )

        st.stop()


    # Create tree
    root = create_tree(values)


    # -----------------------------------------------------
    # RUN MINIMAX
    # -----------------------------------------------------

    if algorithm == "Minimax":

        result, visited, best_path = minimax(
            root,
            depth,
            True
        )

        pruned = []


    # -----------------------------------------------------
    # RUN ALPHA BETA
    # -----------------------------------------------------

    else:

        result, visited, best_path, pruned = alpha_beta(
            root,
            depth,
            True
        )


    # -----------------------------------------------------
    # RESULTS
    # -----------------------------------------------------

    st.subheader("📌 Algorithm Result")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Optimal Value",
            result
        )


    with col2:

        st.metric(
            "Nodes Visited",
            visited
        )


    with col3:

        st.metric(
            "Nodes Pruned",
            len(pruned)
        )


    # -----------------------------------------------------
    # BEST MOVE
    # -----------------------------------------------------

    if best_path:

        first_move = best_path[0]

        if first_move == 0:

            move = "LEFT"

        else:

            move = "RIGHT"

        st.success(
            f"🏆 Best Move: **{move}**"
        )


    # -----------------------------------------------------
    # TREE
    # -----------------------------------------------------

    st.subheader(
        "🌳 Graphical Game Tree"
    )


    figure = draw_tree(
        root,
        pruned
    )


    st.pyplot(
        figure,
        use_container_width=True
    )


    # -----------------------------------------------------
    # EXPLANATION
    # -----------------------------------------------------

    st.subheader(
        "📖 Execution Information"
    )


    if algorithm == "Minimax":

        st.info(
            """
            **Minimax** examines all possible game states.

            • MAX tries to maximize the value.

            • MIN tries to minimize the value.

            • No branches are skipped.

            Therefore, all required nodes are evaluated.
            """
        )

    else:

        st.info(
            """
            **Alpha-Beta Pruning** improves Minimax.

            • α represents the best value found by MAX.

            • β represents the best value found by MIN.

            • When α ≥ β, remaining branches can be ignored.

            🔴 Red nodes represent branches affected by pruning.
            """
        )


# ---------------------------------------------------------
# INSTRUCTIONS
# ---------------------------------------------------------

st.divider()

st.subheader("🧑‍🎓 How to Use")

st.markdown(
    """
    **Example**

    Select:

    `Tree Depth = 2`

    Enter:

    `3 5 2 9`

    The tree becomes:

    ```text
              MAX
             /   \\
           MIN    MIN
           / \\    / \\
          3   5  2   9
    ```

    Then select:

    **Minimax**

    or

    **Alpha-Beta Pruning**

    and click **Run Algorithm**.

    The application will calculate the optimal value and
    display the search tree graphically.
    """
)