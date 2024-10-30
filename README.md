# EstateSmart 🏡

### Empowering Real Estate Agents with Instant Property Insights

---

## Overview
EstateSmart is an AI-powered chatbot designed to assist real estate agents by providing instant access to crucial property and client information. Built with the goal of enhancing efficiency and delivering faster, more informed responses to clients, EstateSmart leverages call transcripts to enable agents to quickly answer client queries about properties, amenities, and client history, directly from a user-friendly interface.

With EstateSmart, agents can ask questions like:
- "What amenities are available in Property X?"
- "Can you give me details about the client’s history with Property Y?"
- "What is the pricing and neighborhood information for Property Z?"

This real-time Q&A capability empowers agents with the data they need, making client interactions smoother, more accurate, and more satisfying.

---

## Infrastructure and Tools Used

### 1. **Data and Storage:**
   - **Data Source:** EstateSmart uses call transcripts between clients and agents as the primary data source. This data is stored in a structured format on **Databricks** for efficient management and processing.
   - **Data Pipeline:** Databricks facilitates ETL (Extract, Transform, Load) processes, allowing the team to clean, annotate, and organize transcripts to ensure relevant, real-time information is available for the chatbot.

### 2. **Machine Learning & Model Serving:**
   - **Model Deployment:** The Q&A model was developed and deployed on **Databricks**. This platform was chosen for its robust environment that supports data preparation, model training, and deployment under one unified platform.
   - **Serving Endpoint:** EstateSmart’s model is deployed via **Databricks’ Serving Endpoint**, ensuring that each query from the agent receives a fast, accurate response in real time.

### 3. **Frontend - User Interface:**
   - **Streamlit Application:** The frontend is built using **Streamlit**, providing an intuitive and user-friendly UI where agents can interact with the chatbot. The UI is designed to be simple and responsive, allowing agents to type in questions and instantly view the responses.

---

## Data Pipeline and Processing

EstateSmart’s data pipeline is structured to maximize the accuracy and speed of response:
1. **Data Ingestion:** Call transcripts are ingested into Databricks from various sources and standardized to ensure consistency.
2. **Data Cleaning and Annotation:** Text is processed to remove any irrelevant information, and labels are added for property details, amenities, and client history.
3. **Deployment:** The trained model is deployed on Databricks’ Serving Endpoint, where it interacts with the Streamlit frontend to answer queries in real-time.

---

## Features

- **Instant Property and Client Information**: Quickly retrieve property specifications, amenities, and client history to enhance the agent’s interaction with clients.
- **Efficient Data Handling**: With Databricks as the backend, EstateSmart efficiently handles large volumes of data, ensuring accuracy and speed in responses.
- **User-Friendly Interface**: The Streamlit-based UI is designed for agents, allowing easy, question-based interactions without the need to sift through multiple sources.

---

## Getting Started

### Prerequisites
To run EstateSmart, you'll need:
- Python 3.8+
- Access to a Databricks account (for data and model deployment)
- Streamlit (for UI)

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/estatesmart.git
   cd estatesmart
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Databricks Access:**
   Set up a Databricks API token and add it to your environment for model access and data handling.

4. **Run the Application:**
   Start the Streamlit app with the following command:
   ```bash
   streamlit run app.py
   ```

---

## Conclusion
EstateSmart is designed to redefine how real estate agents interact with clients by putting the data they need right at their fingertips. By using Databricks for seamless data processing and Streamlit for an interactive UI, EstateSmart brings together the best of AI and real estate, setting a new standard for efficiency and customer engagement in the industry.

---

### Future Improvements
We plan to add more features, including:
- Support for multiple languages.
- Enhanced analytics to track popular queries and agent interactions.
- Improved natural language understanding to handle more complex queries.

---

**Contributors:**    
Galina - Data Scientist
Guzal - Data Scientist
Padmaj - Data Scientist

**License:** This project is licensed under the MIT License.

---

