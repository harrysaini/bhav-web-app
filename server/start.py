from scripts.saveCSVToDb import setup_db
from app import start_server


def main():
    start_server()
    setup_db()

if __name__ == "__main__":
    main()