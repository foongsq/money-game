from routes.app import app

try:
  if __name__ == "__main__":
    app.run(debug=True)
except Exception as e:
  print(e)