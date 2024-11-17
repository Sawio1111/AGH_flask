"""
Module for generating HTML templates for displaying calculator results.
"""


def generate_summary_html(result: [int, str]):
    """
    Generates an HTML template as a string to display the result of a calculation.

    Args:
        result (int, str)

    Returns:
        str: HTML summary page.
    """
    return f"""
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator Result</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
        }}
        .result-container {{
            text-align: center;
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        .result {{
            font-size: 2rem;
            color: #333;
        }}
    </style>
    </head>
    <body>
    <div class="result-container">
        <div class="result">
            {result}
        </div>
    </div>
    </body> 
    """
