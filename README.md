# Log Analyzer

A small Python tool that analyzes authentication logs to detect
brute-force attacks.

## What it does
- Counts connections and failed logins per IP address
- Flags IPs with many failed attempts (configurable threshold)
- Detects successful logins that follow repeated failures,
  a sign of a compromised account

## Usage
    python3 log_analyzer.py

## Log format
    DATE TIME IP STATUS USER
    2026-10-07 14:01:45 203.0.113.50 LOGIN_FAIL root

## Example output
(colle ici la sortie de ton script)

## Limitations
- Threshold is not time-based (5 failures in a year ≠ 5 in a minute)
- Detection is per IP only, not per account
- Reads the whole file several times (fine for small logs)

## What I learned
Python basics, dictionaries and sets, file handling, and how
brute-force attacks appear in logs.