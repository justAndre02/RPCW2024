from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, OWL
import pprint
import json
from urllib.parse import quote

g = Graph()
g.parse("cinema.ttl")

with open('cinema.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
file.close()

cinema = Namespace("http://www.semanticweb.org/andre/ontologies/2024/cinema/")
# Assuming 'data' is a list of dictionaries where each dictionary represents a film
for film in data:
    film_uri = URIRef(f"""{cinema}{film['film'].replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů')}""")
    g.add((film_uri, RDF.type, cinema.Film))
    for films in film['title']:
        film_name = films.replace(' ', '_')
        film_name = quote(film_name)
        film_name = (film_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        g.add((film_uri, cinema.movie_title, Literal(film_name)))


    # ...

    for book in film['books']:
        book_name = book.replace(' ', '_')
        book_name = quote(book_name)
        book_name = (book_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', '"').replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if book_name == "N/A":
            book_uri = Literal("N/A")
        else:
            book_uri = URIRef(f"{cinema}{book_name}")
            g.add((book_uri, RDF.type, cinema.Book))
            g.add((book_uri, cinema.book_title, Literal(book_name)))
            g.add((film_uri, cinema.basedOf, book_uri))

    for actor in film['actors']:
        actor_name = actor['name'].replace(' ', '_')
        actor_birth = actor['birth_date']
        actor_name = quote(actor_name)
        actor_name = (actor_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if actor_name == "N/A":
            actor_uri = Literal("N/A")
        else:
            actor_uri = URIRef(f"{cinema}{actor_name}")
            g.add((actor_uri, RDF.type, cinema.Actor))
            g.add((actor_uri, cinema.name, Literal(actor_name)))
            g.add((actor_uri, cinema.birthDate, Literal(actor_birth)))
            g.add((film_uri, cinema.hasActor, actor_uri))

# ...

    for director in film['directors']:
        director_name = director['name'].replace(' ', '_')
        director_birth = director['birth_date']
        director_name = quote(director_name)
        director_name = (director_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if director_name == "N/A":
            director_uri = Literal("N/A")
        else:
            director_uri = URIRef(f"{cinema}{director_name}")
            g.add((director_uri, RDF.type, cinema.Director))
            g.add((director_uri, cinema.name, Literal(director_name)))
            g.add((director_uri, cinema.birthDate, Literal(director_birth)))
            g.add((film_uri, cinema.hasDirector, director_uri))

    # ...

    for writer in film['writers']:
        writer_name = writer['name'].replace(' ', '_')
        writer_birth = writer['birth_date']
        writer_name = quote(writer_name)
        writer_name = (writer_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if writer_name == "N/A":
            writer_uri = Literal("N/A")
        else:
            writer_uri = URIRef(f"{cinema}{writer_name}")
            g.add((writer_uri, RDF.type, cinema.Writer))
            g.add((writer_uri, cinema.name, Literal(writer_name)))
            g.add((writer_uri, cinema.birthDate, Literal(writer_birth)))
            g.add((film_uri, cinema.hasWriter, writer_uri))

    for screenwriter in film['screenwriters']:
        screenwriter_name = screenwriter['name'].replace(' ', '_')
        screenwriter_birth = screenwriter['birth_date']
        screenwriter_name = quote(screenwriter_name)
        screenwriter_name = (screenwriter_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if screenwriter_name == "N/A":
            screenwriter_uri = Literal("N/A")
        else:
            screenwriter_uri = URIRef(f"{cinema}{screenwriter_name}")
            g.add((screenwriter_uri, RDF.type, cinema.Screenwriter))
            g.add((screenwriter_uri, cinema.name, Literal(screenwriter_name)))
            g.add((screenwriter_uri, cinema.birthDate, Literal(screenwriter_birth)))
            g.add((film_uri, cinema.hasScreenwriter, screenwriter_uri))

    for soundtrack in film['soundtracks']:
        soundtrack_name = soundtrack['name'].replace(' ', '_')
        soundtrack_birth = soundtrack['birth_date']
        soundtrack_name = quote(soundtrack_name)
        soundtrack_name = (soundtrack_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if soundtrack_name == "N/A":
            soundtrack_uri = Literal("N/A")
        else:
            soundtrack_uri = URIRef(f"{cinema}{soundtrack_name}")
            g.add((soundtrack_uri, RDF.type, cinema.Musician))
            g.add((soundtrack_uri, cinema.name, Literal(soundtrack_name)))
            g.add((soundtrack_uri, cinema.birthDate, Literal(soundtrack_birth)))
            g.add((film_uri, cinema.hasComposer, soundtrack_uri))

    for producer in film['producers']:	
        producer_name = producer['name'].replace(' ', '_')
        producer_birth = producer['birth_date']
        producer_name = quote(producer_name)
        producer_name = (producer_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if producer_name == "N/A":
            producer_uri = Literal("N/A")
        else:
            producer_uri = URIRef(f"{cinema}{producer_name}")
            g.add((producer_uri, RDF.type, cinema.Producer))
            g.add((producer_uri, cinema.name, Literal(producer_name)))
            g.add((producer_uri, cinema.birthDate, Literal(producer_birth)))
            g.add((film_uri, cinema.hasProducer, producer_uri))

    # ...

    for genre in film['genres']:
        genre_name = genre.replace(' ', '_')
        genre_name = quote(genre_name)
        genre_name = (genre_name.replace(' ', '_').replace('%28', '').replace('%29', '')
                                 .replace('%3F', '?').replace('%27', "'").replace('%3A', ':').replace('%26', '&').replace('%C3%B3', 'ó')
                                 .replace('%C3%A9', 'é').replace('%C3%A1', 'á').replace('%C3%AD', 'í').replace('%C3%B1', 'ñ').replace('%C3%BA', 'ú')
                                 .replace('%C3%BC', 'ü').replace('%C3%BB', 'û').replace('%C3%AE', 'î').replace('%C3%AA', 'ê').replace('%C3%AE', 'î')
                                 .replace('%C3%B6', 'ö').replace('%C3%A7', 'ç').replace('%C3%A0', 'à').replace('%C3%A8', 'è').replace('%C3%B2', 'ò')
                                 .replace('%C3%B9', 'ù').replace('%C3%B8', 'ø').replace('%C3%B4', 'ô').replace('%C3%B5', 'õ').replace('%C3%A3', 'ã')
                                 .replace('%C3%A2', 'â').replace('%C3%AE', 'î').replace('%C3%AF', 'ï').replace('%C3%AB', 'ë').replace('%C3%A3', 'ã')
                                 .replace('%C3%A4', 'ä').replace('%C3%A5', 'å').replace('%C3%A6', 'æ').replace('%C3%BD', 'ý').replace('%C3%BD', 'ý')
                                 .replace('%C3%B7', '÷').replace('%C3%97', '×').replace('%C3%9F', 'ß').replace(',', '.').replace('%C3%9C', 'Ü')
                                 .replace('%22', "'").replace('%2C', ',').replace('%2E', '.').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';')
                                 .replace('%21', '!').replace('%C3%B0', 'ð').replace('%3C', '<').replace('%E2%80%99', '’').replace('%C4%A3', 'ģ').replace('%E2%80%93', '–')
                                 .replace('%C8%9B', 'ș').replace('%C8%9A', 'Ț').replace('%C8%99', 'ș').replace('%C8%98', 'Ș').replace('%C3%87', 'Ç').replace('%C3%86', 'Æ')
                                 .replace('%C3%85', 'Å').replace('%C3%84', 'Ä').replace('%C3%83', 'Ã').replace('%C3%82', 'Â').replace('%C3%81', 'Á').replace('%C3%80', 'À')
                                 .replace('%C3%9F', 'ß').replace('%C3%9E', 'Þ').replace('%C3%9C', 'Ü').replace('%C3%9B', 'Û').replace('%C3%9A', 'Ú').replace('%C3%99', 'Ù')
                                 .replace('%C3%98', 'Ø').replace('%C3%97', '×').replace('%C3%96', 'Ö').replace('%C3%95', 'Õ').replace('%C3%94', 'Ô').replace('%C3%93', 'Ó')
                                 .replace('%C3%92', 'Ò').replace('%C3%91', 'Ñ').replace('%C3%90', 'Ð').replace('%C3%8F', 'Ï').replace('%C3%8E', 'Î').replace('%C3%8D', 'Í')
                                 .replace('%C4%83', 'ă').replace('%C4%82', 'Ă').replace('%C4%9B', 'ě').replace('%C4%9A', 'Ě').replace('%C4%9D', 'ĝ').replace('%C4%9C', 'Ĝ')
                                 .replace('%C4%9F', 'ğ').replace('%C4%9E', 'Ğ').replace('%C4%A5', 'ĥ').replace('%C4%A4', 'Ĥ').replace('%C4%A9', 'ĩ').replace('%C4%A8', 'Ĩ')
                                 .replace('%C4%AF', 'į').replace('%C4%AE', 'Į').replace('%C4%B3', 'ĳ').replace('%C4%B2', 'Ĳ').replace('%C5%84', 'ń').replace('%C5%83', 'Ń')
                                 .replace('%C4%87', 'ć').replace('%C4%86', 'Ć').replace('%C4%8D', 'č').replace('%C4%8C', 'Č').replace('%C4%8F', 'ď').replace('%C4%8E', 'Ď')
                                 .replace('%C4%91', 'đ').replace('%C4%90', 'Đ').replace('%C4%97', 'ė').replace('%C4%96', 'Ė').replace('%C5%8D', 'ō').replace('%C5%8C', 'Ō')
                                 .replace('%C5%82', 'ł').replace('%C3%89', 'É').replace('%C5%84', 'ń').replace('%C5%83', 'Ń').replace('%C5%88', 'ň').replace('%C5%87', 'Ň')
                                 .replace('%C5%A1', 'š').replace('%C5%A0', 'Š').replace('(', '').replace(')', '').replace('%C5%AF', 'ů').replace('%C5%AE', 'Ů'))
        if genre_name == "N/A":
            genre_uri = Literal("N/A")
        else:
            genre_uri = URIRef(f"{cinema}{genre_name}")
            g.add((genre_uri, RDF.type, cinema.Genre))
            g.add((film_uri, cinema.hasGenre, genre_uri))

    length = film['length']
    if length.is_integer():
        hours = int(length) // 3600
        minutes = (int(length) % 3600) // 60
        length_str = f"{hours}:{minutes:02d}"
    else:
        hours = int(length) // 3600
        minutes = (int(length) % 3600) // 60
        seconds = int(length) % 60
        length_str = f"{hours}:{minutes:02d}:{seconds:02d}"

    g.add((film_uri, cinema.duration, Literal(length_str)))

    for release_date in film['releases']:
        if release_date == "N/A":
            g.add((film_uri, cinema.date, Literal("N/A")))
        else:
            g.add((film_uri, cinema.date, Literal(release_date)))

print(len(g))
with open('andre_pg54707.ttl', 'wb') as f:
    f.write(g.serialize().encode('utf-8'))
    print("=====================================")
    for smt in g:
        pprint.pprint(smt)