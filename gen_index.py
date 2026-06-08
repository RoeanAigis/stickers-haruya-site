import json
import os

STICKERS_DIR = "./stickers"
OUTPUT_FILE = "stickers.json"

IMAGE_EXTS = (".webp", ".gif", ".png", ".jpg", ".jpeg")


def get_images(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(IMAGE_EXTS)]
    files.sort()
    return files


def build_path(folder, filename):
    return f"stickers/{folder}/{filename}"


def main():
    data = []

    if not os.path.exists(STICKERS_DIR):
        print(f"Missing folder: {STICKERS_DIR}")
        return

    for folder in sorted(os.listdir(STICKERS_DIR)):
        folder_path = os.path.join(STICKERS_DIR, folder)

        if not os.path.isdir(folder_path):
            continue

        images = get_images(folder_path)
        if not images:
            continue

        normal_images = [
            build_path(folder, img) for img in images if not img.startswith("LM_")
        ]

        lost_media = [
            build_path(folder, img) for img in images if img.startswith("LM_")
        ]

        preview_list = normal_images if normal_images else lost_media

        data.append(
            {
                "name": folder,
                "folder": folder,
                "preview": preview_list[0],
                "images": normal_images,
                "lostmedia": lost_media,
            }
        )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Generated {OUTPUT_FILE} with {len(data)} folders")


if __name__ == "__main__":
    main()
