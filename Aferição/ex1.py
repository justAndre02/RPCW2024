import json

# Open the JSON file with UTF-8 encoding
with open('dataset.json', 'r', encoding='utf-8') as f:
    bd = json.load(f)

ttl = ""

for aluno in bd['alunos']:
    # Generate the TPC relations
    tpc_relations = ',\n'.join([f":{aluno['idAluno']}_{tpc['tp']}" for tpc in aluno['tpc']])
    # Generate the exam relations
    exam_relations = ',\n'.join([f":{aluno['idAluno']}_{exam}" for exam in aluno['exames']])

    registo = f"""
###  http://www.semanticweb.org/andre/ontologies/2024/avaliacao#{aluno['idAluno']}
:{aluno['idAluno']} rdf:type owl:NamedIndividual ,
                 :Aluno ;
        :hasCurso :{aluno['curso']} ;
        :hasExame {exam_relations} ;
        :hasProjeto :{aluno['idAluno']}_projeto ;
        :hasTPC {tpc_relations} ;
        :id_aluno "{aluno['idAluno']}" ;
        :nome_aluno "{aluno['nome']}" .
"""
    ttl += registo

    # Generate the TPC details
    for tpc in aluno['tpc']:
        ttl += f"""
###  http://www.semanticweb.org/andre/ontologies/2024/avaliacao#{aluno['idAluno']}_{tpc['tp']}
:{aluno['idAluno']}_{tpc['tp']} rdf:type owl:NamedIndividual ,
                      :TPC ;
             :id_tpc "{tpc['tp']}" ;
             :nota_tpc {tpc['nota']} .
"""

    # Generate the exam details
    for exam, nota in aluno['exames'].items():
        ttl += f"""
###  http://www.semanticweb.org/andre/ontologies/2024/avaliacao#{aluno['idAluno']}_{exam}
:{aluno['idAluno']}_{exam} rdf:type owl:NamedIndividual ,
                         :Exame ;
                :nome_exame "{exam}" ;
                :nota_exame {nota} .
"""

    # Generate the project details
    ttl += f"""
###  http://www.semanticweb.org/andre/ontologies/2024/avaliacao#{aluno['idAluno']}_projeto
:{aluno['idAluno']}_projeto rdf:type owl:NamedIndividual ,
                         :Projeto ;
                :nota_projeto {aluno['projeto']} .
"""

# Write the TTL data to a file
with open('output.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

print("TTL data has been written to output.ttl")