# Django Weather App

A simple Django-based web application that allows users to get weather information for different cities by calling an external API. The app fetches weather data such as temperature, humidity, wind speed, and condition description using the OpenWeatherMap API.

## Features

- Fetch weather data for a specific city by entering its name.
- Displays temperature, humidity, wind speed, and weather condition.
- Handle errors like invalid city names or API issues.
- Provides weather details for multiple cities by default.

## Installation

### Prerequisites

- Python 3.x
- Django
- `requests` library

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/abdurrahman310303/django-weather-app.git
2. Navigate to the project directory: cd django-weather-app
 
3. Create a virtual environment (optional but recommended): python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install the required dependencies: pip install -r requirements.txt

5. Apply database migrations: python manage.py migrate

6. Run the development server: python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000 to view the application.


#Usage
Enter the name of the city in the input field and click "Get Weather".
The app will fetch and display the weather information for the city entered.
You can view weather data for several predefined cities on the homepage.

