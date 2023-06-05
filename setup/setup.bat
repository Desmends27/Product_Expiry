@echo off

python -m venv venv

echo Activating virtual environment...
venv\Scripts\activate.bat
echo Installing requirements...
pip install -r requirements.txt
echo Done installing requirements

echo Making migrations
python manage.py makemigrations
python manage.py migrate

echo "Creating .env file..."
echo EMAIL_HOST_PASSWORD=Enter_password_here > .env
echo EMAIL_HOST_USER=Enter_email_account_here >> .env
echo Done with setup...
echo Please complete the .env file with required data...
echo example EMAIL_HOST_USER=john@gmail.com
