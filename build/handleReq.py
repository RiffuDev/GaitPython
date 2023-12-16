import os
import httpx

def getReq(api_url):

    try:
        response = httpx.post(api_url)

        if response.status_code == 200:
            # Access response data (assuming it's JSON)
            data = response.json()
            print(f"Successfully retrieved data: {data}")
            return data
        else:
            print(f"Error getting data: {response.status_code}")
            return response.status_code

    except httpx.HTTPError as e:
        print(f"HTTP Error: {e}")
        return "HTTP Error: {e}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Unexpected error: {e}"

def startAnalysis(anlTime, ip):
    # 192.168.11.43/test?Trigger=ON&Time=100&trigId=5359&patientId=322032

    url = f"http://{ip}/test?Trigger=ON&Time={anlTime}&trigId=5359&patientId=322032"
    print(url)
    getReq(url)

def stopAnalysis(anlTime, ip):
    # 192.168.11.43/test?Trigger=OFF&Time=100&trigId=5359&patientId=322032

    url = f"http://{ip}/test?Trigger=OFF&Time={anlTime}&trigId=5359&patientId=322032"
    print(url)
    getReq(url)

def download_file(url, path):
    """
    Downloads a file from the given URL and saves it to the specified path.

    Args:
        url: The URL of the file to download.
        path: The path (including filename) to save the downloaded file.

    Returns:
        None
    """

    # Create the directory containing the path if it doesn't exist
    data_dir = os.path.dirname(path)
    try:
        os.makedirs(data_dir, exist_ok=True)
    except FileExistsError:
        pass

    # Send the GET request and download the file
    with httpx.Client() as client:
        response = client.get(url)

        # Get the filename from the response headers
        # filename = response.headers.get("Content-Disposition", "").split("=")[1].strip('"') or os.path.basename(url)

        # Save the downloaded content to the file
        with open(os.path.join(data_dir, "testJSON"), "wb") as file:
            file.write(response.content)

    # print(f"Downloaded file: {filename} to {os.path.join(data_dir, filename)}")

# Example usage
# download_file("https://filesamples.com/samples/code/json/sample4.json", "fData/my_file")

# startAnalysis(60, "192.168.4.1")