import requests
import json
import time

# Define the DBpedia SPARQL endpoint
endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query to fetch actors with additional information
query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT DISTINCT ?actor ?name ?birthdate ?nationality (GROUP_CONCAT(DISTINCT ?movie; SEPARATOR=", ") AS ?movies)
WHERE {
  ?actor a dbo:Actor ;
         foaf:name ?name .
  OPTIONAL { ?actor dbo:birthDate ?birthdate }
  OPTIONAL { ?actor dbo:nationality ?nationality }
  OPTIONAL {
    ?movie dbo:starring ?actor ;
           rdfs:label ?movieLabel .
    FILTER (LANG(?movieLabel) = "en")
  }
  FILTER (LANG(?name) = "en")
}
GROUP BY ?actor ?name ?birthdate ?nationality
offset 0
"""

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

# Define the parameters
params = {
    "query": query,
    "format": "json"
}

MAX_RETRIES = 3

for retry in range(MAX_RETRIES):
    try:
        response = requests.get(endpoint, params=params, headers=headers)
        # Process successful response
        break  # Exit the loop on success
    except requests.exceptions.RequestException as e:
        print(f"Error during request, retrying: {retry+1}/{MAX_RETRIES}")
        time.sleep(2)  # Wait for 2 seconds before retry

if retry == MAX_RETRIES - 1:
    print("Failed to retrieve data after retries.")

# Check if the request was successful
if response.status_code == 200 or response.status_code == 206:
    results = response.json()
    actors_list = []

    for result in results["results"]["bindings"]:
        actor_info = {}
        actor_info["actor"] = result.get("actor", {}).get("value", "N/A")
        actor_info["name"] = result.get("name", {}).get("value", "N/A")
        actor_info["birthdate"] = result.get("birthdate", {}).get("value", "N/A")
        actor_info["nationality"] = result.get("nationality", {}).get("value", "N/A")
        actor_info["movies"] = result.get("movies", {}).get("value", "N/A")
        actors_list.append(actor_info)

    # Write data to JSON file
    with open("actors.json", "w", encoding='utf-8') as json_file:
        json.dump(actors_list, json_file, ensure_ascii=False, indent=4)
else:
    print("Error:", response.status_code)
    print(response.text)
