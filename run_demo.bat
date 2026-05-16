@echo off
setlocal
set PYTHONPATH=%~dp0src;%PYTHONPATH%

python -m assetpack scan examples\shot001 --out work\shot001.manifest.json
if errorlevel 1 exit /b %errorlevel%

python -m assetpack validate work\shot001.manifest.json
if errorlevel 1 exit /b %errorlevel%

python -m assetpack plan-export work\shot001.manifest.json --out-root work\export --dry-run --out work\shot001.export_plan.json
if errorlevel 1 exit /b %errorlevel%

python scripts\validate.py --profile fast
exit /b %errorlevel%
