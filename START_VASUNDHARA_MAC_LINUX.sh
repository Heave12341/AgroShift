#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -d .venv ]]; then python3 -m venv .venv; fi
. .venv/bin/activate
python -c 'import fastapi, uvicorn, httpx' >/dev/null 2>&1 || pip install -r backend/requirements.txt

if [[ ! -x frontend/node_modules/.bin/vite ]]; then
  (cd frontend && npm ci)
fi

( .venv/bin/python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000 ) &
API_PID=$!
trap 'kill "$API_PID" 2>/dev/null || true' EXIT
sleep 2
cd frontend
npm run dev
