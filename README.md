{\rtf1\ansi\ansicpg1252\cocoartf2907
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Log Analyzer\
\
A small Python tool that analyzes authentication logs to detect\
brute-force attacks.\
\
## What it does\
- Counts connections and failed logins per IP address\
- Flags IPs with many failed attempts (configurable threshold)\
- Detects successful logins that follow repeated failures,\
  a sign of a compromised account\
\
## Usage\
    python3 log_analyzer.py\
\
## Log format\
    DATE TIME IP STATUS USER\
    2026-10-07 14:01:45 203.0.113.50 LOGIN_FAIL root\
\
## Example output\
(colle ici la sortie de ton script)\
\
## Limitations\
- Threshold is not time-based (5 failures in a year \uc0\u8800  5 in a minute)\
- Detection is per IP only, not per account\
- Reads the whole file several times (fine for small logs)\
\
## What I learned\
Python basics, dictionaries and sets, file handling, and how\
brute-force attacks appear in logs.}