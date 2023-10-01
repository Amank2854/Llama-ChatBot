# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY ./ ./


# Download the file from the URL and add it to the working directory
RUN apt-get update && apt-get install -y wget

RUN wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q2_K.bin

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]