# 🌌 ORBIT AI: Local RAG Intelligence Engine

ORBIT AI is a professional-grade, privacy-first Retrieval-Augmented Generation (RAG) platform. It allows users to create a private knowledge base by uploading documents (PDF, DOCX, CSV) and chatting with them using local Large Language Models (LLMs). 

Built specifically for low-latency and high privacy, ORBIT AI runs entirely on local hardware, ensuring no data ever leaves the host machine.



---

## ✨ Key Features

- **Multi-Format Ingestion**: Native support for `.pdf`, `.docx`, and `.csv` file formats.
- **100% Local Processing**: Leverages **Ollama** and **Llama 3.2 1B** to ensure complete data sovereignty and privacy.
- **Glassmorphism 2.0 UI**: A sleek, modern interface featuring frosted-glass components, CSS animations, and a focus-driven layout.
- **Dynamic Knowledge Mapping**: Automatically chunks and indexes data into a **ChromaDB** vector store for high-accuracy retrieval.
- **Zero-Cloud Dependency**: Does not require API keys or internet connectivity once the models are downloaded.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit (Custom CSS & Glassmorphism) |
| **Orchestration** | LangChain & LangChain-Classic |
| **LLM Engine** | Ollama |
| **Model** | Llama 3.2 1B (Optimized for i3/Low-Power CPUs) |
| **Vector DB** | ChromaDB |
| **Embeddings** | Ollama Local Embeddings |

---

## 🚀 Installation & Setup

### 1. Prerequisites
- **Python 3.9 - 3.11** installed.
- **Ollama** installed on your system.
  - Download the model: `ollama pull llama3.2:1b`

### 2. Clone and Install
Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
