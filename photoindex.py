import osxphotos


class PhotoIndex:
    def __init__(self):
        self.db = osxphotos.PhotosDB()

    def photo_count(self):
        return len(self.db.photos())
    