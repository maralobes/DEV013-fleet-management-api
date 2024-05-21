from flask import jsonify, make_response

class Errors:
    @staticmethod
    def handle_400_error(_error):
        """Return a 400 http status code"""
        return make_response(jsonify({'error' : 'Bad request'}, 400))
    @staticmethod
    def handle_404_error(_error):
        """Return a 404 http status code"""
        return make_response(jsonify({'error' : 'Not found'}, 404))
    @staticmethod
    def handle_500_error(_error):
        """Return a 500 http status code"""
        return make_response(jsonify({'error' : 'Internal server error occured'}, 500))