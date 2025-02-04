import os
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st
from langchain_core.documents import Document
os.environ["GROQ_API_KEY"] = st.secrets["Groq_API"]
os.environ["GOOGLE_API_KEY"]= st.secrets["Gemini_API"]

def load_faker_docs():
    docs = {
  "person": {
    "firstName": {
      "description": "Generate a random first name",
      "patterns": [
        "first name", "given name", "forename",
        "generate first name", "random first name"
      ],
      "examples": [
        "first name",
        "female first name",
        "male first name"
      ],
      "parameters": {
        "sex": "optional - 'female' | 'male'"
      }
    },
    "lastName": {
      "description": "Generate a random last name",
      "patterns": [
        "last name", "surname", "family name",
        "generate last name", "random last name"
      ],
      "examples": [
        "last name",
        "surname"
      ]
    },
    "middleName": {
      "description": "Generate a random middle name",
      "patterns": [
        "middle name", "generate middle name",
        "random middle name"
      ],
      "examples": [
        "middle name",
        "female middle name"
      ],
      "parameters": {
        "sex": "optional - 'female' | 'male'"
      }
    },
    "fullName": {
      "description": "Generate a full name with optional prefix/suffix",
      "patterns": [
        "full name", "complete name", "entire name",
        "generate full name", "random person name"
      ],
      "examples": [
        "full name",
        "female full name with prefix",
        "male full name with suffix"
      ],
      "parameters": {
        "sex": "optional - 'female' | 'male'",
        "includeMiddleName": "optional - boolean",
        "prefix": "optional - boolean",
        "suffix": "optional - boolean"
      }
    },
    "gender": {
      "description": "Generate a random gender",
      "patterns": [
        "gender", "sex", "generate gender",
        "random gender"
      ],
      "examples": [
        "gender",
        "binary gender"
      ]
    },
    "jobTitle": {
      "description": "Generate a random job title",
      "patterns": [
        "job title", "occupation", "profession",
        "generate job title", "random job"
      ],
      "examples": [
        "job title",
        "profession"
      ]
    }
  },

  "date": {
    "birthdate": {
      "description": "Generate a random birthdate with age-based options",
      "patterns": [
        "birth date", "date of birth", "birthday",
        "dob", "generate birthday"
      ],
      "examples": [
        "date of birth over 18",
        "birthdate between 20 and 30",
        "birthday under 65"
      ],
      "parameters": {
        "mode": "optional - 'age' | 'year'",
        "min": "optional - number (minimum age)",
        "max": "optional - number (maximum age)",
        "year": "optional - number (specific year)"
      }
    },
    "future": {
      "description": "Generate a date in the future",
      "patterns": [
        "future date", "upcoming date", "date in future",
        "generate future date"
      ],
      "examples": [
        "future date",
        "date 5 years from now"
      ],
      "parameters": {
        "years": "optional - number",
        "refDate": "optional - Date object"
      }
    },
    "past": {
      "description": "Generate a date in the past",
      "patterns": [
        "past date", "previous date", "date in past",
        "generate past date"
      ],
      "examples": [
        "past date",
        "date 3 years ago"
      ],
      "parameters": {
        "years": "optional - number",
        "refDate": "optional - Date object"
      }
    }
  },

  "internet": {
    "email": {
      "description": "Generate an email address",
      "patterns": [
        "email", "email address", "mail",
        "generate email", "random email"
      ],
      "examples": [
        "email address",
        "email with gmail",
        "business email"
      ],
      "parameters": {
        "firstName": "optional - string",
        "lastName": "optional - string",
        "provider": "optional - string"
      }
    },
    "userName": {
      "description": "Generate a username",
      "patterns": [
        "username", "user name", "login name",
        "generate username"
      ],
      "examples": [
        "username",
        "login name"
      ],
      "parameters": {
        "firstName": "optional - string",
        "lastName": "optional - string"
      }
    },
    "password": {
      "description": "Generate a password",
      "patterns": [
        "password", "generate password", "secure password",
        "random password"
      ],
      "examples": [
        "password",
        "password with length 12",
        "strong password"
      ],
      "parameters": {
        "length": "optional - number",
        "memorable": "optional - boolean",
        "pattern": "optional - regex pattern"
      }
    }
  },

  "finance": {
    "creditCardNumber": {
      "description": "Generate a credit card number",
      "patterns": [
        "credit card", "credit card number", "cc number",
        "generate credit card"
      ],
      "examples": [
        "credit card number",
        "visa card number",
        "mastercard number"
      ],
      "parameters": {
        "issuer": "optional - 'visa' | 'mastercard' | 'amex'"
      }
    },
    "bitcoinAddress": {
      "description": "Generate a Bitcoin address",
      "patterns": [
        "bitcoin address", "btc address",
        "generate bitcoin address"
      ],
      "examples": [
        "bitcoin address",
        "btc wallet"
      ]
    },
    "amount": {
      "description": "Generate a random amount of money",
      "patterns": [
        "amount", "money amount", "payment amount",
        "generate amount"
      ],
      "examples": [
        "amount between 100 and 1000",
        "payment amount in USD"
      ],
      "parameters": {
        "min": "optional - number",
        "max": "optional - number",
        "dec": "optional - number (decimals)",
        "symbol": "optional - string",
        "autoFormat": "optional - boolean"
      }
    }
  }
}

    documents = []
    for category, functions in docs.items():
        for func_name, details in functions.items():
            content = f"""
Category: {category}
Function: {func_name}
Description: {details['description']}
Patterns: {', '.join(details['patterns'])}
Examples: {', '.join(details['examples'])}
Parameters: {str(details.get('parameters', 'None'))}"""

            documents.append(Document(
                page_content=content,
                metadata={
                    "category": category,
                    "function": func_name,
                    "parameters": details.get('parameters', {})
                }
            ))
    return documents

def create_vector_store():
    docs = load_faker_docs()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
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

Convert the user's request into the correct Faker.js function call.
- Use proper syntax and parameters
- Return only the function call, no explanations

Examples:
Input: date of birth over 18 → faker.date.birthdate({{ mode: 'age', min: 18, max: 65 }})
Input: realistic 9-digit number → faker.helpers.sbn9()"""),
        ("user", "{input}")
    ])

    llm = ChatGroq(
        temperature=0.1,
        model_name="mixtral-8x7b-32768",
    )

    chain = (
        {"docs": lambda x: "\n\n".join([d.page_content for d in x["relevant_docs"]]),
         "input": lambda x: x["user_input"]}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke({"relevant_docs": relevant_docs, "user_input": user_input})

# Streamlit UI
st.title("Faker.js Function Finder with RAG")
user_input = st.text_input("Describe the data need:", "date of birth over 18")

if user_input:
    with st.spinner("Searching Faker docs..."):
        try:
            result = get_faker_function(user_input)
            st.subheader("Recommended Function:")
            st.code(result, language="javascript")

            st.divider()
            st.caption("Top matching documentation:")
            vector_store = create_vector_store()
            retrieved_docs = vector_store.as_retriever().invoke(user_input)

            for doc in retrieved_docs[:2]:
                st.text(doc.page_content)
                st.write("---")

        except Exception as e:
            st.error(f"Error: {str(e)}")
