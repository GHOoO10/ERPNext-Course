import requests

def download_video(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print("Video downloaded successfully.")
    else:
        print("An error occurred while downloading the video.")

# Use the URL of the video you want to download
video_url = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_5mb.mp4"

# Specify the file path where the video will be saved
save_path = "GhamdanVid.mp4"

# Execute the function to download the video
print("Download Video from website using URL for the video...")
download_video(video_url, save_path)

