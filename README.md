# HTTPHealthCheck
## Description

Welcome to the HTTP Health Check project! This repository contains a Python-based program that monitors the health of a set of HTTP endpoints by periodically sending HTTP requests and checking their status. Designed to be configurable and efficient, the program accepts a YAML configuration file that lists the endpoints to monitor, including options for HTTP method, headers, and request body. In this walkthrough we use VS Code as our IDE (Integrated Development Environment) but feel free to use the IDE of your choice. It will, however, be easier to follow along if you use the same IDE.

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
- Also, install the Python extension found under VS Code > Extensions > "Python" ![Screenshot 2024-11-11 at 6 33 50 PM](https://github.com/user-attachments/assets/a162f272-9fc9-479d-b0b9-e046f6bc796b)

- Note: If you are using an IDE seperate from VS Code please follow the instructions for downloading Python provided in the literature for your IDE.

  ## Configuration

- Create a New Folder by going to Open > New Folder > Create > Open
  ![Screenshot 2024-11-11 at 6 22 06 PM](https://github.com/user-attachments/assets/fd98fd6d-8943-4fba-8cb6-9b14ce3e8b41)
![Screenshot 2024-11-11 at 6 25 53 PM](https://github.com/user-attachments/assets/72af1520-7a94-4fde-9dea-db800776e5cc)
![Screenshot 2024-11-11 at 6 27 34 PM](https://github.com/user-attachments/assets/fcb8ee39-cf0f-4afd-bff4-8d0d7581ef6a)
![Screenshot 2024-11-11 at 6 28 22 PM](https://github.com/user-attachments/assets/c0287e10-2275-4cb6-b87e-ed7e3aa75062)

  - Create a YAML configuration file listing the endpoints you want to monitor. I do this by creating a new file, naming it, and ending it with ".yaml". I gave my .yaml file the name "test.yaml"
   ![Screenshot 2024-11-11 at 7 06 10 PM](https://github.com/user-attachments/assets/8e3024ce-3017-49d9-84ef-32bea89a94cc)
![Screenshot 2024-11-11 at 7 02 44 PM](https://github.com/user-attachments/assets/113ed7f3-e72a-469d-bc6c-42d84892244f)

