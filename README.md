# Monte Carlo Simulation

Monte Carlo Simulation is a computational technique that uses random sampling to solve probabilistic and mathematical problems. The core idea is to simulate numerous possible outcomes and use statistical analysis to estimate the result.

Steps:

1. Define the problem
2. Generate random sample - random values based on the probability distribution
3. Run simulation - Repeat the process multiple times
4. Analyze results
<br>

## Monte Carlo $\pi$ Approximation

Approximating $\pi$ can be done with Monte Carlo simulation. This can be done by randomly sampling points within a square and checking how many fall inside the circle.

![Run `main.py` to view this result](./pi-approximation.png)

Run `main.py` to view this result

- Consider a unit square (1 x 1) with a circle with radius 1 inside it with the same centre point.
- Generate random points $(x, y)$ where $x$ and $y$ are uniformly sampled between $[-1, 1]$.
- Then we can count how many points fall inside the circle with the condition $x^2 + y^2 \leq 1$. This helps us calculate $P(\text{points inside cricle})=\dfrac{\text{num of points inside circle}}{\text{num of total points}}$.
- Note that the ratio of the $A_{circle}$ to the $A_{square}$  is $\dfrac{\pi}{4}$.
- Then we can approximate $P(\text{points inside cricle})=\dfrac{\text{num of points inside circle}}{\text{num of total points}}\approx \dfrac{\pi}{4} \implies \pi \approx 4 \cdot \dfrac{\text{num of points inside circle}}{\text{num of total points}}$
- Above image shows that when `n = 2560000`, `pi = 3.14165` which is accurate to its 100th decimal place. The 9 approximations with `n` being doubled shows how increasing the num of samples improves the accuracy.
<br>

## Monte Carlo in Reinforcement Learning

Monte Carlo plays an important role in RL, especially in the part where the agent interacts with an environment to maximize cumulative rewards. It’s primarily used in value estimation and policy improvement. 
<br>

### Key Applications in RL

- Value Function Estimation - Evaluating state-action pairs by running multiple episodes and averaging their returns.
- Policy Evaluation & Improvement - Simulating actions using different policies → determine which one performs the best.
- Exploration - Randomized action selection to explore the environment.
<br>

### Example of Monte Carlo in RL

For example, if we want to train a robot to exit a maze, we can use MC with RL. Let’s consider:

The robot is placed in a maze, and needs to learn the best path to exit.

- It can move up, down, left, right
- Some paths may have obstacles/penalties
- Robot does not know the environment at first

1. Start with random movement - randomly move around the maze (may hit the wall/obstacle/dead ends)
2. Complete episodes (start-end process)
3. Record rewards for each action (path taken)
4. Compute average returns - after many episodes, the robot calculates which action led faster and safer paths ← Monte Carlo
5. Policy is updated 
<br>

### Monte Carlo Tree Decision

MCTS (MCT Search) is a search algorithm used for decision making in turn based games and planning problems. It builds a search tree by also using random simulations to evaluate future moves and progressively improves on making the decision over time.

1. Selection - Navigate the tree using exploitation (good moves) and exploration (moves that it didn’t try out much)
2. Expansion - Add new possible moves to the tree (as a node)
3. Simulation - Play a random game from that node until the end (terminal state)
4. Backpropagation - Update the tree with the result → reinforcement of the good moves

- MC: Randomly try different routes and after many times, calculate the avg fastest route
- MCTS: Instead of trying all possible routes, gradually explore. Start randomly but remember the good ones and explore more starting from that point.

- MCTS was used by DeepMind for AlphaGO!
