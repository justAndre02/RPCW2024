const express = require('express');
const axios = require('axios');
const app = express();

// Define route to retrieve list of students from GraphDB
app.get('/api/alunos', async (req, res) => {
  const groupBy = req.query.groupBy; // Obtém o parâmetro de agrupamento da URL
  const curso = req.query.curso; // Obtém o parâmetro do curso da URL
  

  if (groupBy === 'curso') {
    try {
      const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
      let sparqlQuery = `
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
        PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
        SELECT ?nome_curso (COUNT(?aluno) AS ?numAlunos) WHERE {
          ?aluno a tp:Aluno ;
          tp:hasCurso ?curso .
          ?curso :nome_curso ?nome_curso .
        } GROUP BY ?nome_curso ORDER BY ?nome_curso`;

      // Se o parâmetro curso também for fornecido, filtramos por curso na consulta SPARQL
      if (curso) {
        sparqlQuery = `
          PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
          PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
          SELECT ?nome_curso (COUNT(?aluno) AS ?numAlunos) WHERE {
            ?aluno a tp:Aluno ;
            tp:hasCurso ?curso ;
            ?curso :nome_curso "${curso}" .
          } GROUP BY ?nome_curso ORDER BY ?nome_curso`;
      }

      const response = await axios.get(graphDBEndpoint, {
        params: {
          query: sparqlQuery,
          format: 'json'
        },
        headers: {
          Accept: 'application/sparql-results+json'
        }
      });

      const cursos = response.data.results.bindings.map(binding => ({
        nome_curso: binding.nome_curso.value,
        num_alunos: binding.numAlunos.value
      }));

      res.json(cursos);
    } catch (error) {
      console.error('Error fetching data from GraphDB:', error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  } 
  if (groupBy === 'projeto') {
    try {
      const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
      const sparqlQuery = `
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
        PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
        SELECT ?notaProjeto (COUNT(?aluno) AS ?numAlunos) WHERE {
          ?aluno a tp:Aluno ;
          tp:hasProjeto ?projeto .
          ?projeto :nota_projeto ?notaProjeto .
        } GROUP BY ?notaProjeto ORDER BY ?notaProjeto`;

      const response = await axios.get(graphDBEndpoint, {
        params: {
          query: sparqlQuery,
          format: 'json'
        },
        headers: {
          Accept: 'application/sparql-results+json'
        }
      });

      const notasProjeto = response.data.results.bindings.map(binding => ({
        notaProjeto: binding.notaProjeto.value,
        num_alunos: binding.numAlunos.value
      }));

      res.json(notasProjeto);
    } catch (error) {
      console.error('Error fetching data from GraphDB:', error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  }
  if (groupBy === 'recurso') {
    try {
      const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
      const sparqlQuery = `
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
        PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
        SELECT ?idAluno ?nome ?nome_curso ?nota_recurso WHERE {
          ?aluno a tp:Aluno ;
          tp:id_aluno ?idAluno ;
          tp:nome_aluno ?nome ;
          tp:hasCurso ?curso .
          ?curso :nome_curso ?nome_curso .
          ?aluno tp:hasExame ?exame .
          ?exame :nome_exame "recurso" .
          ?exame :nota_exame ?nota_recurso .
        } ORDER BY ?nome`;

      const response = await axios.get(graphDBEndpoint, {
        params: {
          query: sparqlQuery,
          format: 'json'
        },
        headers: {
          Accept: 'application/sparql-results+json'
        }
      });

      const alunosRecurso = response.data.results.bindings.map(binding => ({
        idAluno: binding.idAluno.value,
        nome: binding.nome.value,
        nome_curso: binding.nome_curso.value,
        nota_recurso: binding.nota_recurso.value
      }));

      res.json(alunosRecurso);
    } catch (error) {
      console.error('Error fetching data from GraphDB:', error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  }
  else {
    // Se o parâmetro groupBy não for 'curso' ou não for fornecido, continua com a lógica original para retornar a lista de alunos
    try {
      const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
      let sparqlQuery = `
      PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
      PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
      SELECT ?idAluno ?nome ?nome_curso WHERE {
        ?aluno a tp:Aluno ;
        tp:id_aluno ?idAluno ;
        tp:nome_aluno ?nome ;
        tp:hasCurso ?curso .
        ?curso :nome_curso ?nome_curso .
      } ORDER BY ?nome`;

      // Se o parâmetro curso também for fornecido, filtramos por curso na consulta SPARQL
      if (curso) {
        sparqlQuery = `
          PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
          PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
          SELECT ?idAluno ?nome ?nome_curso WHERE {
            ?aluno a tp:Aluno ;
            tp:id_aluno ?idAluno ;
            tp:nome_aluno ?nome ;
            tp:hasCurso ?curso .
            ?curso :nome_curso ?nome_curso .
            FILTER(?nome_curso = "${curso}")
          } ORDER BY ?nome`;
      }

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
        nome_curso: binding.nome_curso.value
      }));

      res.json(alunos);
    } catch (error) {
      console.error('Error fetching data from GraphDB:', error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  }
});

app.get('/api/alunos/tpc', async (req, res) => {
  try {
    const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
    const sparqlQuery = `
    PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
    PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
    SELECT ?idAluno ?nome ?nome_curso (COUNT(?tpc) AS ?tpcs_feitos) WHERE {
      ?aluno a tp:Aluno ;
      tp:id_aluno ?idAluno ;
      tp:nome_aluno ?nome ;
      tp:hasCurso ?curso .
      ?curso :nome_curso ?nome_curso .
      OPTIONAL { ?aluno tp:hasTPC ?tpc . }
    } GROUP BY ?idAluno ?nome ?nome_curso
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
      nome_curso: binding.nome_curso.value,
      tpcs_feitos: binding.tpcs_feitos.value
    }));

    res.json(alunos);
  } catch (error) {
    console.error('Error fetching data from GraphDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/api/alunos/avaliados', async (req, res) => {
  try {
    const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
    const sparqlQuery = `
      PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
      PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
      SELECT ?idAluno ?nome ?nome_curso ?nota_projeto (MAX(?nota_exame) as ?nota_max_exame) (SUM(DISTINCT ?nota_tpc) as ?soma_tpcs) WHERE {
        ?aluno a tp:Aluno ;
        tp:id_aluno ?idAluno ;
        tp:nome_aluno ?nome ;
        tp:hasCurso ?curso ;
        tp:hasProjeto ?projeto .
        ?curso :nome_curso ?nome_curso .
        ?projeto :nota_projeto ?nota_projeto .
        OPTIONAL {
          ?aluno tp:hasExame ?exame .
          ?exame :nota_exame ?nota_exame .
        }
        OPTIONAL {
          ?aluno tp:hasTPC ?tpc .
          ?tpc :nota_tpc ?nota_tpc .
        }
      } GROUP BY ?idAluno ?nome ?nome_curso ?nota_projeto ORDER BY ?nome`;

    const response = await axios.get(graphDBEndpoint, {
      params: {
        query: sparqlQuery,
        format: 'json'
      },
      headers: {
        Accept: 'application/sparql-results+json'
      }
    });

    const alunos = response.data.results.bindings.map(binding => {
      const notaProjeto = parseFloat(binding.nota_projeto.value);
      const notaMaxExame = binding.nota_max_exame ? parseFloat(binding.nota_max_exame.value) : null;
      
      let notaFinal;
      
      // Verificar se a nota do projeto é inferior a 10 ou se a nota máxima do exame é inferior a 10
      if (notaProjeto < 10 || (notaMaxExame !== null && notaMaxExame < 10)) {
        notaFinal = "R";
      } else {
        // Calcular a nota final
        const tpcs = binding.soma_tpcs ? parseFloat(binding.soma_tpcs.value) : 0;
        const notaFinalCalculada = tpcs + (0.4 * notaProjeto) + (0.4 * notaMaxExame);
        
        // Verificar se a nota final calculada é inferior a 10
        if (notaFinalCalculada < 10) {
          notaFinal = "R";
        } else {
          notaFinal = notaFinalCalculada.toFixed(2); // Arredondar para duas casas decimais
        }
      }

      return {
        idAluno: binding.idAluno.value,
        nome: binding.nome.value,
        nome_curso: binding.nome_curso.value,
        notaFinal
      };
    });

    res.json(alunos);
  } catch (error) {
    console.error('Error fetching data from GraphDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/api/alunos/:id', async (req, res) => {
  try {
    const graphDBEndpoint = 'http://localhost:7200/repositories/Alunos';
    const sparqlQuery = `
    PREFIX : <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
    PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/avaliacao/>
    SELECT ?idAluno ?nome ?nome_curso ?nota_projeto ?id_tpc ?nota_tpc ?nome_exame ?nota_exame WHERE {
      ?aluno a tp:Aluno ;
      tp:id_aluno ?idAluno ;
      tp:nome_aluno ?nome ;
      tp:hasCurso ?curso ;
      tp:hasProjeto ?projeto.
      optional{?aluno tp:hasExame ?exam} .
      optional{?exam :nome_exame ?nome_exame} .
      optional{?exam :nota_exame ?nota_exame} .
      optional{?aluno tp:hasTPC ?tpc} .
      optional{?tpc :id_tpc ?id_tpc} .
      optional{?tpc :nota_tpc ?nota_tpc} .
      ?curso :nome_curso ?nome_curso .
      ?projeto :nota_projeto ?nota_projeto .
      FILTER(?idAluno = "${req.params.id}")
    }`;

    const response = await axios.get(graphDBEndpoint, {
      params: {
        query: sparqlQuery,
        format: 'json'
      },
      headers: {
        Accept: 'application/sparql-results+json'
      }
    });

    const aluno = {};
    const addedTPCs = new Set(); // Set to keep track of added TPCs
    const addedExams = new Set(); // Set to keep track of added exams

    response.data.results.bindings.forEach(binding => {
      const idAluno = binding.idAluno.value;
      if (!aluno.idAluno) {
        aluno.idAluno = idAluno;
        aluno.nome = binding.nome.value;
        aluno.nome_curso = binding.nome_curso.value;
        aluno.nota_projeto = binding.nota_projeto.value;
        aluno.tpcs = [];
        aluno.exames = [];
      }
      if (binding.id_tpc && binding.nota_tpc && !addedTPCs.has(binding.id_tpc.value)) {
        aluno.tpcs.push({
          id_tpc: binding.id_tpc.value,
          nota_tpc: binding.nota_tpc.value
        });
        addedTPCs.add(binding.id_tpc.value);
      }
      if (binding.nome_exame && binding.nota_exame && !addedExams.has(binding.nome_exame.value)) {
        aluno.exames.push({
          nome_exame: binding.nome_exame.value,
          nota_exame: binding.nota_exame.value
        });
        addedExams.add(binding.nome_exame.value);
      }
    });

    if (aluno.idAluno) {
      res.json(aluno);
    } else {
      res.status(404).json({ error: 'Aluno not found' });
    }
  } catch (error) {
    console.error('Error fetching data from GraphDB:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
