from pyicloud import PyiCloudService
from dotenv import load_dotenv
import os
from os.path import dirname, join

#  load .env file
load_dotenv(os.getcwd() + "/.env")

# set login information
apple_id = os.getenv("icloud.user")
password = os.getenv("icloud.password")

if not apple_id or not password:
    print("Apple ID or password environment variables are not set.")
    exit(1)

# require authentication
api = PyiCloudService(apple_id, password)

# confirm 2 factor authentication
if api.requires_2fa:
    code = input("Enter the code you received: ")
    result = api.validate_2fa_code(code)
    print("2FA result: ", result)
    if not result:
        print("Failed to authenticate")
        exit(1)

# set download target dir
download_dir = os.getenv("icloud.backup.dir")
os.makedirs(download_dir, exist_ok=True)

# fetch all photos
photos = api.photos.all

# run download
for photo in photos:
    photo_name = photo.filename
    photo_path = os.path.join(download_dir, photo_name)
    with open(photo_path, 'wb') as f:
        f.write(photo.download().raw.read())
    print(f"Downloaded {photo_name}")

print("All photos downloaded.")