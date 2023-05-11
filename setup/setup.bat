@echo off

IF EXIST venv (
    echo Virtual environment already exists
) ELSE (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Installing requirements...
pip install -r requirements.txt
echo Done installing requirements

echo "Creating .env file..."
echo EMAIL_HOST_PASSWORD=Enter_password_here> .env
echo EMAIL_HOST_USER=Enter_email_account_here>> .env
echo Done with setup...
echo Please complete the .env file with required data...
echo example EMAIL_HOST_USER=john@gmail.com
