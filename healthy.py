import yaml
import requests
import time
import sys
import logging
import concurrent.futures
from collections import defaultdict
from argparse import ArgumentParser

# Set up structured logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_endpoints(file_path):
    """Load and parse endpoints from a YAML configuration file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_endpoint_health(endpoint):
    """Send a request to an endpoint and return True if UP, else False."""
    url = endpoint['url']
    method = endpoint.get('method', 'GET').upper()
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    try:
        response = requests.request(method, url, headers=headers, data=body, timeout=0.5)
        # UP if status code is 2xx and response time is under 500 ms
        is_up = response.status_code in range(200, 300) and response.elapsed.total_seconds() < 0.5
        logging.info(f"Endpoint {endpoint['name']} {'UP' if is_up else 'DOWN'} with status {response.status_code}")
        return is_up
    except requests.RequestException as e:
        logging.error(f"Request to {url} failed: {e}")
        return False

def update_availability_stats(domain_stats, domain, is_up):
    """Update the availability statistics for a specific domain."""
    domain_stats[domain]['total'] += 1
    if is_up:
        domain_stats[domain]['up'] += 1

def log_availability(domain_stats):
    """Log the availability percentage for each domain."""
    for domain, stats in domain_stats.items():
        availability = round(100 * (stats['up'] / stats['total']))
        logging.info(f"{domain} has {availability}% availability")

def monitor_endpoints(file_path, interval):
    """Main function to load endpoints and continuously monitor their health."""
    endpoints = load_endpoints(file_path)
    domain_stats = defaultdict(lambda: {'up': 0, 'total': 0})

    while True:
        try:
            # Concurrently check all endpoints
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {executor.submit(check_endpoint_health, endpoint): endpoint for endpoint in endpoints}
                for future in concurrent.futures.as_completed(futures):
                    endpoint = futures[future]
                    url = endpoint['url']
                    domain = url.split("//")[1].split("/")[0]
                    is_up = future.result()
                    update_availability_stats(domain_stats, domain, is_up)

            log_availability(domain_stats)
            time.sleep(interval)

        except KeyboardInterrupt:
            logging.info("\nMonitoring stopped by user.")
            break

if __name__ == "__main__":
    parser = ArgumentParser(description="HTTP endpoint health checker.")
    parser.add_argument("file_path", help="Path to the YAML configuration file.")
    parser.add_argument("--interval", type=int, default=15, help="Time interval (seconds) between health checks.")
    args = parser.parse_args()

    monitor_endpoints(args.file_path, args.interval)
