# chatbot-thelmaAI
ABSTRACT
This project presents the design and implementation of an AI-powered chatbot system aimed at improving student access to academic information and administrative support at Igbinedion University. The system leverages Natural Language Processing (NLP) using the SentenceTransformer model all-MiniLM-L6-v2 to understand and respond to student queries in real time. By integrating a Flask-based backend, a user-friendly web interface, and a xampp database, the chatbot efficiently handles inquiries related to course registration, tuition, exam schedules, and university policies. The system reduces administrative workload, enhances student engagement, and provides 24/7 support. Through the application of object-oriented design principles and lightweight AI models, the solution is cost-effective, scalable, and tailored to the infrastructure constraints of developing academic environments. The project demonstrates how AI technologies can transform student services in higher education institutions.
3.3.3  IMPLEMENTATION ARCHITECHTURE
The implementation architecture of the proposed AI-powered chatbot system consists of four main components: the user interface, backend server, AI model layer, and database. Students interact with the system by entering their queries through the interface. These inputs are processed by the backend, which hosts the SentenceTransformer model all-MiniLM-L6-v2 to understand and generate relevant responses. The backend also communicates with xampp database to retrieve or update necessary information, such as academic records or event data. The system ensures seamless communication between the AI engine and database, providing accurate, real-time responses to users.






Figure 3.2: Diagram of the Implementation architecture of the proposed system

3.3.4 SYSTEM ARCHITECHTURE
The proposed AI-based chatbot system is designed to streamline how students access academic information by using Natural Language Processing (NLP) to understand and respond to their queries in real time. The architecture of this system consists of several interconnected components that work together to ensure accurate, fast, and user-friendly interaction.The process begins when the system is activated, marked by the “Start” point in the architecture. A student then enters a query through the user interface. This input could be a question regarding course registration, fee payment, class schedules, or examination dates. Simultaneously, the administrator (admin) provides the system with updated academic information, such as event schedules, fee structures, and course details. These inputs from the admin are stored securely in the system's database.
Once a user query is received, it moves to the Query Processing stage. At this point, the system begins analyzing the student's question. To accurately interpret the meaning behind the words, the chatbot uses a Sentence Transformer, an NLP tool that converts the student’s text into a machine-understandable format. This transformation helps the system identify the intent of the question.
Following this, the system searches the Knowledge Base, which is built using the admin’s inputs and previously gathered information. The chatbot compares the transformed query with the contents of the knowledge base to find the most relevant answer.Next, the system checks if the Query is Understood. This is a crucial decision point. If the system determines that it fully understands the question, it proceeds to Generate a Response using the most relevant data. This response is then sent back to the student in a conversational format. If the system does not understand the query, it may prompt the user for clarification or rephrasing.
Finally, the process concludes at the End stage, where the student has received a meaningful and helpful response to their academic inquiry.























                                                                                                                                                             















Figure 3.3: Flowchart of the system architecture .
