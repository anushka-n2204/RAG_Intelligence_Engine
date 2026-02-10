import streamlit as st
import os
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

# 1. Advanced UI: Professional Branding & Animations
st.set_page_config(page_title="ORBIT AI", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono&display=swap');

    /* Background and global animation */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        animation: fadeInPage 2s ease-in-out;
    }
    @keyframes fadeInPage { from { opacity: 0; } to { opacity: 1; } }

    /* COMPLETELY REMOVE DEFAULT BLACK FOOTER, HEADER, AND MENU */
    header, footer, [data-testid="stHeader"], #MainMenu {
        visibility: hidden !important;
        height: 0px !important;
        display: none !important;
    }

    /* Professional layout spacing */
    .block-container { padding-top: 2rem; padding-bottom: 7rem; max-width: 800px; }

    /* Custom relevant footer */
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background: rgba(15, 12, 41, 0.9); backdrop-filter: blur(15px);
        color: rgba(255, 255, 255, 0.5); text-align: center;
        padding: 15px 0; font-size: 0.75rem; font-family: 'JetBrains Mono';
        border-top: 1px solid rgba(255, 255, 255, 0.15); z-index: 999;
    }

    /* Style for chat bubbles to match the glass look */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 18px !important;
        animation: slideUpFade 0.7s ease-out;
    }

    /* Title Styling */
    .main-title {
        background: linear-gradient(to right, #00d2ff, #9d50bb);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800; font-size: 3.5rem; margin-bottom: 0.2rem;
        letter-spacing: -1.5px;
    }
    </style>
    
    <div class="custom-footer">
        🔒 ORBIT AI runs locally. Your documents never leave your device.
    </div>
    """, unsafe_allow_html=True)

# 2. RAG Logic (Updated for validation, UI remains intact)
def auto_process():
    if st.session_state.uploader:
        with st.status("🧠 Synchronizing Knowledge Modules...", expanded=True) as status:
            all_docs = []
            file_meta = []
            
            # Supported formats
            valid_extensions = (".pdf", ".docx", ".csv")
            
            for file in st.session_state.uploader:
                # Validation check
                if not file.name.lower().endswith(valid_extensions):
                    st.error(f"⚠️ '{file.name}' is an invalid format. Only PDF, DOCX, and CSV are supported.")
                    continue  # Skip invalid file
                
                temp_path = os.path.join(os.getcwd(), file.name)
                with open(temp_path, "wb") as f: f.write(file.getbuffer())
                
                if file.name.endswith(".pdf"): loader = PyPDFLoader(temp_path)
                elif file.name.endswith(".docx"): loader = Docx2txtLoader(temp_path)
                elif file.name.endswith(".csv"): loader = CSVLoader(temp_path)
                
                data = loader.load()
                all_docs.extend(data)
                file_meta.append({"name": file.name, "size": len(data)})
                os.remove(temp_path)

            if all_docs:
                splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
                chunks = splitter.split_documents(all_docs)
                vector_db = Chroma.from_documents(documents=chunks, embedding=OllamaEmbeddings(model="llama3.2:1b"))
                
                llm = ChatOllama(model="llama3.2:1b")
                prompt = ChatPromptTemplate.from_template("Use the following context to answer: {context}\n\nQuestion: {input}")
                chain = create_stuff_documents_chain(llm, prompt)
                st.session_state.rag_chain = create_retrieval_chain(vector_db.as_retriever(), chain)
                
                status.update(label="🚀 Intelligence Layer Ready!", state="complete")
                st.session_state.ready = True
                st.session_state.file_list = file_meta
            else:
                # Feedback if zero valid files were processed
                status.update(label="❌ No valid modules detected.", state="error")

# 3. UI Content
st.markdown("<h1 class='main-title'>ORBIT AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#00bcff; font-family:JetBrains Mono; font-size:0.85rem; margin-bottom: 2rem;'>> Private AI for your documents </p>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
if "ready" not in st.session_state: st.session_state.ready = False

st.file_uploader(
    "Upload", type=["pdf", "docx", "csv"], 
    accept_multiple_files=True, 
    key="uploader", 
    on_change=auto_process, 
    label_visibility="collapsed"
)

if st.session_state.ready:
    st.markdown("### 📊 Indexed Intelligence")
    for f in st.session_state.file_list:
        st.caption(f"✓ {f['name']} — Indexed for search")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.button("Executive Summary", use_container_width=True)
    with col2: st.button("Extract Actions", use_container_width=True)
    with col3: st.button("Identify Risks", use_container_width=True)
else:
    st.info("🚀 Upload a document to activate your private AI workspace.")

st.divider()

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

placeholder = "Enter your inquiry..." if st.session_state.ready else "🚀 Upload a document to activate your private AI workspace."
if user_input := st.chat_input(placeholder, disabled=not st.session_state.ready):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"): st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Synthesizing answer..."):
            res = st.session_state.rag_chain.invoke({"input": user_input})
            st.markdown(res["answer"])
            st.session_state.messages.append({"role": "assistant", "content": res["answer"]})
