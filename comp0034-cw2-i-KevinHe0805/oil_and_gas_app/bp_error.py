"""
This module contains the blueprint for the error page of the web app
"""

from flask import render_template, Blueprint

error_bp = Blueprint('errors', __name__, template_folder='templates')


@error_bp.app_errorhandler(404)
def error_404(error):
    """
    Error handler 404
    """
    return render_template('404.html'), 404


@error_bp.app_errorhandler(500)
def error_500(error):
    """
    Error handler 500
    """
    return render_template('500.html'), 500
