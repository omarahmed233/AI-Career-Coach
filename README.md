# AI-Career-Coach

# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        | Omar Ahmed Abd El-Kader              |
| Project Name     | AI Career Coach                      |
| GitHub Username  | omarahmed233                         |
| Internship Batch | August–October 2026                  |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en) |

---

# 📖 Project Overview

building an AI career coach that extracts skills from a CV, retrieves skills for a target role, and compares them to identify potential skill gaps.

---

# ✨ Features

The project extracts skills from a CV, retrieves skills for a target role, and compares them to identify potential skill gaps.

---

# 🛠️ Technologies Used

- Python for the application logic
- FastAPI for the API
- LangChain and Pydantic for prompts and structured outputs
- Groq API for LLM-powered skill extraction and comparison
- Sentence Transformers and FAISS for retrieving target-role skills
- Pyngrok for exposing the API during development

---

# ⚙️ Installation

The project runs in a Kaggle notebook:
1. Add the target-role rules file as a Kaggle dataset.
2. Add GROQ_API_KEY and NGROK_TOKEN as Kaggle Secrets.
3. Install dependencies:
   !pip install -q langchain-groq sentence-transformers faiss-cpu fastapi uvicorn pyngrok
4. Run the notebook cells in order to load the models, build the RAG index, and start the FastAPI server.
5. Copy the printed ngrok URL and send a POST request to /generate with full_text and target_role.
The API returns the CV skills, target-role skills, and identified skill gaps.

---

# 🚀 Usage

The user uploads or provides their CV, selects or enters a target role, and submits the request. The project returns the skills found in the CV, the target role’s skills, and potential gaps to help guide their career development.

---

# 📸 Demo

Add screenshots, GIFs, or a demo video.

---

# 📈 Results

I gained hands-on experience integrating external APIs, RAG-based retrieval, and LangChain with Pydantic structured outputs in one workflow. I learned how to connect CV skill extraction with target-role comparison and return structured skill-gap results.

---

# 🔮 Future Improvements

- Improve skill extraction and matching accuracy with a manually reviewed evaluation set.
- Use job descriptions to distinguish required skills from conditional role skills.
- Add evidence and source sections so users can see why each skill was matched or marked as needed.
- Expand the role database and improve retrieval so it returns the correct profile consistently.
- Add secure deployment, request validation, and clearer error handling for production use.

---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
