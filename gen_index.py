import json
import os

STICKERS_DIR = "./stickers"
OUTPUT_FILE = "stickers.json"

IMAGE_EXTS = (".webp", ".gif", ".png", ".jpg", ".jpeg")


def get_images(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(IMAGE_EXTS)]
    files.sort()

    return files


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

        data.append(
            {
                "name": folder,
                "folder": folder,
                "preview": f"stickers/{folder}/{images[0]}",
                "images": [f"stickers/{folder}/{img}" for img in images],
            }
        )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Generated {OUTPUT_FILE} with {len(data)} folders")


if __name__ == "__main__":
    main()
