from myapp import initalie_app

app = initalie_app()

app.run(debug=app.config['DEBUG'], host='0.0.0.0')