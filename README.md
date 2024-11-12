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
  
- Open the terminal: Go to the top menu, click View > Terminal. This will open a terminal at the bottom of the VS Code window.
![Screenshot 2024-11-11 at 7 38 17 PM](https://github.com/user-attachments/assets/c915b35b-bd00-421b-a1d8-ec4225c9aa16)

- Clone the repository: In the terminal, enter the following command to clone the repository: git clone https://github.com/RightChoiceJayden/HTTPHealthCheck
  ![Screenshot 2024-11-11 at 7 41 20 PM](https://github.com/user-attachments/assets/e9a7c23d-770b-4110-bff0-c1541ffbe2ca)
  - Open the folder:
 ![Screenshot 2024-11-11 at 7 42 07 PM](https://github.com/user-attachments/assets/b8c9f2e8-bb2f-455a-a80f-80f0b7c26b04)

- Navigate to the Project Directory using the following command: cd HTTPHealthCheck/
![Screenshot 2024-11-11 at 8 05 32 PM](https://github.com/user-attachments/assets/031b4208-9740-4454-b6a1-1d11263d540f)

  - Run the program using the following command: python3 healthy.py test.yaml
![Screenshot 2024-11-11 at 8 10 48 PM](https://github.com/user-attachments/assets/51552f00-d3f7-4bb1-a003-6c20a996c8ab)

- Note: If you get any 'ModuleNotFoundError:' messages simply run the command: pip install "module name"
- As you can see here we had an error concerrning the module "requests" so the command pip install requests is ran
  
![Screenshot 2024-11-11 at 8 15 26 PM](https://github.com/user-attachments/assets/e64988ee-8e86-41f1-8d62-adee8b330e37)
![Screenshot 2024-11-11 at 8 20 53 PM](https://github.com/user-attachments/assets/9b4b9115-3570-48d3-afc4-e30913158df8)

