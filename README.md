# Reinforcement Learning Project

## Overview

This repository contains code for a simple reinforcement learning project using a grid world environment. The project focuses on implementing the Value Iteration algorithm to find optimal policies and values within the environment.

## Reinforcement Learning Basics

Reinforcement Learning (RL) is a subfield of machine learning where an agent learns to make decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties based on the actions it takes. The goal is to learn a policy that maximizes the cumulative reward over time.

### Value Iteration

Value Iteration is a dynamic programming algorithm used to find the optimal state values and policies in a Markov Decision Process (MDP). It involves iteratively updating the value of each state based on the expected cumulative rewards of taking each possible action.

## Project Structure

- **`GridWorld` Class:**
  - Represents the grid world environment.
  - Defines methods for initializing transition probabilities, checking terminal states, and handling valid movements.

- **`print_v` and `print_policy` Functions:**
  - Visualization functions to display the state values and policies on the grid.

- **`interate_values` Function:**
  - Implements the Value Iteration algorithm to find optimal values and policies.

- **Main Section:**
  - Sets up the grid world environment with specified dimensions, item locations, and rewards.
  - Calls the `interate_values` function to obtain optimal values and policies.
  - Visualizes the results using the `print_v` and `print_policy` functions.

## Usage

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/Suryatejakalapala/gridworld.git](https://github.com/Suryatejakalapala/gridworld.git)
    ```

2. **Navigate to the project directory:**

    ```bash
    cd gridworld
    ```

3. **Run the main script:**

    ```bash
    python grid.py
    ```

## Dependencies

- Python 3.x
- NumPy
- Matplotlib

Install dependencies using:

```bash
pip install numpy matplotlib
