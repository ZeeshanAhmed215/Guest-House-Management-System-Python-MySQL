# import urllib.request
# import json

# # Prompt the user for a URL
# url = "http://py4e-data.dr-chuck.net/comments_2223768.json"

# # Open the URL and read the data
# with urllib.request.urlopen(url) as response:
#     data = response.read().decode()

# # Parse the JSON data
# json_data = json.loads(data)

# # Extract comment counts and compute the sum
# total_count = 0
# for comment in json_data['comments']:
#     total_count += comment['count']

# print("Sum of comment counts:", total_count)
# import urllib.request
# import urllib.parse
# import json

# # Prompt for location
# location = input("Enter location: ").strip()
# if len(location) < 1:
#     print("No location entered")
#     quit()

# # API endpoint
# serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# # Build URL
# params = {"q": location}
# url = serviceurl + urllib.parse.urlencode(params)

# print("Retrieving", url)

# # Retrieve data
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()

# print("Retrieved", len(data), "characters")

# # Parse JSON
# js = json.loads(data)

# # Extract plus_code (CORRECT LOCATION)
# try:
#     plus_code = js["features"][0]["properties"]["plus_code"]
#     print("Plus code", plus_code)
# except:
#     print("No plus_code found")
