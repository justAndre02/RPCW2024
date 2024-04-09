const express = require('express');
const axios = require('axios');
const app = express();

// Define route to retrieve list of students from GraphDB
app.get('/api/alunos', async (req, res) => {
  try {
    const graphDBEndpoint = 'http://98aceee95a96:7200/repositories/Alunos';
    const sparqlQuery = `
      PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
      SELECT ?idAluno ?nome ?curso WHERE {
        ?aluno a tp:Aluno ;
               tp:id_aluno ?idAluno ;
               tp:nome_aluno ?nome ;
        ?nome :hasCurso ?curso .
      }
      ORDER BY ?nome`;

    const response = await axios.get(graphDBEndpoint, {
      params: {
        query: sparqlQuery,
        format: 'json'
      },
      headers: {
        Accept: 'application/sparql-results+json'
      }
    });

    const alunos = response.data.results.bindings.map(binding => ({
      idAluno: binding.idAluno.value,
      nome: binding.nome.value,
      curso: binding.curso.value
    }));

    res.json(alunos);
  } catch (error) {
    console.error('Error fetching data from GraphDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
