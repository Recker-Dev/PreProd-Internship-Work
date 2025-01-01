# Deep Q-Network (DQN) for CartPole-v1

This project demonstrates the implementation of a Deep Q-Network (DQN) to solve the classic CartPole-v1 environment from OpenAI Gym.

## Description

The DQN agent learns to balance a pole on a cart by taking discrete actions (left or right). It utilizes a neural network to approximate the Q-function, which estimates the expected future rewards for each action in a given state. The agent is trained using experience replay and a target network to stabilize the learning process.

## Additional Learning Resources

Below are some helpful resources for understanding DQN (Deep Q-Network), the SeLU activation function, and coding a DQN model:

### Understanding DQN [Theory]

Gain a theoretical understanding of DQN and how it works in reinforcement learning.

- [Watch here](https://youtu.be/x83WmvbRa2I?si=qUBOc9s--_-TRxOb)

### Coding a DQN (SentDex Series)

A hands-on tutorial by SentDex that walks through implementing a DQN. Although it uses a different architecture and approach, it provides great insights into building a DQN model.

- **Part 1:** [Watch here](https://youtu.be/t3fbETsIBCY?si=YVRa-qdPH2Ayqs-Z)
- **Part 2:** [Watch here](https://youtu.be/qfovbG84EBg?si=zjTuFFVSae5mDIsw)

### Understanding SeLU Activation Function Used in Model Architecture

Learn about the SeLU activation function, its properties, and its role in the model architecture.

- [Watch here](https://youtu.be/2OwWs7Hzr9g?si=RlLPiwLWN0pITEVD)

## IMPORTANT NOTE

**Recommended Environment:**

This project was developed primarily in Google Colab, but later moved to a local machine and tested within a virtual environment. It worked perfectly, even with Gym in render mode. However, smooth installation of the dependencies listed in the `requirements.txt` file is extremely important for optimal performance.

If you face issues running the project locally, we recommend moving the codebase to Google Colab for better compatibility. Keep in mind, this might mean sacrificing the Gym render capability. Here's how you can set it up:

1. Place the contents of the project folder in your Google Drive.
2. Mount your Google Drive in Colab.
3. Configure the paths properly, for example: `/content/drive/MyDrive/Project/Path/to/trained_weights/policy_net.pth`

## Important Note on Using and Understanding the Code

### Recommended Approach

If you want to **understand the code** thoroughly, it is advised to first go through the recommended watch series provided above. These resources will help you grasp the theoretical and practical aspects of DQNs, making the code more intuitive and easier to follow.

### Quick Playaround

If you just want to **play around with the code**, you can directly use the `TestDQN` script to explore and experiment with the model{both in render and non-render mode}. However, note that this approach assumes a basic understanding of DQNs and the provided codebase.

### Configuration Reminder

In either case, it is **important to configure the path to the weights folder properly**, whether you are using a local Jupyter environment or Google Colab. Failure to do so may result in errors when loading or saving model weights.

## Setting Up a Virtual Environment

To ensure compatibility and manage dependencies for this project, it’s recommended to set up a virtual environment. This will allow you to isolate project dependencies from your system-wide packages and ensure that the project runs smoothly.

Follow the steps below to create and activate a virtual environment, and install the necessary dependencies:

### 1. **Create a Virtual Environment**

For Conda users:

- Open your terminal/command prompt and run the following command to create a virtual environment with Python 3.10:

  ```bash
  conda create --name rein_env python=3.10 -y
  ```

  This command will create a new Conda environment named `rein_env` with Python version 3.10. The `-y` flag automatically confirms the action.

### 2. **Activate the Virtual Environment**

Once the environment is created, activate it with the following command:

```bash
conda activate rein_env
```

### 3. **Install Project Dependencies**

With the environment activated, install all the required dependencies listed in the requirements.txt file. This can be done with the following command:

```bash
pip install -r requirements.txt
```

### 4. **Deactivating the Virtual Environment**

```bash
conda deactivate
```

## Requirements

- Python 3.10
- torch==2.5.0
- torchvision==0.20.0
- torchaudio==2.5.0
- gym==0.25.2
- gym-notices==0.0.8
- numpy==1.26.4
- ipykernel==5.5.6
- gym[classic_control]

## Code Flow

<img src="DQN Code Flowchart.png" alt="Flowchart" width="600">
<!-- (Replace `DQN Code Flowchart.png` with the actual path to your flowchart image) -->

## Results

The trained DQN agent achieves a high score and successfully balances the pole for an extended period. You can observe the agent's performance by running the testing script after training, or use the weights given by us.

## Folder Structure

```
└── root
├── Code
| ├── trained_weights
│ | ├── policy_net.pth
| ├── TestDQN.ipynb
| ├── TrainDQN.ipynb
| ├── model.py
├── DQN_documentation.pdf
├── prompts.md
├── README.md
├── requirements.txt
├── requirements_frozen_from_colab.txt
└── DQN Code Flowchart.png
```
