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

- Download python. If you are having trouble, use the information under the "Install a Python Interpreter" section of [this link](https://code.visualstudio.com/docs/python/python-tutorial)
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

# How It Works

1. Importing Libraries:

   ![Screenshot 2024-11-11 at 8 32 04 PM](https://github.com/user-attachments/assets/285613f7-0da7-4b5b-a987-70c84759d074)

import yaml: This library helps us read and write YAML files. YAML is a human-readable data format that's often used for configuration files.

import requests: This library allows us to send HTTP requests (like GET and POST) to websites. It's very useful for interacting with web APIs.

import time: This module provides various time-related functions, such as sleeping for a certain number of seconds.

import sys: This module provides access to some variables used or maintained by the Python interpreter, like command-line arguments.

import logging: This module allows us to log messages that can help us understand what the program is doing, especially useful for debugging and monitoring.

import concurrent.futures: This module helps us run multiple tasks at the same time (concurrently). Here, we'll use it to check multiple websites simultaneously.

from collections import defaultdict: defaultdict is a type of dictionary that provides a default value for non-existent keys, making it easier to handle data without checking if keys exist.

from argparse import ArgumentParser: This module helps us handle command-line arguments, allowing users to provide input when running the program.

2. Setting Up Logging:

![Screenshot 2024-11-11 at 8 34 58 PM](https://github.com/user-attachments/assets/3c168c7c-48cd-4a8a-b371-1a13530437e7)

logging.basicConfig(...): This line configures the logging system.

level=logging.INFO: Sets the logging level to INFO, meaning it will capture INFO, WARNING, ERROR, and CRITICAL messages. It won’t capture DEBUG messages.

format="%(asctime)s - %(levelname)s - %(message)s": Defines the format of the log messages. Each message will include the time it was logged (%(asctime)s), the level of the message (%(levelname)s), and the actual message (%(message)s).

3. Function to Load Endpoints from YAML
   
![Screenshot 2024-11-11 at 8 37 39 PM](https://github.com/user-attachments/assets/298071fd-ff28-47a0-a0e0-f2db74d52561)

def load_endpoints(file_path):: Defines a function named load_endpoints that takes file_path as an argument. This function will load and parse the YAML file containing the list of websites to check.

with open(file_path, 'r') as file:: Opens the file at file_path in read mode ('r'). The with statement ensures that the file is properly closed after we're done with it.

return yaml.safe_load(file): Reads the content of the file and parses it as YAML using yaml.safe_load(). This converts the YAML content into a Python data structure (like a list of dictionaries) and returns it.

4. Function to Check Endpoint Health

![Screenshot 2024-11-11 at 8 38 52 PM](https://github.com/user-attachments/assets/2e7ea71f-e8c7-48bc-8905-f677ba2cd2f9)

def check_endpoint_health(endpoint):: Defines a function that takes an endpoint (a dictionary with details about the website) and checks its health.

url = endpoint['url']: Extracts the URL of the website from the endpoint dictionary.

method = endpoint.get('method', 'GET').upper():

endpoint.get('method', 'GET'): Tries to get the HTTP method (like GET or POST) from the endpoint dictionary. If it’s not provided, defaults to 'GET'.
.upper(): Converts the method to uppercase to ensure consistency (e.g., 'get' becomes 'GET').
headers = endpoint.get('headers', {}): Retrieves the headers from the endpoint dictionary. If no headers are provided, it defaults to an empty dictionary {}.

body = endpoint.get('body', None): Retrieves the body of the request from the endpoint dictionary. If no body is provided, it defaults to None.

- Sending the Request

try:: Starts a try-except block to handle potential errors when sending the request.

response = requests.request(method, url, headers=headers, data=body, timeout=0.5):

requests.request(...): Sends an HTTP request using the specified method (GET, POST, etc.), URL, headers, and body.
timeout=0.5: Sets a timeout of 0.5 seconds (500 milliseconds). If the request takes longer than this, it will raise a timeout error.

- Determining UP or DOWN

is_up = response.status_code in range(200, 300) and response.elapsed.total_seconds() < 0.5:

response.status_code in range(200, 300): Checks if the HTTP response status code is in the 200s (e.g., 200 OK, 201 Created). These codes generally indicate success.
response.elapsed.total_seconds() < 0.5: Checks if the response time is less than 0.5 seconds (500 milliseconds).
is_up: If both conditions are true, the endpoint is considered "UP". Otherwise, it's "DOWN".
logging.info(...): Logs an INFO-level message indicating whether the endpoint is UP or DOWN along with the status code.

return is_up: Returns True if the endpoint is UP, else False.

- Handling Errors

except requests.RequestException as e:: Catches any exceptions raised by the requests library (like timeouts, connection errors, etc.).

logging.error(...): Logs an ERROR-level message indicating that the request to the URL failed, along with the error message.

return False: Returns False since the endpoint couldn’t be reached or responded correctly, marking it as DOWN.

5. Function to Update Availability Statistics

![Screenshot 2024-11-11 at 8 41 42 PM](https://github.com/user-attachments/assets/9c9b3710-9a8d-4416-b486-75cf1cf3a14f)

def update_availability_stats(domain_stats, domain, is_up):: Defines a function that updates the statistics for a given domain.

domain_stats[domain]['total'] += 1: Increments the total number of checks for the domain by 1.

if is_up:: Checks if the current check determined the domain is UP.

domain_stats[domain]['up'] += 1: If UP, increments the count of successful (UP) checks for the domain by 1.
What is domain_stats?

domain_stats: A dictionary that keeps track of how many times each domain was checked and how many times it was UP.

Structure: { 'example.com': {'up': 5, 'total': 10}, ... }

6. Function to Log Availability

![Screenshot 2024-11-11 at 8 43 59 PM](https://github.com/user-attachments/assets/a6714c19-02bf-4856-a277-070855f7ec06)

def log_availability(domain_stats):: Defines a function that logs the availability percentage for each domain.

for domain, stats in domain_stats.items():: Iterates over each domain and its statistics in the domain_stats dictionary.

availability = round(100 * (stats['up'] / stats['total'])):

stats['up'] / stats['total']: Calculates the ratio of successful (UP) checks to total checks.
100 * ...: Converts the ratio to a percentage.
round(...): Rounds the percentage to the nearest whole number for readability.

logging.info(...): Logs an INFO-level message showing the domain and its availability percentage.

7. Main Monitoring Function

![Screenshot 2024-11-11 at 8 45 08 PM](https://github.com/user-attachments/assets/18ae602d-413b-45a1-a141-2786c81f9015)

def monitor_endpoints(file_path, interval):: Defines the main function that orchestrates loading the endpoints and monitoring their health.

endpoints = load_endpoints(file_path): Calls the load_endpoints function to read the YAML file and get the list of endpoints to monitor.

domain_stats = defaultdict(lambda: {'up': 0, 'total': 0}):

Initializes a defaultdict where each key (domain) maps to another dictionary with keys 'up' and 'total', both starting at 0.
This structure helps in tracking how many times each domain was checked and how many times it was up.

-Infinite Monitoring Loop

while True:: Starts an infinite loop that will continuously monitor the endpoints until the user stops the program.

try:: Starts a try-except block to handle user interruptions gracefully.

- Concurrent Health Checks

with concurrent.futures.ThreadPoolExecutor() as executor::

ThreadPoolExecutor: Creates a pool of threads to run multiple tasks (checking endpoints) concurrently.
Using threads allows multiple HTTP requests to be sent at the same time, speeding up the process.
futures = {executor.submit(check_endpoint_health, endpoint): endpoint for endpoint in endpoints}:

executor.submit(...): Schedules the check_endpoint_health function to run for each endpoint.
futures: A dictionary mapping each future (a placeholder for the result of the function) to its corresponding endpoint.
for future in concurrent.futures.as_completed(futures)::

as_completed(futures): Returns an iterator that yields futures as they complete, regardless of the order they were started.

- Inside the Loop:

endpoint = futures[future]: Retrieves the endpoint corresponding to the completed future.

url = endpoint['url']: Gets the URL of the endpoint.

domain = url.split("//")[1].split("/")[0]:

url.split("//")[1]: Splits the URL at '//' and takes the second part, which contains the domain and path (e.g., 'example.com/path').
.split("/")[0]: Splits this part at '/' and takes the first part, which is the domain (e.g., 'example.com').
is_up = future.result(): Retrieves the result of the check_endpoint_health function, which is True if the endpoint is UP and False otherwise.

update_availability_stats(domain_stats, domain, is_up): Updates the statistics for the domain based on whether it was UP or DOWN.

- Logging and Sleeping

log_availability(domain_stats): Calls the function to log the current availability percentages for all domains.

time.sleep(interval): Pauses the program for the specified interval (default 15 seconds) before the next round of health checks.

- Handling User Interruptions

except KeyboardInterrupt:: Catches the KeyboardInterrupt exception, which occurs when the user presses CTRL+C to stop the program.

logging.info("\nMonitoring stopped by user."): Logs an INFO-level message indicating that the monitoring was stopped by the user.

break: Exits the infinite loop, effectively stopping the program.

- Why Use This Structure?

Concurrency: Using ThreadPoolExecutor allows multiple endpoints to be checked at the same time, making the monitoring process faster and more efficient, especially when dealing with many endpoints.

Graceful Shutdown: By catching KeyboardInterrupt, the program can exit cleanly without showing an error message, providing a better user experience.

8. Entry Point of the Program

![Screenshot 2024-11-11 at 8 48 21 PM](https://github.com/user-attachments/assets/aed3bf00-fae7-442f-82e3-979c20bbd418)

if __name__ == "__main__":: This line checks if the script is being run directly (not imported as a module). If it is, the code inside this block will execute.

parser = ArgumentParser(description="HTTP endpoint health checker."):

Creates an ArgumentParser object that will handle command-line arguments.
description: A brief description of what the program does.
parser.add_argument("file_path", help="Path to the YAML configuration file."):

"file_path": Adds a required positional argument named file_path. The user must provide this argument when running the program.
help: A short description of what this argument is for, which is displayed if the user asks for help.
parser.add_argument("--interval", type=int, default=15, help="Time interval (seconds) between health checks."):

"--interval": Adds an optional argument named --interval. The user can specify it using --interval 30 to set the interval to 30 seconds.
type=int: Specifies that the value for this argument should be an integer.
default=15: If the user doesn’t provide this argument, it defaults to 15 seconds.
help: Description shown in help messages.
args = parser.parse_args():

Parses the command-line arguments provided by the user and stores them in the args variable.
args.file_path: Contains the value provided for file_path.
args.interval: Contains the value provided for --interval, or the default value (15) if not provided.
monitor_endpoints(args.file_path, args.interval):

Calls the monitor_endpoints function with the provided file_path and interval.
This starts the monitoring process.
