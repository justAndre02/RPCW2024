import json

# Open the JSON file with UTF-8 encoding
with open('dataset.json', 'r', encoding='utf-8') as f:
    bd = json.load(f)

ttl = ""

for aluno in bd['alunos']:
    registo = f"""
###  http://rpcw.di.uminho.pt/2024/escola_musica#{aluno['id']}
                                            :{aluno['id']} rdf:type owl:NamedIndividual ,
                                                        :aluno ;
                                            :temCurso :{aluno['curso']} ;
                                            :temInstrumentoAluno :{aluno['instrumento']} ;
                                            :ano_aluno {aluno['anoCurso']} ;
                                            :data_nascimento "{aluno['dataNasc']}" ;
                                            :id_aluno "{aluno['id']}" ;
                                            :nome_aluno "{aluno['nome']}" .
"""
    ttl += registo

for curso in bd['cursos']:
    registo = f"""
###  http://rpcw.di.uminho.pt/2024/escola_musica#{curso['id']}
                                            :{curso['id']} rdf:type owl:NamedIndividual ,
                                                        :curso ;
                                            :temInstrumento :{curso['instrumento']['#text']} ;
                                            :designacao_curso "{curso['designacao']}" ;
                                            :duracao_curso {curso['duracao']} ;
                                            :id_curso "{curso['id']}" .
"""
    ttl += registo

for instrumento in bd['instrumentos']:
    registo = f"""
###  http://rpcw.di.uminho.pt/2024/escola_musica#{instrumento['#text']}
                                            :{instrumento['#text']} rdf:type owl:NamedIndividual ,
                                                            :instrumento ;
                                                    :id_instrumento "{instrumento['id']}" ;
                                                    :nome_instrumento "{instrumento['#text']}" .
"""
    ttl += registo

# Write the TTL data to a file
with open('output.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

print("TTL data has been written to output.ttl")
