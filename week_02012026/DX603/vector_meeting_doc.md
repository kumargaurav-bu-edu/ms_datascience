# Proposal: Model-Based Vector Search for Customer Data

**Meeting with manager — [Date]**  
**Subject:** Moving from Elasticsearch to model-based vector search for customer/entity matching

---

## 1. Executive summary

I'm proposing we evaluate and eventually adopt **model-based vector search** for our customer data (and related entities) instead of relying only on Elasticsearch. Vector search can fix real matching failures we're seeing today and improve findability, but the change is non-trivial in implementation effort, integration, and cost. This document outlines the benefits, evidence from our own cases, and the main challenges so we can decide together how to prioritize and escalate.

---

## 2. Why consider moving from Elasticsearch to vector search?

Today we rely heavily on **Elasticsearch** for searching customer and related records. It's great for **keyword and exact/text matching**, but it struggles when:

- Names and labels are **phrased differently** but refer to the same entity.
- We care about **semantic similarity** (meaning) rather than literal string overlap.
- **Context** (e.g., location, type) should influence which match is best.

**Model-based vector search** encodes text into numerical vectors so we can compare **meaning**, not just keywords. That leads to better matching for entities like companies, people, and addresses, especially when naming and formatting vary.

---

## 3. Evidence from our own data

Two concrete cases show where Elasticsearch falls short and where a semantic/vector approach would help.

### Example 1: CMS Energy vs Consumer Energy

- **Issue:** Queries don't match well when company names are similar but not identical (e.g., "CMS Energy Corporation" vs "Consumer Energy Corporations").
- **Why Elasticsearch struggles:** Matching is driven by tokens and text. Slight wording or spelling differences reduce or block matches even when country, city, and other parameters align.
- **How vector search helps:** A model can place "CMS Energy Corporation" and "Consumer Energy Corporations" close in vector space when context (country, city, sector) is similar, so we can still surface the right entity.

### Example 2: Wells Fargo entity matching

- **Input:** "Wells Fargo & Company"
- **Observed output:** "Wells Fargo Bank, National Association" was ranked above the correct entity.
- **Expected:** "Wells Fargo & Company" should rank first.
- **Why it failed:** The search logic was heavily influenced by **location**. The location attached to the input favored the "Bank, National Association" record, so keyword + location rules preferred the wrong entity.
- **How vector search helps:** By encoding the **entity name and context** into vectors, we can emphasize "same real-world entity" over minor wording or location biases, and combine vector similarity with business rules (e.g., preferred entity type) in a controlled way.

These examples are strong evidence that we need **semantic/vector-aware search** in addition to (or in place of) pure keyword search for critical customer data.

---

## 4. Benefits of model-based vector search (for the business)

- **Better match quality** for company names, customer names, and addresses that are phrased differently.
- **Fewer missed or wrong matches** in critical flows (e.g., compliance, onboarding, reporting).
- **More consistent behavior** across regions and naming conventions.
- **Future flexibility** for RAG, recommendations, and other AI use cases that rely on semantic retrieval.

---

## 5. Challenges: implementation and cost

Adopting vector search is **not a small change**. It's important to be clear about what's involved so we can plan and, if needed, get support from leadership.

### 5.1 Implementation complexity

- **New stack components:** Vector store, embedding pipeline, and (optionally) reranking.
- **Data pipeline changes:** We need to generate and store embeddings for existing and new records, and keep them in sync with source data.
- **Integration work:** Our apps and APIs currently talk to Elasticsearch; we'll need to integrate with a vector store and possibly run hybrid (keyword + vector) queries.
- **Operational model:** Monitoring, indexing strategy, and failure handling for embedding and search services.
- **Testing and validation:** Defining "correct" matches, building test sets from cases like the two above, and measuring improvement over current Elasticsearch behavior.

### 5.2 Cost

- **Embedding model:** Either a hosted embedding API (per token/call) or self-hosted model (compute and maintenance).
- **Vector store:** Additional storage and compute (e.g., MongoDB Atlas Vector Search or another vector DB).
- **Engineering time:** Design, implementation, migration, and tuning over several sprints.

So the benefits are real, but the **implementation effort and cost are substantial**. That's why I'm raising it now: so we can align on scope and, if appropriate, involve your manager for prioritization and resource allocation.

---

## 6. Proposed direction: MongoDB + embedding model

- **Vector store:** Use **MongoDB** (e.g., **MongoDB Atlas Vector Search**) so we can keep vectors close to our existing document data and avoid a separate vector-only system if that fits our architecture.
- **Embedding model:** We need to choose a model that fits our data volume, latency, and accuracy needs. Options to evaluate:
  - **Voyage AI** (now part of MongoDB): Good fit if we're already on Atlas; supports automated embedding and is optimized for semantic search.
  - **Sentence-transformers** (e.g., `all-MiniLM-L6-v2`, `all-mpnet-base-v2`): Open source, can be self-hosted; good for entity and sentence similarity.
  - **Meta (Facebook) AI:**  
    - **FAISS** is a **similarity-search library** (how we search vectors at scale), not an embedding model. We can use FAISS as the search index on top of embeddings produced by another model.  
    - For **embeddings**, Meta has released models like **E5** (e.g., `intfloat/e5-base-v2`); these are strong for retrieval and can be run via Hugging Face or similar.
  - **Other options:** OpenAI/Cohere embeddings if we prefer a managed API and have budget for it.

Recommendation: **Short term** — pilot with **sentence-transformers** or **E5** (self-hosted or via existing ML infra) plus **MongoDB Atlas Vector Search** (or existing MongoDB with vector support). **Medium term** — evaluate Voyage AI / automated embedding if we standardize on Atlas, and consider **FAISS** (or Atlas's built-in index) for very large-scale similarity search.

---

## 7. Suggested talking points for the meeting

1. **Problem:** Our current Elasticsearch-based search is missing or misranking entities (e.g., CMS Energy vs Consumer Energy, Wells Fargo & Company vs Wells Fargo Bank). These are concrete, reproducible cases.
2. **Proposal:** Introduce model-based vector search for customer/entity data, using MongoDB as the vector store and a chosen embedding model.
3. **Benefits:** Better match quality, fewer errors, and a path to more advanced AI use cases.
4. **Reality check:** This is a multi-sprint effort with real implementation and cost implications; I've documented the main challenges so we can get the right visibility and support (including with your manager) for prioritization and resourcing.
5. **Next steps:** Align on a small pilot (e.g., one domain or one use case), choose embedding model and vector store, and define success metrics (e.g., improvement on the two example cases plus a small test set).

---

## 8. Next steps I can own

- Draft a **short pilot plan** (scope, data, metrics, timeline) if we agree to proceed.
- Put together a **one-page comparison** (Elasticsearch vs vector search) and cost/effort ranges for leadership.
- Prototype **one of the example cases** (e.g., Wells Fargo or CMS/Consumer Energy) with MongoDB + an embedding model and share results.

---

*Document prepared for manager discussion. Please adjust dates, names, and technical choices to match your environment and team.*
