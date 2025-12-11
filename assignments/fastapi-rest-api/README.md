# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a criar uma API REST usando o framework FastAPI do Python. Você construirá uma API simples para gerenciar uma lista de tarefas (To-Do List), incluindo operações de criar, ler, atualizar e deletar (CRUD).

## 📝 Tasks

### 🛠️	Criar Endpoints Básicos da API

#### Description
Crie uma API REST com FastAPI que permita gerenciar tarefas. Você deve implementar endpoints para listar todas as tarefas, obter uma tarefa específica por ID, criar novas tarefas, atualizar tarefas existentes e deletar tarefas.

#### Requirements
Completed program should:

- Ter um endpoint GET `/tasks` que retorna todas as tarefas
- Ter um endpoint GET `/tasks/{task_id}` que retorna uma tarefa específica
- Ter um endpoint POST `/tasks` que cria uma nova tarefa
- Ter um endpoint PUT `/tasks/{task_id}` que atualiza uma tarefa existente
- Ter um endpoint DELETE `/tasks/{task_id}` que deleta uma tarefa
- Usar modelos Pydantic para validação de dados
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)


### 🛠️	Adicionar Validação e Tratamento de Erros

#### Description
Implemente validação de dados usando Pydantic e adicione tratamento adequado de erros para casos como tarefa não encontrada ou dados inválidos.

#### Requirements
Completed program should:

- Validar que o título da tarefa não seja vazio
- Validar que o status da tarefa seja um dos valores permitidos (ex: "pending", "in_progress", "completed")
- Retornar erro 404 quando uma tarefa não for encontrada
- Retornar erro 422 quando os dados enviados forem inválidos
- Incluir mensagens de erro claras e descritivas


### 🛠️	Testar a API

#### Description
Teste sua API usando o FastAPI Swagger UI (disponível automaticamente em `/docs`) ou usando ferramentas como `curl` ou Postman. Documente exemplos de uso de cada endpoint.

#### Requirements
Completed program should:

- Incluir documentação de exemplo para cada endpoint no código
- Demonstrar a criação de pelo menos 3 tarefas diferentes
- Demonstrar atualização do status de uma tarefa
- Demonstrar deleção de uma tarefa
- Incluir exemplos de resposta de erro
