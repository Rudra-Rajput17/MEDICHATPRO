"# MEDICHATPRO" 
# 🏥 **MediChat Pro — Medical Document Assistant**

> *"Empowering healthcare professionals and patients to understand medical reports through AI."*

---

## 🌐 **Overview**

**MediChat Pro** is an **AI-powered medical document assistant** that allows users to **upload PDF medical reports** (like prescriptions, lab results, discharge summaries, etc.) and **interact with them conversationally**.

It uses **LangChain**, **FAISS**, and **Euri AI models** to retrieve relevant information from the uploaded PDFs and answer medical queries in context — just like chatting with your own healthcare analyst.

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be applied to real-world healthcare data safely and effectively.

---

## ⚡ **Key Features**

✅ Upload and process multiple **medical PDFs**
✅ AI-powered **chat interface** using **Streamlit**
✅ **Context-aware answers** from your own medical reports
✅ **FAISS vector store** for fast and accurate document retrieval
✅ Integrated with **Euri AI API** via **LangChain**
✅ **Clean, responsive, and professional UI**

---

## 🧠 **Tech Stack**

| Category            | Technology                                                                   |
| ------------------- | ---------------------------------------------------------------------------- |
| **Frontend**        | Streamlit                                                                    |
| **Backend / Logic** | Python                                                                       |
| **Vector Database** | FAISS (Facebook AI Similarity Search)                                        |
| **AI / LLM**        | Euri AI (via LangChain)                                                      |
| **Libraries**       | `langchain`, `langchain_community`, `sentence-transformers`, `pypdf`, `fpdf` |
| **Architecture**    | Retrieval-Augmented Generation (RAG)                                         |

---

## 🧬 **Folder Structure**

```
MEDICHATPRO/
│
├── app/
│   ├── ui.py                    # Handles PDF uploads & Streamlit UI
│   ├── pdf_utils.py             # Extracts text from PDFs
│   ├── vectorstore_utils.py     # Creates and queries FAISS index
│   ├── chat_utils.py            # Handles chat model setup and responses
│   └── config.py                # Contains EURI_API_KEY and configurations
│
├── main.py                      # Streamlit entry point (main app)
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ **Installation & Setup**

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/yourusername/MediChatPro.git
cd MediChatPro
```

2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Set Up API Key**
Create a file named `.env` or directly in `config.py`:

```python
EURI_API_KEY = "your_euriai_api_key_here"
```

4️⃣ **Run the App**

```bash
streamlit run main.py
```

---

## 🧬 **How It Works**

1. **Upload PDFs** of medical reports (lab results, prescriptions, etc.)
2. The app extracts **text** using `PyPDF` and splits it into chunks.
3. These chunks are embedded using `sentence-transformers` and stored in a **FAISS vector index**.
4. When you ask a question, the system retrieves the **most relevant document chunks**.
5. The context + question is passed to the **Euri AI LLM** via LangChain.
6. You receive a **contextual, medically-informed answer** in real time.

---

## 💬 **Example Chat**

**User:** *“What does my blood test say about hemoglobin levels?”*
**MediChat Pro:**

> “According to your uploaded report, your hemoglobin level is 11.5 g/dL, which is slightly below the normal range. You may want to consult your physician for further evaluation.”

---

## 📞 **Requirements**

```
streamlit
fpdf
pypdf
faiss-cpu
langchain
euriai
langchain_community
sentence-transformers
```

---

## 🧥 **Ethical Disclaimer**

> MediChat Pro is designed **for educational and informational purposes only**.
> It **does not replace professional medical advice**.
> Always consult a certified healthcare provider for diagnosis or treatment decisions.

---

## 🌟 **Future Improvements**

* 🕡️ Voice-based medical queries
* 🧩 Chat history and session memory
* 🌍 Multilingual medical support
* 📊 Dashboard for report summarization

---

## 👤 **About the Developer**

**👨‍💻 Rudra Rajput**
🚀 *Aspiring Data Scientist | AI & GenAI Developer | Healthcare Tech Enthusiast*
🔗 [LinkedIn](https://www.linkedin.com/in/rudra-pratap-singh-59122a24b)

---

## ⭐ **Support the Project**

If you found **MediChat Pro** inspiring, give it a ⭐ on GitHub and share it with others who love **AI + Healthcare Innovation**!
