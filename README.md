 Minimax_simulator
MINIMAX algorithm and AlphaBeta Prunning

 🤖 Minimax & AlphaBeta Pruning Simulator

An interactive Artificial Intelligence gamesearch simulator developed using Python and Streamlit.

The application allows students to enter gametree values and visually understand how the Minimax algorithm and AlphaBeta Pruning work.



 🎯 Features

 🌳 Graphical gametree visualization
 🤖 Minimax algorithm simulation
 ✂️ AlphaBeta pruning simulation
 📊 Userdefined leafnode values
 🔢 Configurable tree depth
 🏆 Displays the optimal value
 🎯 Displays the best move
 📈 Displays the number of nodes visited
 ✂️ Displays the number of nodes pruned
 🔴 Highlights pruned branches
 💻 Simple Streamlit web interface
 🚀 Easy deployment using GitHub and Streamlit Community Cloud



 🧠 Algorithms

 1. Minimax

Minimax is a decisionmaking algorithm used in twoplayer games.

The algorithm assumes

 MAX player tries to maximize the score.
 MIN player tries to minimize the score.

Example


                 MAX
                    
             MIN     MIN
                     
           3    5   2    9


MIN chooses


MIN(3,5) = 3
MIN(2,9) = 2


Then MAX chooses


MAX(3,2) = 3


Therefore


Optimal Value = 3




 2. AlphaBeta Pruning

AlphaBeta Pruning is an optimization of Minimax.

It avoids evaluating branches that cannot influence the final decision.

The two important values are


α (Alpha) = Best value found so far for MAX

β (Beta)  = Best value found so far for MIN


When


α ≥ β


the remaining branch can be skipped.

This reduces the number of nodes that need to be evaluated.



 📁 Project Structure


MinimaxSimulator
│
├── app.py
│       Main Streamlit application
│
├── minimax.py
│       Minimax and AlphaBeta algorithms
│
├── tree_visualizer.py
│       Graphical tree generation
│
├── requirements.txt
│       Python dependencies
│
└── README.md
       Project documentation




 💻 Requirements

The project requires

 Python 3.9 or higher
 Streamlit
 NetworkX
 Matplotlib
 A web browser

No database is required.

No API key is required.



 ⚙️ Local Installation

 Step 1 — Clone the repository

bash
git clone httpsgithub.comYOUR_USERNAMEMinimaxSimulator.git


Move into the project

bash
cd MinimaxSimulator




 Step 2 — Install dependencies

Run

bash
pip install r requirements.txt




 Step 3 — Run the application

bash
streamlit run app.py


The application will open in your browser.

Usually Streamlit runs at


httplocalhost8501




 🧪 Example

Select


Algorithm Minimax
Tree Depth 2


Enter


3 5 2 9


The generated tree is


                 MAX
                    
             MIN     MIN
                     
           3    5   2    9


The algorithm evaluates the tree and determines the optimal value.

Now select


AlphaBeta Pruning


and run the same example.

The application will display

 Optimal value
 Nodes visited
 Nodes pruned
 Graphical tree



 📊 Tree Depth

The number of required leaf values depends on the tree depth.

 Depth  Leaf Nodes 

 1  2 
 2  4 
 3  8 
 4  16 
 5  32 

For example


Depth = 3


requires


8 leaf values


Example


3 5 2 9 12 5 23 4




 🌳 Graphical Visualization

The application generates a graphical representation of the game tree.

MAX and MIN levels are displayed in the tree.

For AlphaBeta Pruning, branches that are skipped during the search are identified as pruned branches.

This makes the application useful for understanding the difference between


Minimax


and


Minimax + AlphaBeta Pruning




 🚀 Deploy on Streamlit Community Cloud

 Step 1 — Create a GitHub repository

Go to GitHub and create a new repository.

For example


MinimaxSimulator




 Step 2 — Upload these files

Upload


app.py
minimax.py
tree_visualizer.py
requirements.txt
README.md


Your repository should look like


MinimaxSimulator
│
├── app.py
├── minimax.py
├── tree_visualizer.py
├── requirements.txt
└── README.md




 Step 3 — Open Streamlit Community Cloud

Go to

httpsshare.streamlit.io

Sign in using your GitHub account.



 Step 4 — Create a new app

Select


Create app


Choose your GitHub repository


YOUR_USERNAME  MinimaxSimulator


Select the branch


main


For the main file, select


app.py


Then deploy the application.



 🎉 Deployment

After deployment, Streamlit will provide a public URL similar to


httpsyourprojectname.streamlit.app


You can share this URL with

 Students
 Teachers
 College faculty
 Friends
 Researchers

No Python installation is required for users accessing the deployed application.



 🎓 Educational Purpose

This simulator is designed primarily for learning and teaching Artificial Intelligence gamesearch algorithms.

Students can experiment with different leafnode values and observe how the decision changes.

It is particularly useful for understanding

 Game trees
 MAX nodes
 MIN nodes
 Minimax
 AlphaBeta pruning
 Alpha values
 Beta values
 Optimal decisions
 Searchspace reduction



 🔬 Suggested Classroom Experiment

Use the following values


3 5 2 9 12 5 23 4


Run


Minimax


Record


Optimal Value
Nodes Visited


Then run


AlphaBeta Pruning


Record


Optimal Value
Nodes Visited
Nodes Pruned


Compare the results.

The purpose is to demonstrate that AlphaBeta Pruning can obtain the same optimal decision while potentially evaluating fewer nodes.



 🛠️ Technologies Used

 Technology  Purpose 

 Python  Core programming 
 Streamlit  Web interface 
 NetworkX  Graph representation 
 Matplotlib  Tree visualization 
 GitHub  Sourcecode hosting 
 Streamlit Community Cloud  Deployment 



 📜 License

This project is intended for educational and academic use.

You are free to modify and extend the project for learning, teaching, and academic demonstrations.



 👨‍💻 Author

Tathagata Roy Chowdhury

Department of Computer Science and Engineering



 ⭐ Future Enhancements

Possible future versions can include

 Interactive node creation
 Manual tree drawing
 Stepbystep Minimax execution
 Stepbystep AlphaBeta execution
 Animated pruning
 Alpha and Beta values displayed beside nodes
 Game examples such as TicTacToe
 Chesslike gametree demonstration
 Searchdepth comparison
 Minimax vs AlphaBeta performance graph
 Downloadable execution report



 ⭐ If you find this project useful

Star the GitHub repository and use it for your AI laboratory, classroom demonstrations, and student practice.
