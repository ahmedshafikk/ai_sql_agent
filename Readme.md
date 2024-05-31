# AI SQL Agent

## Overview

The **AI SQL Agent** is an intelligent tool designed to translate natural language into SQL queries, connect to a database using provided credentials, fetch the data, and summarize the output to match conversational requirements. This project utilizes Groq with Llama3 in the backend and connects to a Microsoft SQL Server running locally. It serves as a basic framework with the potential to expand for more complex databases. Feel free to clone the repository and customize it for your use case.

## Features

- **Natural Language Processing (NLP)**: Utilizes llm to convert natural language queries into SQL commands.
- **Dynamic Query Generation**: Generates SQL queries based on user input, eliminating the need for manual query construction.
- **Database Interaction**: Connects to specified SQL databases, executes generated SQL queries, and retrieves relevant data.
- **Query Summarization**: Summarizes the retrieved data using llm, providing readable and conversational results.
- **Interactive User Interface**: Features a user-friendly interface for entering natural language queries, viewing SQL queries, and accessing query results.

## Getting Started

To use the AI SQL Agent, follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your_username/ai-sql-agent.git
   ```

2. **Install Dependencies**: Install the required Python dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**: Create a `.env` file in the project directory and add your API keys and database credentials:
   ```text
   GROQ_API_KEY="your_groq_api_key"
   GOOGLE_API_KEY="your_google_api_key"
   DB_SERVER="your_db_server"
   DB_NAME="your_db_name"
   ```

4. **Run the Application**: Start the application by running the following command:
   ```bash
   streamlit run app.py
   ```

5. **Enter Queries**: Use the application's user interface to enter natural language queries and explore the generated SQL queries and results.

## Using the Application

1. **Launch the App**: Open your browser and navigate to the local Streamlit server (usually http://localhost:xxxx).

2. **Enter a Query**: Type your natural language query into the text input field and click "Submit".

3. **View SQL Query**: The application will display the generated SQL query.

4. **Fetch Data**: The application will execute the SQL query on the database and display the fetched data in a table format.

5. **Summarize Data**: Optionally, click the "Summarize Output" button to get a human-readable summary of the retrieved data.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to fork the project, make improvements, and contribute back! If you encounter any issues, please open an issue on the GitHub repository.
=======
# AI SQL Agent

## Overview

The **AI SQL Agent** is an intelligent tool designed to translate natural language into SQL queries, connect to a database using provided credentials, fetch the data, and summarize the output to match conversational requirements. This project utilizes Groq with Llama3 in the backend and connects to a Microsoft SQL Server running locally. It serves as a basic framework with the potential to expand for more complex databases. Feel free to clone the repository and customize it for your use case.

## Features

- **Natural Language Processing (NLP)**: Utilizes llm to convert natural language queries into SQL commands.
- **Dynamic Query Generation**: Generates SQL queries based on user input, eliminating the need for manual query construction.
- **Database Interaction**: Connects to specified SQL databases, executes generated SQL queries, and retrieves relevant data.
- **Query Summarization**: Summarizes the retrieved data using llm, providing readable and conversational results.
- **Interactive User Interface**: Features a user-friendly interface for entering natural language queries, viewing SQL queries, and accessing query results.

## Getting Started

To use the AI SQL Agent, follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your_username/ai-sql-agent.git
   ```

2. **Install Dependencies**: Install the required Python dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**: Create a `.env` file in the project directory and add your API keys and database credentials:
   ```text
   GROQ_API_KEY="your_groq_api_key"
   GOOGLE_API_KEY="your_google_api_key"
   DB_SERVER="your_db_server"
   DB_NAME="your_db_name"
   ```

4. **Run the Application**: Start the application by running the following command:
   ```bash
   streamlit run app.py
   ```

5. **Enter Queries**: Use the application's user interface to enter natural language queries and explore the generated SQL queries and results.

## Using the Application

1. **Launch the App**: Open your browser and navigate to the local Streamlit server (usually http://localhost:xxxx).

2. **Enter a Query**: Type your natural language query into the text input field and click "Submit".

3. **View SQL Query**: The application will display the generated SQL query.

4. **Fetch Data**: The application will execute the SQL query on the database and display the fetched data in a table format.

5. **Summarize Data**: Optionally, click the "Summarize Output" button to get a human-readable summary of the retrieved data.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to fork the project, make improvements, and contribute back! If you encounter any issues, please open an issue on the GitHub repository.
