Please follow the below instructions to run this branch in your machine:

1. Login to the GitHub account on which you have been granted access to this repository.

2. Clone this repository -
   ```sh
   git clone https://github.com/tDipto/qoutes_newroz.git
   ```
3. Go to the cloned project directory
   ```sh
   cd qoutes_newroz/quotes_server
   ```
4. Create a Virtual Environment
   ```sh
   python -m venv env
   env\Scripts\activate
   ```
5. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```
6. Set Up the Database
    ```sh
   python manage.py migrate
   ```
7. Create a Superuser
    ```sh
   python manage.py createsuperuser --username admin --email admin@example.com
   ```
8. Run the Development Server
   ```sh
   python manage.py runserver
   ```


# Features
### Scraping from URL
https://github.com/tDipto/qoutes_newroz/blob/master/pictures/scraping.PNG

