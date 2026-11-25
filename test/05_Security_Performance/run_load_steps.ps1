# Windows version of run_load_steps.sh
# Usage (PowerShell):  .\run_load_steps.ps1
New-Item -ItemType Directory -Force results | Out-Null
foreach ($u in 1, 5, 10, 25, 50) {
  Write-Host "=== $u users ==="
  locust -f locustfile.py --headless -u $u -r 5 -t 2m `
         --csv "results/step_${u}u" --html "results/step_${u}u.html" --only-summary
  Start-Sleep -Seconds 15
}
python summarise_results.py
