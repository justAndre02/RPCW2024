import json

# Open the JSON file with UTF-8 encoding
with open('mapa.json', 'r', encoding='utf-8') as f:
    bd = json.load(f)

ttl = ""

for cidade in bd['cidades']:
    registo = f"""
###  http://rpcw.di.uminho.pt/2024/mapa#{cidade['id']}
                                :{cidade['id']} rdf:type owl:NamedIndividual ,
                                            :Cidade ;
                                    :distrito "{cidade['distrito'].replace(" ", "_")}" ;
                                    :idCidade "{cidade['id']}" ;
                                    :nome "{cidade['nome'].replace(" ", "_")}" ;
                                    :populacao {cidade['população']} .
"""
    ttl += registo

for ligacao in bd['ligacoes']:
    registo = f"""
###  http://rpcw.di.uminho.pt/2024/mapa#{ligacao['id']}
                                :{ligacao['id']} rdf:type owl:NamedIndividual ,
                                            :Ligacao ;
                                    :destinoLigacao :{ligacao['destino']} ;
                                    :origemLigacao :{ligacao['origem']} ;
                                    :distancia {ligacao['distância']} ;
                                    :idLigacao "{ligacao['id']}" .
"""
    ttl += registo

# Write the TTL data to a file
with open('output.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

print("TTL data has been written to output.ttl")