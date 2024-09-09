# ConvoMate
ConvoMate: Your AI English Coach
An AI-Powered English Mentor for Engaging and Effective Language Learning

## Description
The ConvoMate is a web-based conversational application designed to help users improve their English language fluency through interactive chat sessions. The application uses a combination of natural language processing, language models, and conversational strategies to engage users in meaningful dialogues and provide feedback to enhance their speaking and comprehension skills.

The core features of the English Fluency Mentor include:

 1. **Conversational AI Assistant**: The assistant, named Emma, acts as a friendly and experienced English language instructor. She initiates conversations, suggests topics, engages in natural dialogue, provides feedback, and asks follow-up questions to guide users through the learning process.
 2. **Grammar and Spelling Correction**: The assistant monitors the user's input and gently corrects any grammar or spelling mistakes, helping users improve their overall language proficiency.
 3. **Personalized Feedback**: Based on the user's responses and performance, the assistant provides personalized feedback, praise, and encouragement to foster a supportive learning environment.
 4. **Conversation History**: The application keeps track of the conversation history, allowing users to revisit and review past discussions, as well as enabling the assistant to maintain context and continuity throughout the learning session.

## Requirements:
 * Python 3.8 or later
 * FastAPI
 * LangChain
 * Llama-3
 * HTML, CSS, JavaScript (for the frontend)


## Steps To Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create and activate a virtual environment:**

    ```bash
    conda activate -n <env_name> python=3.11 -y
    conda activate <env_name>
    ```
    Repalce the <env_name> with the name of your environment 

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your Replicate API token

    ```env
    #REPLICATE
    REPLICATE_API_TOKEN=your_replicate_api_token

    ```

5. **Running the Application:**

    Launch your terminal and execute the following command:

    ```bash
    python main.py
    ```

## Future Works
Some of the planned future improvements include:

 - Voice-Powered Chatbot: Integrating speech recognition and text-to-speech technologies to enable a voice-based conversational experience, allowing users to practice their English speaking skills more naturally.
 - Adaptive Learning Algorithms: Developing more advanced natural language processing and machine learning algorithms to better understand the user's proficiency level and tailor the conversation and feedback accordingly..
 - Mobile-Friendly Deployment: Optimizing the application for mobile devices, making it accessible and convenient for users to practice their English skills on the go.
 - User Analytics and Reporting: Implementing robust user analytics and reporting features to track individual progress, identify areas for improvement, and provide detailed insights to both users and administrators.