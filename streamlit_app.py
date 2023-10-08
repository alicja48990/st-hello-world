import streamlit as st

st.write('Hello world!')

import requests
import pandas as pd

base_url = "https://api.waqi.info"  # Replace this with the actual base URL of the API
city = "warsaw"  # Replace with the desired city
token = "136f8d87c3aa5d2a7a6fe9b84cb80ac79abf0adf"  # Replace with your actual API token

# Construct the full URL
url = f"{base_url}/feed/{city}/?token={token}"

# Make a request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    iss_data = response.json()
    # Print the data
    st.write(iss_data)
else:
    st.write(f"Error {response.status_code}: {response.text}")


data = {
    'status': 'ok',
    # ... [rest of your data] ...
    'debug': {'sync': '2023-10-08T20:03:08+09:00'}
}

if 'data' in data:
    # Convert main details to dataframe
    main_df = pd.DataFrame([{
        'status': data['status'],
        'aqi': data['data']['aqi'],
        'dominentpol': data['data']['dominentpol'],
        'time': data['data']['time']['s']
    }])
    st.write(main_df)

    # Convert 'iaqi' to dataframe
    iaqi_df = pd.DataFrame(data['data']['iaqi'])
    st.write(iaqi_df)
else:
    st.write("The key 'data' is not present in the JSON.")
