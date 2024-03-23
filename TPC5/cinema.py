import requests
import json


# Define the DBpedia SPARQL endpoint
endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query to fetch movies with additional information
query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbp: <http://dbpedia.org/property/>
select distinct ?film ?film_title ?book_name ?actor_name ?actor_birth ?director_name ?director_birth ?writer_name ?writer_birth ?screen_writer ?screen_writer_birth ?music_composers ?composers_birth ?producer_name ?producer_birth ?length ?release_date ?film_genres  where {
    ?film rdf:type <http://dbpedia.org/ontology/Film> .
    optional {?film dbp:name ?film_title.
            FILTER(LANG(?film_title) = "en")}
    optional {?film dbp:basedOn ?book.
            ?book rdfs:label ?book_name .
            FILTER(LANG(?book_name) = "en")}
    optional {?film dbo:starring ?actor.
            ?actor rdfs:label ?actor_name .
            ?actor dbo:birthDate ?actor_birth .
            FILTER(LANG(?actor_name) = "en")}
    optional {?film dbo:director ?director.
            ?director rdfs:label ?director_name .
            ?director dbo:birthDate ?director_birth .
            FILTER(LANG(?director_name) = "en")}
    optional {?film dbo:writer ?writer.
            ?writer rdfs:label ?writer_name .
            ?writer dbo:birthDate ?writer_birth .
            FILTER(LANG(?writer_name) = "en")}
    optional {?film dbp:screenplay ?screen_play.
            ?screen_play rdfs:label ?screen_writer .
            ?screen_play dbo:birthDate ?screen_writer_birth .
            FILTER(LANG(?screen_writer) = "en")}
    optional {?film dbp:music ?soundtrack.
            ?soundtrack rdfs:label ?music_composers .
            ?soundtrack dbo:birthDate ?composers_birth .
            FILTER(LANG(?music_composers) = "en")}
    optional {?film dbo:producer ?producer.
            ?producer rdfs:label ?producer_name .
            ?producer dbo:birthDate ?producer_birth .
            FILTER(LANG(?producer_name) = "en")}
    optional {?film dbo:runtime ?length .}
    optional {?film dbo:releaseDate ?release_date .}
    optional {?film dbp:genre ?film_genre.
            ?film_genre rdfs:label ?film_genres .
            FILTER(LANG(?film_genres) = "en")}

} group by ?film ?film_title ?book_name ?actor_name ?director_name ?writer_name ?screen_writer ?music_composers ?producer_name ?length ?release_date ?film_genres
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
        movie_link = result.get("film", {}).get("value", "N/A")

        # Check if the movie title already exists in the dictionary
        if movie_link not in movies_dict:
            movie = {}
            movie["film"] = movie_link
            movie["title"] = []
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

            movies_dict[movie_link] = movie

        movie = movies_dict[movie_link]

        # Add movie title
        movie_title = result.get("film_title", {}).get("value", "N/A")
        if movie_title not in movie["title"]:
            movie["title"].append(movie_title)
        
        # Add book names
        book_name = result.get("book_name", {}).get("value", "N/A")
        if book_name not in movie["books"]:
            movie["books"].append(book_name)


        # Add actor names if not already present in the movie
        actor_name = result.get("actor_name", {}).get("value", "N/A")
        actor_birth = result.get("actor_birth", {}).get("value", "N/A")
        if not any(actor_info["name"] == actor_name and actor_info["birth_date"] == actor_birth for actor_info in movie["actors"]):
            actor_info = {"name": actor_name, "birth_date": actor_birth}
            movie["actors"].append(actor_info)

        # Add director names
        director_name = result.get("director_name", {}).get("value", "N/A")
        director_birth = result.get("director_birth", {}).get("value", "N/A")
        if not any(director_info["name"] == director_name and director_info["birth_date"] == director_birth for director_info in movie["directors"]):
            director_info = {"name": director_name, "birth_date": director_birth}
            movie["directors"].append(director_info)

        # Add writer names
        writer_name = result.get("writer_name", {}).get("value", "N/A")
        writer_birth = result.get("writer_birth", {}).get("value", "N/A")
        if not any(writer_info["name"] == writer_name and writer_info["birth_date"] == writer_birth for writer_info in movie["writers"]):
            writer_info = {"name": writer_name, "birth_date": writer_birth}
            movie["writers"].append(writer_info)

        # Add screenwriter names
        screen_writer = result.get("screen_writer", {}).get("value", "N/A")
        screen_writer_birth = result.get("screen_writer_birth", {}).get("value", "N/A")
        if not any(screen_writer_info["name"] == screen_writer and screen_writer_info["birth_date"] == screen_writer_birth for screen_writer_info in movie["screenwriters"]):
            screen_writer_info = {"name": screen_writer, "birth_date": screen_writer_birth}
            movie["screenwriters"].append(screen_writer_info)

        # Add soundtrack names
        soundtrack = result.get("music_composers", {}).get("value", "N/A")
        composer_birth = result.get("composers_birth", {}).get("value", "N/A")
        if not any(composers_info["name"] == soundtrack and composers_info["birth_date"] == composer_birth for composers_info in movie["soundtracks"]):
            composers_info = {"name": soundtrack, "birth_date": composer_birth}
            movie["soundtracks"].append(composers_info)

        # Add producer names
        producer_name = result.get("producer_name", {}).get("value", "N/A")
        producer_birth = result.get("producer_birth", {}).get("value", "N/A")
        if not any(producer_info["name"] == producer_name and producer_info["birth_date"] == producer_birth for producer_info in movie["producers"]):
            producer_info = {"name": producer_name, "birth_date": producer_birth}
            movie["producers"].append(producer_info)

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
