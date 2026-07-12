# RAG Intelligence Engine

This is a professional-grade, **privacy-first Retrieval-Augmented Generation (RAG)** platform. It lets you build a private knowledge base by uploading documents (PDF, DOCX, CSV) and chatting with them using local Large Language Models.

Built for low latency and high privacy, it runs **entirely on local hardware** — no data ever leaves the host machine.

---

## ✨ Key Features

- 📂 **Multi-Format Ingestion** — native support for `.pdf`, `.docx`, and `.csv` file formats.
- 🔒 **100% Local Processing** — leverages **Ollama** and **Llama 3.2 1B** to ensure complete data sovereignty and privacy.
- 🪟 **Glassmorphism 2.0 UI** — a sleek, modern interface featuring frosted-glass components, CSS animations, and a focus-driven layout.
- 🧠 **Dynamic Knowledge Mapping** — automatically chunks and indexes data into a **ChromaDB** vector store for high-accuracy retrieval.
- ☁️ **Zero-Cloud Dependency** — no API keys or internet connectivity required once the models are downloaded.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| 🎨 **Frontend** | Streamlit (Custom CSS & Glassmorphism) |
| 🔗 **Orchestration** | LangChain & LangChain-Classic |
| ⚙️ **LLM Engine** | Ollama |
| 🤖 **Model** | Llama 3.2 1B |
| 🗄️ **Vector DB** | ChromaDB |
| 🧬 **Embeddings** | Ollama Local Embeddings |

---

## 🚀 Installation & Setup

### 1️⃣ Prerequisites

- 🐍 **Python 3.9 – 3.11** installed.
- 🦙 **Ollama** installed on your system.
  - Download the model:
    ```bash
    ollama pull llama3.2:1b
    ```

### 2️⃣ Clone and Install

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/anushka-n2204/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
```

### 3️⃣ Start Ollama

Make sure the Ollama server is running in the background:

```bash
ollama serve
```

### 4️⃣ Run the App

Launch the Streamlit app:

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 💬 Usage

1. 📤 **Upload** one or more `.pdf`, `.docx`, or `.csv` files through the sidebar.
2. 🧩 The app **chunks and embeds** your documents locally, storing vectors in ChromaDB.
3. ❓ **Ask questions** about your documents in the chat interface.
4. 📚 It **retrieves the most relevant chunks** and generates a grounded answer using Llama 3.2 1B — all on-device.

---

## 📁 Project Structure

```
RAG_Intelligence_Engine/
├── app.py                # Streamlit entry point / UI
├── requirements.txt      # Python dependencies
├── ingestion/             # Document loaders & chunking (PDF, DOCX, CSV)
├── vectorstore/           # ChromaDB setup & retrieval logic
├── chains/                 # LangChain RAG pipeline
└── README.md
```

*(Adjust the tree above to match the repo's actual folder layout.)*

---

## 🔐 Privacy by Design

- 🚫 No cloud API calls — all inference and embedding happens locally via Ollama.
- 🚫 No telemetry, no external logging.
- ✅ Your documents and conversations never leave your machine.

---

## 📝 Notes

Built as a hands-on exploration of local, privacy-preserving RAG pipelines — combining document ingestion, chunking, vector retrieval with ChromaDB, and on-device LLM inference into a single production-styled Streamlit app.
