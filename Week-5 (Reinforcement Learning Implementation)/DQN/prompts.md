# DQN Training with LLMs: Prompts for Understanding and Customization

## Understanding DQN

**Prompt 1:** Explain the core concepts of Deep Q-Networks (DQN) and how they are used in reinforcement learning.

**Prompt 2:** What is the role of the replay memory in DQN? How does it improve the learning process?

**Prompt 3:** Describe the difference between the policy network and the target network in DQN. Why is this distinction important?

**Prompt 4:** Explain the Bellman equation and its significance in the DQN update rule.

**Prompt 5:** What is epsilon-greedy exploration and how does it balance exploration and exploitation in DQN?

## Understanding the Code

**Prompt 6:** Analyze the provided Python code and explain the functionality of the `Model` class. What type of neural network is it defining?

**Prompt 7:** Describe the purpose of the `get_action` function. How does it implement the epsilon-greedy policy?

**Prompt 8:** How does the `optimize_model` function update the policy network's weights using experiences from the replay memory?

**Prompt 9:** Explain the role of the `target_update_delay` parameter in the training process. Why is it necessary to periodically update the target network?

**Prompt 10:** What is the purpose of the `state_reward` function and how does it modify the environment's reward signal?

## Customizing DQN

**Prompt 11:** Modify the `Model` class to implement a convolutional neural network (CNN) architecture instead of a fully connected network.

**Prompt 12:** Implement a prioritized experience replay mechanism to improve the efficiency of the replay memory.

**Prompt 13:** Adapt the code to work with a different OpenAI Gym environment, such as 'LunarLander-v2'.

**Prompt 14:** Experiment with different hyperparameters, such as the learning rate, discount factor, and epsilon decay rate, to optimize the DQN's performance.

**Prompt 15:** Implement a Double DQN (DDQN) algorithm to address the overestimation bias in Q-learning.

## Important Functions

**Prompt 16:** Explain the purpose and implementation of the `get_states_tensor` function.

**Prompt 17:** How does the `normalize_state` function contribute to the stability of the training process?

**Prompt 18:** Describe the functionality of the `fit` function and how it trains the policy network.

**Prompt 19:** What is the role of the `train_one_episode` function in the overall training loop?

**Prompt 20:** How does the `test` function evaluate the performance of the trained model?

