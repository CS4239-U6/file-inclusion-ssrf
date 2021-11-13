FROM ubuntu:latest

# Install update.
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Copy files over
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt
RUN mkdir temp
RUN echo 'You found it!!' >> /etc/passwd

EXPOSE 5000

ENTRYPOINT [ "python3", "VulnerableServer" ]