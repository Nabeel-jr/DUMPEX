@echo off
echo SafeBite - Setting up Python environment...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.9-3.11 from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Check if venv module is available
python -c "import venv" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Unable to create virtual environment.
    pause
    exit /b 1
)

:: Create virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

:: Activate and install dependencies
echo.
echo Installing Python packages from requirements.txt...
echo.

call venv\Scripts\activate.bat

if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

pip install --upgrade pip
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ERROR: Failed to install required packages.
    echo Check your internet connection or requirements.txt.
    pause
    exit /b 1
)

echo.
echo SETUP COMPLETE!
echo.
echo To run the project, use:
echo     venv\Scripts\activate
echo     python manage.py runserver
echo.
pause
