#!/bin/bash
pip install --no-cache-dir -r requirements.txt
PYTHONPATH=. uvicorn achmod +x start.sh
pp.main:app --host "0.0.0.0" --port="${PORT:-8000}"