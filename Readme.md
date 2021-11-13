# File Inclusion

An attacker can use Local File Inclusion (LFI) to trick the web application into exposing or running files on the web server.


# Quick start guide
1. Clone the repo
2. Build the docker image using `docker build -t lfi .`
3. Run the docker image using `docker run -dt -p 5000:5000 lfi`
4. The server is now on [`localhost:5000`](http://localhost:5000)

# Defenses

## Proper input validation

Filter user inputs and make sure that filepath is correct.


## Create a whitelist

Whitelist what can be included within a whitelist to prevent other files from being read.