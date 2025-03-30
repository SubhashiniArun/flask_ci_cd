from flask import jsonify
from werkzeug.exceptions import HTTPException

def init_error_handling(app):

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        return jsonify({
            "error": e.name,
            "message": e.description
        }), e.code
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500
