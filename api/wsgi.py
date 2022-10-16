from app import app

try:
    if __name__ == "__main__":
        app.run()
except Exception as e:
    print(e)
