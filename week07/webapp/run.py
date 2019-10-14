from myapp import initialize_app

app = initialize_app()

app.run(debug=app.config['DEBUG'], host='0.0.0.0')