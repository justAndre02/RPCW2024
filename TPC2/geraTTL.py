import json

# Open the JSON file with UTF-8 encoding
with open('dataset.json', 'r', encoding='utf-8') as f:
    bd = json.load(f)

ttl = ""

for planta in bd:
    registo = f"""
###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Estado'].replace(" ", "_")}
:{planta['Estado'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                 :Estado .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Freguesia'].replace(" ", "_")}
:{planta['Freguesia'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                      :Freguesia .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Gestor'].replace(" ", "_")}
:{planta['Gestor'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
               :Gestor .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Rua'].replace(" ", "_")}
:{planta['Rua'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                          :Rua .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Local'].replace(" ", "_")}
:{planta['Local'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                     :Local .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Espécie'].replace(" ", "_")}
:{planta['Espécie'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                         :Espécie .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Id']}
<http://rpcw.di.uminho.pt/2024/plantas#{planta['Id']}> rdf:type owl:NamedIndividual ,
                                                          :Planta ;
                                                 :temAtualização :{planta['Data de actualização'].replace(" ", "_")};
                                                 :temEspécie :{planta['Espécie'].replace(" ", "_")} ;
                                                 :temEstado :{planta['Estado'].replace(" ", "_")} ;
                                                 :temFreguesia :{planta['Freguesia'].replace(" ", "_")} ;
                                                 :temGestor :{planta['Gestor'].replace(" ", "_")} ;
                                                 :temIntervenções :{planta['Número de intervenções']} ;
                                                 :temLocal :{planta['Local'].replace(" ", "_")} ;
                                                 :temRua :{planta['Rua'].replace(" ", "_")} ;
                                                 :caldeira "{planta['Caldeira']}" ;
                                                 :id {planta['Id']} ;
                                                 :implantação "{planta['Implantação'].replace(" ", "_")}" ;
                                                 :nome_cientifico "{planta['Nome Científico'].replace(" ", "_")}" ;
                                                 :numero_registo {planta['Número de Registo']} ;
                                                 :tutor "{planta['Tutor']}" .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Data de actualização'].replace(" ", "_")}
:{planta['Data de actualização'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
            :DataAtualização .


###  http://rpcw.di.uminho.pt/2024/plantas#{planta['Número de intervenções']}
:{planta['Número de intervenções']} rdf:type owl:NamedIndividual ,
            :Intervenções .
"""
    
    ttl += registo

# Write the TTL data to a file
with open('output.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

print("TTL data has been written to output.ttl")
