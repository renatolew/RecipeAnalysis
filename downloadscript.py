import requests

#specifying the url of the download in order to use the requests module.
download_url = "https://storage.googleapis.com/recipe-box/recipes_raw.zip"

#using the get method to get the exact download url from the API.
req = requests.get(download_url)

#using the find to split the url and get only the filename after the last '/'
filename = req.url[download_url.rfind('/')+1:]

#opening the file in 'wb' (write binary) to make sure the content is not modified in the process of downloading.
with open(filename, "wb") as f:
    #iterating the response content to download the file in chunks.
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)