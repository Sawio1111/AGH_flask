"""
Module containing routes for the calculator application.
"""

from flask import Blueprint, request
from templates.summary import generate_summary_html

calculate_bp = Blueprint('calculate', __name__)


@calculate_bp.route('/calculate')
def calculate():
    """
    Route handler for performing basic arithmetic operations.

    The operation and operands should be provided as query parameters:
    - `op`: the operation (e.g., 'add', 'subtract', 'multiply', 'divide')
    - `arg1`: the first operand (integer)
    - `arg2`: the second operand (integer)

    Returns:
        HTML template displaying the result or an error message.
    """
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op is None or arg1 is None or arg2 is None:
        return "Missing Params! (op, arg1, arg2)", 400

    result = None
    if op == 'sum':
        result = arg1 + arg2
    elif op == 'sub':
        result = arg1 - arg2
    elif op == 'mul':
        result = arg1 * arg2
    elif op == 'div':
        if arg2 == 0:
            return "Error: Divided by zero", 400
        result = arg1 / arg2
    else:
        return "Unsupported operation! (add, subtract, multiply, divide)", 400

    return generate_summary_html(result)
