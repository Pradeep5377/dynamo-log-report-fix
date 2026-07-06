Task

An Apache-style access log is available in the working directory as `access.log`.

Analyze the log and generate a JSON summary report.

Save the report as `report.json`.

The report must contain:

- `total_requests` – total number of requests in the log
- `unique_ips` – number of unique client IP addresses
- `top_path` – the most frequently requested path

Success Criteria

1. Read the input from `access.log`.
2. Calculate the total number of requests.
3. Count the number of unique client IP addresses.
4. Determine the most frequently requested path.
5. Save the results as `report.json` in valid JSON format.