from app import muvan

if __name__ == "__main__":
    muvan_app = muvan.create_app()
    muvan_app.run(debug=True)
    