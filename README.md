[![Pylint](https://github.com/Sawio1111/AGH_flask/actions/workflows/pylint.yml/badge.svg)](https://github.com/Sawio1111/AGH_flask/actions/workflows/pylint.yml)

# Project Description: Online Calculator in Flask
This project is a web application built using the Flask framework that functions as a simple online calculator. The application allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division via HTTP requests with query parameters.
## Key Features:
Endpoint /calculate: Handles HTTP requests with three parameters: op (operation type), arg1 (first argument), and arg2 (second argument). Users can perform operations such as:
add (addition)
subtract (subtraction)
multiply (multiplication)
divide (division)
# Project Structure:
app.py: The main application module that initializes the Flask app, registers blueprints, and runs the server.
urls.py: Contains the calculate endpoint logic as a Flask blueprint, making it easy to maintain and extend.
templates/: Includes the HTML templates used for displaying calculation results.
templates/summary.py: A utility module that generates the HTML template as a string to present the calculation results.
