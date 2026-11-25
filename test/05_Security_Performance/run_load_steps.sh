#!/usr/bin/env bash
# Runs the load test at increasing user counts. Each step: 2 min, results in results/
# Usage:  bash run_load_steps.sh
set -e
mkdir -p results
for USERS in 1 5 10 25 50; do
  echo "=== $USERS users ==="
  locust -f locustfile.py --headless -u "$USERS" -r 5 -t 2m \
         --csv "results/step_${USERS}u" --html "results/step_${USERS}u.html" --only-summary
  sleep 15   # let the server settle between steps
done
python summarise_results.py
