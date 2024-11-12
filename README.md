# HTTPHealthCheck
## Description

Welcome to the HTTP Health Check project! This repository contains a Python-based program that monitors the health of a set of HTTP endpoints by periodically sending HTTP requests and checking their status. Designed to be configurable and efficient, the program accepts a YAML configuration file that lists the endpoints to monitor, including options for HTTP method, headers, and request body. In this walkthrough we use VS Code as our IDE but feel free to use the IDE of your choice.

</b>

### Features

- <b>Configurable Endpoint Monitoring:</b> Accepts a YAML configuration file that specifies multiple HTTP endpoints, each with configurable options such as HTTP method, headers, and request body.

- <b>Health Checking:</b> Sends HTTP requests to each endpoint every 15 seconds (configurable) and determines if each endpoint is UP or DOWN based on response status codes and latency.

- <b>Structured Logging:</b> Logs each health check result and provides availability metrics for each endpoint over time.

- <b>Concurrent Request Handling:</b> Uses threading to handle multiple endpoints simultaneously, improving efficiency for larger endpoint sets.

- <b>Availability Statistics:</b> Calculates and logs the availability percentage of each endpoint over the program's runtime.

</b>

### Languages

- <b>Bash</b>
- <b>Python</b>

# Getting Started

- Download python. If you are having trouble, use the information under the "Install a Python Interpreter" section of [this link]([url](https://code.visualstudio.com/docs/python/python-tutorial))
- Also, install the Python extension found under VS Code > Extensions > "Python" ![Pythonextension1](https://github.com/user-attachments/assets/a63d33fe-25db-4dc3-93ff-1a8a9000d35f)
- Note: If you are using an IDE seperate from VS Code please follow the instructions for downloading Python provided in the literature for your IDE.

  
