import os
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st
from langchain_core.documents import Document
from merge import merge_faker_docs
os.environ["GROQ_API_KEY"] = st.secrets["Groq_API"]
os.environ["GOOGLE_API_KEY"]= st.secrets["Gemini_API"]
from langchain_core.documents import Document
from typing import List
def dict_to_documents(docs_dict: dict) -> List[Document]:
    documents = []
    for category, categories in docs_dict.items():
        if isinstance(categories, dict):
            for subcategory, functions in categories.items():
                if isinstance(functions, dict):
                    for func_name, details in functions.items():
                        if isinstance(details, dict):
                            content = f"""
Category: {category}/{subcategory}
Function: {func_name}
Description: {details.get('description', '')}
Examples: {', '.join(details.get('examples', []))}
"""
                            if 'patterns' in details:
                                content += f"Patterns: {', '.join(details['patterns'])}\n"
                            if 'parameters' in details:
                                content += f"Parameters: {str(details['parameters'])}\n"
                            doc = Document(
                                page_content=content,
                                metadata={
                                    "category": f"{category}/{subcategory}",
                                    "function": func_name,
                                    "type": "function_documentation"
                                }
                            )
                            documents.append(doc)
    return documents
all_docs = merge_faker_docs()
def create_vector_store():
    docs = dict_to_documents(all_docs)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    splits = text_splitter.split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return FAISS.from_documents(splits, embeddings)

def get_faker_function(user_input):
    vector_store = create_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    relevant_docs = retriever.invoke(user_input)
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Faker.js expert. Given the documentation context:

{docs}

Analyze the user's request and construct an appropriate Faker.js function call.
- Understand the intent of the user's request
- Use the documentation only as a reference for available functions and parameters
- Construct a new function call specific to the user's input
- Do not simply copy examples from the documentation
- Return only one function call without explanations
- Use proper syntax and parameters based on the function's requirements

For example, if someone asks for "generate a random adult's birthdate", you should understand:
1. This requires the birthdate function
2. They want an adult (over 18)
3. Therefore construct: faker.date.birthdate({{ mode: 'age', min: 18 }})

Think step by step about what the user is asking for, then construct the appropriate function call and dont return function only, provide the parameters too. e.g. """),
        ("user", "{input}")
    ])
    llm = ChatGroq(
        temperature=0.1,
        model_name="llama-3.3-70b-specdec",
    )
    chain = (
        {"docs": lambda x: "\n\n".join([d.page_content for d in x["relevant_docs"]]),
         "input": lambda x: x["user_input"]}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain.invoke({"relevant_docs": relevant_docs, "user_input": user_input})
st.title("Faker.js Function Finder with RAG")
user_input = st.text_input("Describe the data need:")
if user_input:
    with st.spinner("Searching Faker docs..."):
        try:
            result = get_faker_function(user_input)
            st.subheader("Recommended Function:")
            st.code(result, language="javascript")
        except Exception as e:
            st.error(f"Error: {str(e)}")
