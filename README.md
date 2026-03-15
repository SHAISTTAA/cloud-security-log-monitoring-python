# Cloud Security Log Monitoring

This project demonstrates a simple security monitoring tool that detects suspicious login behavior from server logs.

The script analyzes login attempts and identifies IP addresses that perform multiple failed login attempts.

Technologies

Python
Pandas

Security Concept

Brute Force Detection

Workflow

1 Load server log dataset
2 Filter failed login attempts
3 Group login attempts by IP
4 Detect suspicious behavior

Run

pip install pandas

python log_analyzer.py
