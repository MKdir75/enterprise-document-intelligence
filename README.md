Enterprise Document Intelligence & RAG Backend

An enterprise-oriented backend system for secure document management, role-based access control, document retrieval, knowledge graph integration, and Retrieval-Augmented Generation (RAG).

The project is built with Django and Django REST Framework and integrates PostgreSQL, JWT authentication, RBAC, LangChain, and OpenAI to provide a secure foundation for document-aware AI applications.

🚀 Project Overview

The goal of this project is to build a backend system where users can securely access organizational documents and ask natural-language questions about authorized information.

The system combines traditional backend engineering with AI-powered document retrieval.

At a high level:

Client / Postman
       │
       ▼
Django REST Framework
       │
       ├── JWT Authentication
       │
       ├── Role-Based Access Control
       │
       ├── Document Authorization
       │
       ├── Document Management
       │
       ├── Knowledge Graph
       │
       └── RAG Query System
                │
                ▼
          LangChain
                │
                ▼
           OpenAI API
                │
                ▼
          RAG Response
✨ Key Features
Authentication
User registration
JWT-based authentication
Access token
Refresh token
Protected API endpoints
Authorization
Role-Based Access Control (RBAC)
Role-based API permissions
ADMIN, ANALYST, and USER roles
Permission enforcement on protected resources
Department-aware document access
Document Management
Create documents
Retrieve documents
Document filtering
Document activation/deactivation
Department-based document organization
Document chunk management
RAG
Natural-language document queries
Relevant document retrieval
Context-aware answer generation
Source-aware responses
LangChain integration
OpenAI API integration
Knowledge Graph
Entity management
Relationship management
Entity types
Relationship-based knowledge retrieval
Knowledge graph information can be used alongside document retrieval
Audit Logging
User activity tracking
RAG query logging
Resource/action tracking
Audit history for important operations
Containerization
Docker support
Docker Compose support
PostgreSQL container support
Environment-based configuration
🛠️ Technology Stack
Technology	Purpose
Python	Backend programming
Django	Web framework
Django REST Framework	REST API development
PostgreSQL	Relational database
JWT	Authentication
RBAC	Authorization
LangChain	LLM/RAG orchestration
RAG	Retrieval-Augmented Generation
OpenAI API	AI-powered response generation
Docker	Containerization
Docker Compose	Multi-container development
Postman	API testing
Git/GitHub	Version control
📁 Project Structure
enterprise-document-intelligence/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── ...
│
├── documents/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
│
├── knowledge_graph/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── rag/
│   ├── services/
│   ├── views.py
│   └── ...
│
├── audit_logs/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── .env.example
├── .gitignore
└── README.md

The exact application structure may change as the project evolves.

🔐 Authentication Flow

The application uses JWT authentication.

User
 │
 ▼
Login
 │
 ▼
Access Token + Refresh Token
 │
 ▼
Authenticated API Request
 │
 ▼
JWT Validation
 │
 ▼
Permission Check
 │
 ▼
Protected Resource

Clients include the access token in the request:

Authorization: Bearer <access_token>

When the access token expires, the refresh token can be used to obtain a new access token.

👥 Role-Based Access Control

The application currently uses role-based permissions.

The main roles are:

ADMIN
ANALYST
USER

A simplified permission model:

ADMIN
 ├── Administrative operations
 ├── Manage authorized resources
 └── Elevated permissions

ANALYST
 ├── Create/manage permitted documents
 ├── Perform authorized analysis
 └── Query accessible information

USER
 ├── Access permitted resources
 └── Perform authorized queries

Actual permissions are enforced by the backend rather than relying on the client.

📄 Document Access

Document access is controlled by authorization rules.

Documents can contain information such as:

Document
├── Title
├── Content
├── Department
├── Document Type
├── Status
└── Metadata

The backend applies authorization and filtering before returning protected document information.

This prevents users from automatically accessing documents outside their permitted scope.

🧠 RAG Architecture

The RAG system follows a retrieval-and-generation workflow.

User Question
      │
      ▼
Authentication
      │
      ▼
Authorization
      │
      ▼
Query Processing
      │
      ▼
Document Retrieval
      │
      ▼
Relevant Document Chunks
      │
      ▼
Context Construction
      │
      ▼
LangChain
      │
      ▼
OpenAI API
      │
      ▼
Generated Answer
      │
      ▼
Sources / Response

The purpose of RAG is to provide the language model with relevant retrieved information instead of relying only on the model's general knowledge.

🔗 Knowledge Graph

The project also contains a knowledge graph layer.

The graph consists of:

Entity
   │
   │ Relationship
   ▼
Entity

For example:

Engineering Department
        │
       USES
        │
        ▼
       JWT

Entities can represent different types of information, such as:

PERSON
ORGANIZATION
PROJECT
PRODUCT
TECHNOLOGY
LOCATION
OTHER

Relationships connect entities using defined relationship types.

📝 Audit Logging

The system records important user activities through audit logs.

An audit record can contain information such as:

User
Action
Resource Type
Resource ID
Timestamp

For example:

User: analyst
Action: QUERY
Resource Type: RAGQuery
Resource ID: 1

Audit logging helps provide visibility into how protected resources and RAG functionality are being used.

🌐 API

The application exposes REST APIs through Django REST Framework.

Examples of API categories include:

Authentication
Documents
Knowledge Graph
RAG
Audit Logs

Typical authentication endpoints include:

POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/token/refresh/

Example protected resources:

/api/documents/
/api/rag/
/api/knowledge-graph/
/api/audit-logs/

Endpoint paths may vary depending on the current project configuration. Check config/urls.py for the authoritative API routes.

🧪 API Testing

The APIs can be tested using Postman.

Recommended testing order:

1. Register user
       ↓
2. Login
       ↓
3. Copy access token
       ↓
4. Add Bearer token
       ↓
5. Test protected endpoints
       ↓
6. Test role-based permissions
       ↓
7. Create/retrieve documents
       ↓
8. Test RAG queries
       ↓
9. Check audit logs

Example authorization header:

Authorization: Bearer <access_token>
⚙️ Environment Variables

Create a .env file in the project root.

Example:

DEBUG=True

SECRET_KEY=your-secret-key

POSTGRES_DB=enterprise_document_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-password
POSTGRES_HOST=db
POSTGRES_PORT=5432

OPENAI_API_KEY=your-openai-api-key

Never commit the real .env file or API keys to GitHub.

A .env.example file should be provided for development reference.

🐳 Docker Setup

The project supports containerized development using Docker.

Build and start the services:

docker compose up --build

Run in detached mode:

docker compose up -d

Stop the containers:

docker compose down

View running containers:

docker compose ps

View logs:

docker compose logs

For a specific service:

docker compose logs web

Service names depend on the project's docker-compose.yml.

💻 Local Development Setup
1. Clone the repository
git clone https://github.com/MKdir75/enterprise-document-intelligence.git

Move into the project:

cd enterprise-document-intelligence
2. Create a virtual environment

Windows:

python -m venv venv

Activate:

venv\Scripts\activate

Linux/macOS:

python3 -m venv venv

Activate:

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create:

.env

and add the required configuration.

5. Run migrations
python manage.py makemigrations
python manage.py migrate
6. Start the development server
python manage.py runserver

The development server will normally be available at:

http://127.0.0.1:8000/
🔒 Security Considerations

The project is designed with several backend security concepts in mind:

JWT authentication
Role-based authorization
Protected REST APIs
Server-side permission checks
Environment-based secret configuration
Document access restrictions
Audit logging
Database-backed authorization
Separation of authentication and authorization concerns

Secrets such as:

OPENAI_API_KEY
SECRET_KEY
POSTGRES_PASSWORD

must never be committed to the repository.

🗄️ Database

PostgreSQL is used as the primary relational database.

The database stores application data such as:

Users
Documents
Document Chunks
Entities
Relationships
Audit Logs

The Django ORM is used to interact with PostgreSQL.

🔄 High-Level Request Flow

A protected document/RAG request follows a flow similar to:

HTTP Request
     │
     ▼
Django
     │
     ▼
DRF
     │
     ▼
JWT Authentication
     │
     ▼
RBAC / Permission Check
     │
     ▼
Business Logic
     │
     ├───────────────┐
     ▼               ▼
PostgreSQL       RAG Pipeline
                     │
                     ▼
                  LangChain
                     │
                     ▼
                 OpenAI API
                     │
                     ▼
                  Response
📌 Current Project Focus

The main engineering focus of this project is:

Secure authentication
Role-based authorization
Document access control
Document retrieval
RAG-based question answering
Knowledge graph integration
Auditability
PostgreSQL-backed data management
Dockerized backend development
AI integration through OpenAI
🚧 Future Improvements

Potential future improvements include:

More advanced document ingestion
Additional document formats
Improved chunking strategies
Vector database integration
Embedding-based semantic search
Advanced RAG evaluation
API throttling
More comprehensive input validation
Improved OpenAI error handling
Structured application logging
Automated testing
CI/CD pipeline
Production deployment
Monitoring and observability
📚 Learning Goals

This project was built to practice and demonstrate backend engineering concepts including:

Django architecture
REST API development
Authentication
Authorization
RBAC
Database design
PostgreSQL
Secure API development
RAG architecture
LLM integration
LangChain
Knowledge graphs
Docker
Backend system design