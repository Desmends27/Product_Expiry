# Product_Expiry_System
This is a Django-based program that helps you keep track of product expiry dates.

## Features
The program allows you to:

- Add products
- Edit product information
- Delete products
- Search for products based on product name and manufacturer name
- Receive email notifications when a product is about to expire

## Installation
1. Clone the repository in an empty directory.
2. On Windows run ```setup\setup.bat```, on Unix ```setup/setup.sh```.
3. Fill in the required data for the .env file created.
4. Run the server using ```python manage.py runserver```.
5. Visit http://localhost:8000/ in your browser.

# Usage

## Adding a Product
1. Click on the "Add a Product" button on the home page.
2. Enter the product information.
3. Click the "Save" button.

## Editing a Product
1. Click on the product name on the home page.
2. Click on the "Edit" button.
3. Edit the product information.
Click the "Save" button.

## Deleting a Product
1. Click on the product name on the home page.
2. Click on the "Delete" button.
3. Confirm the deletion.

## Searching for Products
1. Enter the search query in the search box on the home page.
2. Click the "Search" button.

## Receiving Email Notifications (in progress)
1. Set up email settings in the Django settings file.
2. The program will automatically send email notifications to the email address specified in the settings.py file when a product is about to expire.