# Gita ChatBot using Llama-2-7B-Chat


Here's a brief overview of the components of the repository:

- `app.py`: The Streamlit web application code that allows users to interact with the chatbot through a simple user interface.

- `llama-2-7b-chat.ggmlv3.q2_K.bin`:  Quantized model weights provided by TheBloke. It can be downloaded via 

```
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q2_K.bin
```
  We can also use any other model. Just write the model name in the ChatModel Function.

- `Dockerfile`: The Dockerfile containerises the application for easy deployment and management.

- `docker-compose.yml`: A Docker Compose file simplifies the chatbot deployment as a Docker container.

- `requirements.txt`: Contains a list of Python dependencies required to run the application.

## Prerequisites

Before running the Gita ChatBot, you need to have the following installed:

1. Python
2. Docker

## Installation

To set up the chatbot locally, follow these steps:

1. Clone this repository to your local machine using Git:

```bash
git clone https://github.com/Amank2854/Llama-ChatBot.git
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
venv/Scripts/activate  
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the Gita ChatBot, execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the chatbot interface by opening your web browser and navigating to `http://localhost:8501`.

Simply type your messages in the input box and press "Enter" to send them to the chatbot. The chatbot will respond based on the context of the conversation, thanks to its memory capabilities.

## Docker Compose

If you prefer to deploy the chatbot using Docker Compose, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your system.

2. Start the container using Docker Compose:

```bash
docker-compose up -d
```

The chatbot will be accessible at `http://localhost:8501` in your web browser.
