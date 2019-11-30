from scripts.saveCSVToDb import setup_db
from app import start_server


def main():
    setup_db()
    start_server()

if __name__ == "__main__":
    main()