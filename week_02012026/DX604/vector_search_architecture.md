# Vector Search Architecture - MongoDB Atlas

## How Mermaid Diagrams Work

Mermaid is a text-based diagramming tool that converts simple text syntax into diagrams. It's widely supported in:
- **GitHub/GitLab** - renders automatically in markdown files
- **Cursor/VS Code** - with Mermaid preview extensions
- **Notion, Confluence** - many documentation platforms
- **Jupyter Notebooks** - can render with appropriate extensions

### Basic Syntax

1. **Start with diagram type**: `flowchart LR` (Left-to-Right), `flowchart TD` (Top-Down)
2. **Define nodes**: `A[Text in box]`, `B(Text in rounded)`, `C{Diamond}`
3. **Connect nodes**: `A --> B` (arrow), `A --- B` (line)
4. **Subgraphs**: Group related elements
5. **Styling**: Use special characters for different shapes

### Node Shape Syntax
- `A[Rectangle]` - rectangular box
- `A(Rounded)` - rounded corners
- `A{Diamond}` - decision diamond
- `A[(Database)]` - cylinder/database shape
- `A((Circle))` - circle

---

## Architecture Diagram

```mermaid
flowchart LR

    A[Client / UI / API<br/>Search request] --> B[POC Search Service<br/>(Python / Java / API layer)]

    %% -------------------------
    %% Ingestion path
    %% -------------------------
    subgraph INGESTION["Ingestion / Indexing path"]
        C[Source documents<br/>(files, tickets, wiki, etc.)] --> D[Pre-processing / chunking]

        D --> E1[Embedding service<br/>Voyage AI (API)]
        D --> E2[Self-hosted embedding model<br/>MiniLM or E5]

        E1 --> F[(MongoDB Atlas Collection)]
        E2 --> F
    end

    %% -------------------------
    %% Storage
    %% -------------------------
    subgraph ATLAS["MongoDB Atlas"]
        F[(Documents + metadata<br/>+ embeddings)]
        G1[Vector Index<br/>embedding_minilm (384)]
        G2[Vector Index<br/>embedding_e5 (768)]
    end

    %% -------------------------
    %% Query path
    %% -------------------------
    B --> H[Query embedding<br/>(same model as index)]

    H --> Q1[Voyage AI<br/>(optional)]
    H --> Q2[Self-hosted model]

    Q1 --> B
    Q2 --> B

    B --> I[MongoDB Atlas Vector Search<br/>(knn + filters)]

    I --> F
    I --> G1
    I --> G2

    I --> J[Top-K results]
    J --> A
```

---

## Architecture Overview

### Components

**1. Ingestion Path**
- Source documents are collected from various sources
- Pre-processing and chunking prepare text for embedding
- Two embedding options:
  - **Voyage AI** (API-based, external service)
  - **Self-hosted models** (MiniLM 384-dim or E5 768-dim)
- Embeddings stored in MongoDB Atlas Collection

**2. Storage Layer (MongoDB Atlas)**
- Documents stored with metadata and embeddings
- Two vector indexes:
  - `embedding_minilm` - 384 dimensions
  - `embedding_e5` - 768 dimensions

**3. Query Path**
- Client sends search request to POC Search Service
- Query text is embedded using the same model as the index
- Vector search performed using k-nearest neighbors (knn) with filters
- Top-K most relevant results returned to client

---

## How to View This Diagram

### Option 1: GitHub/GitLab
Push this file to a repository and view it online - Mermaid renders automatically.

### Option 2: VS Code/Cursor
1. Install "Markdown Preview Mermaid Support" extension
2. Open this file
3. Press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows/Linux) for preview

### Option 3: Online Tools
Copy the mermaid code block and paste into:
- https://mermaid.live/ (official editor)
- https://mermaid.ink/ (generates images)

### Option 4: Export as Image
Use mermaid-cli:
```bash
npm install -g @mermaid-js/mermaid-cli
mmdc -i vector_search_architecture.md -o diagram.png
```

---

## Tips for Creating Mermaid Diagrams

1. **Use comments**: `%% This is a comment` to organize your code
2. **Break lines in nodes**: Use `<br/>` for multi-line text
3. **Subgraphs**: Group related components for clarity
4. **Keep it simple**: Too many connections can make diagrams hard to read
5. **Test incrementally**: Build the diagram piece by piece
6. **Use meaningful IDs**: `A`, `B`, `C` vs `clientNode`, `serviceNode` (both work, choose what's readable)

## Common Diagram Types

- `flowchart` - Process flows, architecture diagrams
- `sequenceDiagram` - API interactions, message flows
- `classDiagram` - Object-oriented design
- `erDiagram` - Database schemas
- `gantt` - Project timelines
- `pie` - Data distributions
- `gitGraph` - Git branching strategies
