import sys

from photoindex import PhotoIndex


def usage():
    print("Usage:")
    print("    python3 main.py info")
    print("    python3 main.py recent")


def main():
    if len(sys.argv) != 2:
        usage()
        return

    index = PhotoIndex()

    match sys.argv[1]:

        case "info":
            print(f"Found {index.photo_count()} photos.")

        case "recent":
            for photo in index.recent_photos():
                print("=" * 60)
                print(photo.date)
                print(photo.filename)

                if photo.description:
                    print()
                    print("Caption:")
                    print(photo.description)

                if photo.ai_caption:
                    print()
                    print("AI:")
                    print(photo.ai_caption)

                if photo.detected_text:
                    print()
                    print("Detected text:")
                    print(photo.detected_text)

        case _:
            usage()


if __name__ == "__main__":
    main()