import requests
import json


# Define the DBpedia SPARQL endpoint
endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query to fetch movies with additional information
query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbp: <http://dbpedia.org/property/>
select distinct ?film_title ?book_name ?actor_name ?director_name ?writer_name ?screen_writer ?music_composers ?producer_name ?length ?release_date ?film_genres  where {
    ?film_title rdf:type <http://dbpedia.org/ontology/Film> .
    optional {?film_title dbo:basedOn ?book.
            ?book rdfs:label ?book_name .
            FILTER(LANG(?book_name) = "en")}
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
    optional {?film_title dbo:producer ?producer.
            ?producer rdfs:label ?producer_name .
            FILTER(LANG(?producer_name) = "en")}
    optional {?film_title dbo:runtime ?length .}
    optional {?film_title dbo:releaseDate ?release_date .}
    optional {?film_title dbp:genre ?film_genre.
            ?film_genre rdfs:label ?film_genres .
            FILTER(LANG(?film_genres) = "en")}
    optional {?film_title  dbo:starring ?actor .
            ?actor rdfs:label ?actor_name .
            FILTER(LANG(?actor_name) = "en")}

} group by ?film_title ?book_name ?actor_name ?director_name ?writer_name ?screen_writer ?music_composers ?producer_name ?length ?release_date ?film_genres
"""
# Initialize variables for pagination
offset = 0
has_more_results = True
movies_dict = {}


while has_more_results:
    # Modify the query with OFFSET clause
    modified_query = query + f"\nLIMIT 9999\nOFFSET {offset}"

    # Send request with modified query
    params = {"query": modified_query, "format": "json", "timeout": 120000}
    response = requests.get(endpoint, params=params, headers={"Accept": "application/sparql-results+json"})

    # Check for errors
    if response.status_code != 200 and response.status_code != 206:
        print("Error:", response.status_code)
        break
    
    # Process response and build movie dictionary
    results = response.json()
    for result in results["results"]["bindings"]:
        title = result.get("film_title", {}).get("value", "N/A")

        # Check if the movie title already exists in the dictionary
        if title not in movies_dict:
            movie = {}
            movie["title"] = title
            movie["books"] = []
            movie["actors"] = []
            movie["directors"] = []
            movie["writers"] = []
            movie["screenwriters"] = []
            movie["soundtracks"] = []
            movie["producers"] = []
            movie["genres"] = []
            movie["releases"] = []
            movie["abstract"] = result.get("film_abstract", {}).get("value", "N/A")

            movies_dict[title] = movie

        movie = movies_dict[title]

        # Add book names
        book_name = result.get("book_name", {}).get("value", "N/A")
        if book_name not in movie["books"]:
            movie["books"].append(book_name)


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

        # Add producer names
        producer_name = result.get("producer_name", {}).get("value", "N/A")
        if producer_name not in movie["producers"]:
            movie["producers"].append(producer_name)

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

        # Add release date
        # Add genre names
        releasedate = result.get("release_date", {}).get("value", "N/A")
        if releasedate not in movie["releases"]:
            movie["releases"].append(releasedate)

    # Convert the dictionary values to a list of movies
    movies = list(movies_dict.values())

    # Check for "next" link in headers (if applicable)
    has_more_results = len(results["results"]["bindings"]) == 9999  # Check if fully retrieved
    if 'Link' in response.headers:
        links = response.headers['Link'].split(',')
        for link in links:
            if 'next' in link:
                endpoint = link.split('>')[0].strip()[1:]  # Extract next URL
                has_more_results = True  # Continue pagination with new endpoint
                break

    offset += 9999

# Write all movie data to JSON file
with open("cinema.json", "w", encoding='utf-8') as json_file:
    json.dump(list(movies_dict.values()), json_file, ensure_ascii=False, indent=4)
