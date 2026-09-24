# Enterprise RAG Intelligence

Enterprise-style **Agentic Retrieval-Augmented Generation (RAG)** system built with Amazon Bedrock, Amazon Titan Embeddings, FAISS, LangChain, and Python.

The project demonstrates an end-to-end GenAI workflow for ingesting enterprise documents, performing semantic retrieval, routing queries, generating grounded answers, and validating responses through automated evaluation.

## Architecture

![Enterprise Agentic RAG Architecture](./enterprise_agentic_rag_architecture.png)

```text
User Query
    |
    v
Agent Router
    |
    +----------------------+
    |                      |
    v                      v
Grounded RAG         Source Retrieval
    |                      |
    v                      v
FAISS Retrieval      Evidence / Chunks
    |
    v
Amazon Bedrock
    |
    v
Grounded Answer + Sources
```

## Key Capabilities

- Agent-based routing between RAG generation and source retrieval
- Amazon Titan embeddings for semantic representation
- FAISS vector search for relevant document retrieval
- Amazon Bedrock for grounded LLM responses
- Source and chunk attribution for traceability
- Modular ingestion, chunking, retrieval, and generation pipeline
- Structured logging and observability
- Automated evaluation for answer accuracy and source grounding

## RAG Pipeline

```text
Enterprise Documents
        |
        v
Document Loader
        |
        v
Chunking
        |
        v
Amazon Titan Embeddings
        |
        v
FAISS Vector Store
        |
        v
Semantic Retrieval
        |
        v
Amazon Bedrock
        |
        v
Grounded Answer + Source Attribution
```

## Evaluation

The project includes an automated evaluation suite that validates both answer correctness and source grounding.

Current evaluation result:

```text
Test 1: PASS
Test 2: PASS
Test 3: PASS
Test 4: PASS
Test 5: PASS
Test 6: PASS

Evaluation Score: 6/6 passed
```

The evaluation verifies:

- Answer accuracy against expected responses
- Correct source retrieval
- Grounded response generation
- End-to-end RAG execution

## Example

**Question**

```text
How many days per week can employees work remotely?
```

**Response**

```text
Employees may work remotely three days per week.

SOURCES:
company_policy.json
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM Platform | Amazon Bedrock |
| Embeddings | Amazon Titan Embeddings |
| Vector Search | FAISS |
| RAG Orchestration | LangChain + Modular Python Pipeline |
| Agent Routing | Custom Query Router |
| Evaluation | Automated Python Evaluation Suite |
| Cloud Platform | AWS |

## Project Structure

```text
enterprise-rag-intelligence/
├── data/
│   ├── company_policy.json
│   └── it_security_policy.json
├── evaluation/
│   ├── run_evaluation.py
│   └── test_cases.json
├── src/
│   ├── agent_router.py
│   ├── chunking.py
│   ├── config.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── main.py
│   ├── observability.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── vector_store.py
├── enterprise_agentic_rag_architecture.png
├── requirements.txt
└── README.md
```

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure valid AWS credentials with access to Amazon Bedrock.

Example region:

```bash
export AWS_DEFAULT_REGION=us-east-2
```

## Run the RAG Application

```bash
python src/main.py --data data --question "How many days per week can employees work remotely?"
```

## Run Evaluation

```bash
python evaluation/run_evaluation.py
```

Expected result with the included sample dataset:

```text
Evaluation Score: 6/6 passed
```

## Security

AWS credentials and environment-specific secrets are excluded from source control.

Never commit:

- AWS access keys
- AWS secret access keys
- AWS session tokens
- `.env` files
- Local credential files

## Future Enhancements

- Bedrock Knowledge Bases
- Managed vector databases
- Hybrid semantic and keyword search
- Retrieval reranking
- Conversation memory
- Amazon Bedrock Guardrails
- Advanced RAG evaluation
- API deployment
- Web interface
- Monitoring and tracing dashboards

## Project Goal

This project demonstrates practical implementation of enterprise Generative AI patterns including **RAG, semantic search, vector retrieval, agent routing, grounding, source attribution, Amazon Bedrock integration, observability, and automated evaluation**.