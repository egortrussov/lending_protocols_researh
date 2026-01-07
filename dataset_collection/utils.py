from queries import (
    get_vaults_query,
)
import requests

MORPHO_GRAPHQL_API = "https://api.morpho.org/graphql"

def send_morpho_request(query):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'https://sandbox.embed.apollographql.com',
        'Access-Control-Allow-Credentials': 'true'
    }
    
    response = requests.post(
        MORPHO_GRAPHQL_API,
        json={'query': query},
        headers=headers
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")

