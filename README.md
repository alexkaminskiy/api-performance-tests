# Performance Testing Framework (Locust)

### Project Structure
```bash
api-performance-tests/
│
├── locustfile.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore 
│
├── config/
│   ├── settings.py
│
├── clients/
│   ├── base_client.py
│   ├── auth_client.py
│   ├── product_client.py
│   ├── component_client.py
│
├── tasks/
│   ├── auth_tasks.py
│   ├── product_tasks.py
│   ├── component_tasks.py
│   ├── mixed_load.py
│
├── utils/
│   ├── logger.py
└── openapi/
    └── openapi.json
```

## Virtual Environment Setup

It is recommended to use a virtual environment to manage dependencies.

### Windows
1. Create a virtual environment:
   ```bash
   py -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
### MacOS/Linux
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Run Locust tests Locally (Web UI Mode):

### Start Locust:
```bash
locust -f locustfile.py
```
### Open the dashboard:
```bash
http://localhost:8089
```

Configure:

Number of users
Spawn rate
Host (should default to http://eaapi.somee.com/)

### Running Locust in Headless Mode:
```bash
locust -f locustfile.py \
  --headless \
  -u 50 \
  -r 10 \
  --run-time 2m \
  --host http://eaapi.somee.com/ \
  --html report.html
```
This will generate a Locust HTML report.