#!/bin/bash
pip install --no-cache-dir -r requirements.txt
chmod +x start.sh
uvicorn app.main:app --host "0.0.0.0" --port="${PORT:-8000}"
