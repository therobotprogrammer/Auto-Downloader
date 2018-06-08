#==========================================# 
# Author: Pranav
# If you find this code useful, 
# please include this section and give 
# credit to original author.  
#==========================================

print(">>>>>>>>>>>> Tip: How to get Kaggle authentication token <<<<<<<<<<<")

print("1. To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com.")
print("2. Then go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account) and select 'Create API Token'.")
print("3. This will trigger the download of kaggle.json, a file containing your API credentials.")

print("4. Go to your Google Drive and place the kaggle.json file where your Google Colab notebooks are saved."

from googleapiclient.discovery import build
import io, os
from googleapiclient.http import MediaIoBaseDownload
from google.colab import auth

auth.authenticate_user()

drive_service = build('drive', 'v3')
results = drive_service.files().list(
        q="name = 'kaggle.json'", fields="files(id)").execute()
kaggle_api_key = results.get('files', [])

filename = "~/.kaggle/kaggle.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)

request = drive_service.files().get_media(fileId=kaggle_api_key[0]['id'])
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download from Google Drive %d%%." % int(status.progress() * 100))
    print("Done setting up Kaggle authentication token")
os.chmod(filename, 600)


