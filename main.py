from website import create_app
#
app = create_app()
# Run the Flask application
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)