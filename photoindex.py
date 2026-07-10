import osxphotos

from photo import Photo


class PhotoIndex:
    def __init__(self):
        self.db = osxphotos.PhotosDB()

    def photo_count(self):
        return len(self.db.photos())

    def recent_photos(self, count=5):
        photos = []

        all_photos = sorted(
            self.db.photos(),
            key=lambda p: p.date_added,
            reverse=True,
        )

        for p in all_photos[:count]:
            photos.append(
                Photo(
                    uuid=p.uuid,
                    filename=p.filename,
                    date=p.date,
                    description=p.description,
                    ai_caption=p.ai_caption,
                    detected_text=p.detected_text(),
                )
            )

        return photos