# 🚀 LoadBlaster (Simple Version)  
### 🔥 Lightweight HTTP Request Flooder for Ethical Stress Testing

**LoadBlaster** is a no-nonsense, fast, and beginner-friendly CLI tool for stress testing web servers using multithreaded HTTP requests.  
Whether you're testing your own infrastructure, preparing for a CTF, or just learning how stress tests work — **this tool's for you.**

> ⚠️ **Warning:** Use responsibly! This tool is for **educational and authorized testing only**. Unauthorized use against websites you don't own is illegal.

---

## ⚡ Features
- 🧠 Simple & clean CLI interface
- 🧵 Multithreaded request flooder
- 🎭 Random User-Agent spoofing (via `fake_useragent`)
- 📊 Live progress bar with success/fail counters
- 🛠️ Built with pure Python

---

## 🧩 Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```
Or manualy 
```bash
pip install requests tqdm fake_useragent
```
---

## 🔧 Usage
```bash
python loadblaster_simple.py <url> [options]
```

---

## 💡 Examples

```bash
# 10-thread GET spam for 30 seconds
python loadblaster_simple.py http://example.com --threads 10 --duration 30

# 20-thread POST spam with form data
python loadblaster_simple.py http://example.com/login --method POST --data "username=admin&password=123" --threads 20 --duration 45

# With custom headers
python loadblaster_simple.py http://example.com --headers "X-Custom-Header: hello" "User-Agent: LOLBlaster/1.0"
```

## 🔍 Options

| Flag              | Description                                     | Default      |
|-------------------|-------------------------------------------------|--------------|
| `url`             | 🔗 Target URL                                   | *Required*   |
| `--method`, `-m`  | 📨 Request method (`GET` or `POST`)             | `GET`        |
| `--data`, `-d`    | 📝 POST data payload (e.g. `key=value&key2=val`) | `None`       |
| `--headers`, `-H` | 🎭 Custom headers (`Key: Value`)                | `None`       |
| `--threads`, `-t` | 🧵 Number of parallel threads                   | `10`         |
| `--duration`      | ⏱️ Total duration in seconds                    | `30`         |
| `--timeout`       | ⛔ Request timeout per request (in seconds)     | `5`          |

## 🧪 For What Use?
- ✅ CTF practice

- ✅ Bug bounty (with permission)

- ✅ Load testing your own APIs
- ❌ NEVER use on anything without explicit permission!

  ## 💻 Contributing
  Wanna add proxy support, logging, or some cool CLI colors?
  Feel free to fork, hack, and PR away! 🎉

  > Got ideas? Drop an issue or feature request!

  ---

  ## 🧠 Reminder
  > This tool is for ethical testing only.
  > Don't be that guy. You know the one. 👀
