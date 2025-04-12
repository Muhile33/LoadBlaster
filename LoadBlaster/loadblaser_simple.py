import argparse
import threading
import time
import requests
from tqdm import tqdm
from fake_useragent import UserAgent

ua = UserAgent()

# Stats tracking
stats = {
    "success": 0,
    "fail": 0,
    "total_time": 0,
}

# Request function
def make_request(session, url, method, headers, data, timeout, progress):
    try:
        start = time.time()
        headers['User-Agent'] = ua.random  # Randomize user-agent for each request
        if method == 'GET':
            r = session.get(url, headers=headers, timeout=timeout)
        else:
            r = session.post(url, data=data, headers=headers, timeout=timeout)
        elapsed = time.time() - start

        stats["success"] += 1
        stats["total_time"] += elapsed

        progress.update(1)

    except requests.exceptions.RequestException as e:
        stats["fail"] += 1
        print(f"Request failed: {e}")

# Worker function for multithreading
def worker(url, method, headers, data, timeout, end_time, progress):
    session = requests.Session()
    while time.time() < end_time:
        make_request(session, url, method, headers, data, timeout, progress)
        time.sleep(0.1)

# Main CLI function
def main():
    parser = argparse.ArgumentParser(description="LoadBlaster - Basic HTTP request sender")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("-m", "--method", default="GET", choices=["GET", "POST"], help="HTTP method")
    parser.add_argument("-d", "--data", help="POST data (for POST requests)")
    parser.add_argument("-H", "--headers", nargs='*', default=[], help="Custom headers")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads")
    parser.add_argument("--duration", type=int, default=30, help="Duration in seconds")
    parser.add_argument("--timeout", type=int, default=5, help="Request timeout in seconds")

    args = parser.parse_args()
    headers = {h.split(':')[0]: h.split(':')[1] for h in args.headers}
    end_time = time.time() + args.duration

    total_requests = int((args.duration / 0.1) * args.threads)  # Request rate 10Hz
    progress = tqdm(total=total_requests, desc="Sending", unit="req")

    threads = []
    for _ in range(args.threads):
        thread = threading.Thread(
            target=worker,
            args=(args.url, args.method.upper(), headers, args.data, args.timeout, end_time, progress)
        )
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    progress.close()

    avg_time = stats["total_time"] / stats["success"] if stats["success"] > 0 else 0
    print(f"\nAttack Complete")
    print(f"  Successful Requests: {stats['success']}")
    print(f"  Failed Requests: {stats['fail']}")
    print(f"  Avg Response Time: {avg_time:.2f}s")

if __name__ == "__main__":
    main()

