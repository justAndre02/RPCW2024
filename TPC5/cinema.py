import requests
import json
import time


# Define the DBpedia SPARQL endpoint
endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query to fetch movies with additional information
query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbp: <http://dbpedia.org/property/>
select distinct ?film_title ?actor_name ?director_name ?writer_name ?screen_writer ?music_composers ?length ?film_genres  where {
    ?film_title rdf:type <http://dbpedia.org/ontology/Film> .
    optional {?film_title dbo:starring ?actor.
            ?actor rdfs:label ?actor_name .
            FILTER(LANG(?actor_name) = "en")}
    optional {?film_title dbo:director ?director.
            ?director rdfs:label ?director_name .
            FILTER(LANG(?director_name) = "en")}
    optional {?film_title dbo:writer ?writer.
            ?writer rdfs:label ?writer_name .
            FILTER(LANG(?writer_name) = "en")}
    optional {?film_title dbp:screenplay ?screen_play.
            ?screen_play rdfs:label ?screen_writer .
             FILTER(LANG(?screen_writer) = "en")}
    optional {?film_title dbp:music ?soundtrack.
            ?soundtrack rdfs:label ?music_composers .
            FILTER(LANG(?music_composers) = "en")}
    optional {?film_title dbo:runtime ?length .}
    optional {?film_title dbp:genre ?film_genre.
            ?film_genre rdfs:label ?film_genres .
            FILTER(LANG(?film_genres) = "en")}
    optional {?film_title  dbo:starring ?actor .
            ?actor rdfs:label ?actor_name .
            FILTER(LANG(?actor_name) = "en")}

} group by ?film_title ?actor_name ?director_name ?writer_name ?screen_writer ?music_composers ?length ?film_genres
OFFSET 0
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
    movies_dict = {}

    for result in results["results"]["bindings"]:
        title = result.get("film_title", {}).get("value", "N/A")

        # Check if the movie title already exists in the dictionary
        if title not in movies_dict:
            movie = {}
            movie["title"] = title
            movie["actors"] = []
            movie["directors"] = []
            movie["writers"] = []
            movie["screenwriters"] = []
            movie["soundtracks"] = []
            movie["genres"] = []
            movie["abstract"] = result.get("film_abstract", {}).get("value", "N/A")

            movies_dict[title] = movie

        movie = movies_dict[title]

        # Add actor names if not already present in the movie
        actor_name = result.get("actor_name", {}).get("value", "N/A")
        if actor_name not in [actor_info["name"] for actor_info in movie["actors"]]:
            actor_info = {"name": actor_name}
            movie["actors"].append(actor_info)

        # Add director names
        director_name = result.get("director_name", {}).get("value", "N/A")
        if director_name not in movie["directors"]:
            movie["directors"].append(director_name)

        # Add writer names
        writer_name = result.get("writer_name", {}).get("value", "N/A")
        if writer_name not in movie["writers"]:
            movie["writers"].append(writer_name)

        # Add screenwriter names
        screen_writer = result.get("screen_writer", {}).get("value", "N/A")
        if screen_writer not in movie["screenwriters"]:
            movie["screenwriters"].append(screen_writer)

        # Add soundtrack names
        soundtrack = result.get("music_composers", {}).get("value", "N/A")
        if soundtrack not in movie["soundtracks"]:
            movie["soundtracks"].append(soundtrack)

        # Add genre names
        genre = result.get("film_genres", {}).get("value", "N/A")
        if genre not in movie["genres"]:
            movie["genres"].append(genre)

        # Add movie length and type
        length_seconds = float(result.get("length", {}).get("value", "0"))
        movie["length"] = length_seconds
        if length_seconds <= 3600:
            movie["type"] = "Short Film"
        else:
            movie["type"] = "Feature-Length Film"

    # Convert the dictionary values to a list of movies
    movies = list(movies_dict.values())

    # Write data to JSON file
    with open("cinema.json", "w", encoding='utf-8') as json_file:
        json.dump(movies, json_file, ensure_ascii=False, indent=4)
else:
    print("Error:", response.status_code)
    print(response.text)
