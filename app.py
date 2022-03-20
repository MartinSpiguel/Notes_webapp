from website import create_app

#Create the app
app = create_app()

#Run the server (app)
if __name__ == '__main__':
    app.run(debug=True)