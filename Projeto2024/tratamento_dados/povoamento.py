import json
import unicodedata

# Function to handle the unicode conversion
def convert_unicode(obj):
    if isinstance(obj, dict):
        return {convert_unicode(key): convert_unicode(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_unicode(element) for element in obj]
    elif isinstance(obj, str):
        return unicodedata.normalize('NFC', obj)
    else:
        return obj

ttl = """
@prefix : <http://rpcw.di.uminho.pt/2024/Diario_Replublica/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/Diario_Replublica/> .

<http://rpcw.di.uminho.pt/2024/Diario_Replublica> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/emitted
:emitted rdf:type owl:ObjectProperty ;
         rdfs:domain :Emitter ;
         rdfs:range :Document .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/hasEmitter
:hasEmitter rdf:type owl:ObjectProperty ;
            rdfs:domain :Document ;
            rdfs:range :Emitter .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/date
:date rdf:type owl:DatatypeProperty ;
      rdfs:domain :Document ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/docType
:docType rdf:type owl:DatatypeProperty ;
         rdfs:domain :Document ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/emitter_name
:emitter_name rdf:type owl:DatatypeProperty ;
              rdfs:domain :Emitter ;
              rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/notes
:notes rdf:type owl:DatatypeProperty ;
       rdfs:domain :Document ;
       rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/number
:number rdf:type owl:DatatypeProperty ;
        rdfs:domain :Document ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/numberDR
:numberDR rdf:type owl:DatatypeProperty ;
          rdfs:domain :Document ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/series
:series rdf:type owl:DatatypeProperty ;
        rdfs:domain :Document ;
        rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/source
:source rdf:type owl:DatatypeProperty ;
        rdfs:domain :Document ;
        rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/Document
:Document rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/Emitter
:Emitter rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################
"""

# Open the output file
output = open("DR_povoada.ttl", "w", encoding='utf-8')

# Write the prefixes and ontology definitions to the output file
output.write(ttl)

emitters = []
for i in range(1, 11):
    with open(f"2024-04-14-DRE_dump_part{i}.json", 'r', encoding='utf-8') as f:
        bd = json.load(f)
        bd = convert_unicode(bd)
        print(f"Part {i} loaded")

    emitters = []
    for doc in bd:
        id = doc["claint"]
        date = doc["date"]
        docType = doc["doc_type"]
        emitter_list = doc["emiting_body"]
        notes = doc["notes"]
        number = doc["number"]
        numberDR = doc["dr_number"]
        series = doc["series"]
        source = doc["source"]
        
        emitter_data = ""
        for emitter in emitter_list:
            emitter = emitter.replace(' ', '_').replace(',','').replace('.','').replace('"', '').replace('(','').replace(')','').replace('º','').replace('ª','').replace('«','').replace('»','').replace("'","").replace('/','_').replace('–','').replace('%', 'Porcento').replace('_¿', '').replace('-_','').replace('°', '').replace('!', '').replace('?', '').replace('+', 'Mais').replace('[', '').replace(']', '').replace('_', '').replace('@', '_arroba_').replace('=', '_igual_a_').replace('´', '_').replace('&', 'E')
            if emitter not in emitters:
                emitters.append(emitter)
            s = f"""
                                                    :hasEmitter :{emitter} ;"""
            emitter_data += s
        documento = f"""
###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/{id}
<http://rpcw.di.uminho.pt/2024/Diario_Replublica/{id}> rdf:type owl:NamedIndividual ,
                                                            :Document ;
{emitter_data[1:]}
                                                    :date "{date.replace(',','').replace('.','').replace('"', '')}" ;
                                                    :docType "{docType.replace(',','').replace('.','').replace('"', '')}" ;
                                                    :notes "{notes.replace(',','').replace('.','').replace('"', '')}" ;
                                                    :number "{number.replace(',','').replace('.','').replace('"', '')}" ;
                                                    :numberDR "{numberDR.replace(',','').replace('.','').replace('"', '')}" ;
                                                    :series {series} ;
                                                    :source "{source.replace(',','').replace('.','').replace('"', '')}" .

###  http://rpcw.di.uminho.pt/2024/Diario_Replublica/{emitter}
:{emitter} rdf:type owl:NamedIndividual ,
                                               :Emitter ;
                                      :emitted :{id} ;
                                      :emitter_name "{emitter.replace('_', ' ')}" .
"""
        output.write(documento)

# Write the final line to the output file
output.write("###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi")

output.close()
