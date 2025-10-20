@echo off
REM Script to automatically update and push to GitHub

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run pre-commit checks
pre-commit run --all-files
if %errorlevel% neq 0 (
    echo Pre-commit checks failed. Please fix the issues before committing.
    exit /b 1
)

REM Add all changes
git add .

REM Commit with a default message
git commit -m "Auto update"

REM Push to GitHub (assuming remote 'origin' and branch 'main' or 'master')
git push origin main
if %errorlevel% neq 0 (
    REM Try master if main fails
    git push origin master
)

echo Update completed successfully.
