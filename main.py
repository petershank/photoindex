import sys

from photoindex import PhotoIndex


def usage():
    print("Usage:")
    print("    python3 main.py info")


def main():
    if len(sys.argv) != 2:
        usage()
        return

    command = sys.argv[1]

    index = PhotoIndex()

    if command == "info":
        print(f"Found {index.photo_count()} photos.")
    else:
        usage()


if __name__ == "__main__":
    main()
    