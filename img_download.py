import json
import requests
import shutil
import os.path

def download(image_url):
	name = 'C:\\Users\\roofu\\Desktop\\fortniteskins\\main\\static\\image\\' + image_url.split("/image/")[1].replace("/", "_")
	if os.path.exists(name) == False:
		local_file = open(name, 'wb')
		resp = requests.get(image_url, stream=True)
		# Open a local file with wb ( write binary ) permission.
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		resp.raw.decode_content = True
		# Copy the response stream raw data to local image file.
		shutil.copyfileobj(resp.raw, local_file)
		print(image_url)
		local_file.close()

response = requests.get("https://fortnite-api.com/cosmetics/br?language=ru", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
json_data = json.loads(response.text)
for i in json_data["data"]:
    try:
        download(i["images"]["smallIcon"]["url"])
        download(i["images"]["icon"]["url"])
        download(i["images"]["featured"]["url"])
    except Exception as e:
        print(e)
