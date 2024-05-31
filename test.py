import streamlit as st
import os
import pyodbc
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

# Load the GROQ and Google API keys
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Database configuration from environment variables
db_server = os.getenv('DB_SERVER')
db_name = os.getenv('DB_NAME')

# Initialize the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Connection string for SQL Server with Windows Authentication
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={db_server};'
    f'DATABASE={db_name};'
    f'Trusted_Connection=yes;'
)

def extract_sql_query(llm_response):
    # Find the index of 'SELECT' in the LLm response content
    select_index = llm_response.content.find('SELECT')
    if select_index != -1:
        # Find the index of ';' after the 'SELECT' keyword
        semicolon_index = llm_response.content.find(';', select_index)
        if semicolon_index != -1:
            # Extract the substring from 'SELECT' to ';' and return
            sql_query = llm_response.content[select_index:semicolon_index+1]
            return sql_query.strip()
    return None



def summarize_output(output, query):
    # Convert rows to a list of strings
    output_strings = [', '.join(map(str, row)) for row in rows]
    # Join the list of strings into a single string
    output_text = '\n'.join(output_strings)
    # Use the LangChain GROQ model to summarize the output
    prompt = f"Summarize the following output:\n'{output_text}'. based on the user query{query}"
    summary_response = llm.invoke(prompt)
    summary = summary_response.content
    return summary

# Streamlit app setup
st.title("AI SQL Agent")
st.subheader("By Ahmed Shafik")
user_query = st.text_input("Enter your query in natural language:")
return_table = st.checkbox("Return Table Data")
summarize_output_option  = st.checkbox("Summarize Output")

if st.button("Submit"):
    print("Button clicked")
    print(user_query)
    if user_query:
        # Generate the SQL query using LLM
        prompt = f"""Convert the following natural language query knowing you are using 
        Microsoft SQL Server and the table name is houses(id, property, location, price, dive) ex (4, 'Mountain cabin', 'Aspen, Colorado', 850000, 'Rustic'),
           into a SQL query and if it has limit replace it with top :\n'{user_query}' and return only the sql query"""
        llm_response = llm.invoke(prompt)
        sql_query = extract_sql_query(llm_response)

        if sql_query:
            # Display the generated SQL query
            st.write(f"Generated SQL Query: {sql_query}")

            # Basic validation of SQL query
            if not sql_query.lower().startswith("select"):
                st.write("The generated SQL query is not valid. Please refine your query.")
            else:
                try:
                    # Connect to the SQL Server database
                    conn = pyodbc.connect(conn_str)
                    cursor = conn.cursor()
                    st.write("Database connection established.")

                    # Execute the SQL query to select all rows from the houses table
                    cursor.execute(sql_query)
                    rows = cursor.fetchall()

                    # Check if rows are fetched
                    if not rows:
                        st.write("No data fetched.")
                    else:
                        # Print column names
                        columns = [column[0] for column in cursor.description]
                        st.write("Column names:", columns)
                        if return_table:
                            data = [columns] + rows
                            st.table(data)

                        if summarize_output_option:
                            # Summarize the output using LangChain GROQ
                            summarized_output = summarize_output(rows, user_query)
                            st.write("Summarized Output:", summarized_output)
                        

                except pyodbc.Error as err:
                    st.write(f"Error executing the query: {err}")
                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()
        else:
            st.write("Failed to extract SQL query from the LLM response.")
    else:
        st.write("Please enter a query.")
