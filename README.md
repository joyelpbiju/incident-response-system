# **Incident Response System**

This project was developed by [Joshua Porunnedath Biju](https://github.com/JOSHUAPBIJU) and [Joyel Porunnedath Biju](https://github.com/joyelpbiju).

![License](https://img.shields.io/badge/license-MIT-green) ![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen) ![Status](https://img.shields.io/badge/status-completed-blue)

## **Project Overview**

The **Incident Response System** was developed as part of the **Interactive Systems** course to analyze how different user interface designs impact **cybersecurity incident reporting**. The project consists of **two UI prototypes**:

- **Prototype A:** A multi-step **form-based** interface requiring manual input.
- **Prototype B:** An **interactive chatbot** guiding users through predefined responses.

The goal was to **evaluate usability, completion time, and error rates** between the two approaches. The study was conducted in a **controlled environment**, where **users were required to provide responses that matched predefined answers** for valid comparisons.

**This project is fully developed and no further updates are planned.**

## **Features**

- **Prototype A (Form-Based UI):**
  - Multi-step structured input collection.
  - Progress bar for tracking user progress.
  - Traditional form layout.

- **Prototype B (Chatbot UI):**
  - Conversational-style interaction.
  - Dynamic responses based on user inputs.
  - Predefined answer selection for structured reporting.

- **Additional Features:**
  - Real-time input validation.
  - Fully responsive design.
  - Performance data logging for analysis.

## **Technologies Used**

### **Frontend**
- **HTML5**: Page structure.
- **CSS**: Styling and responsiveness.
- **JavaScript**: Interactivity.

### **Backend**
- **Python (Flask)**: Web framework.
- **SQLite**: User data storage.

### **Data Analysis**
- **Python (pandas, scipy)**: Performance evaluation.
- **Statistical Tests**: Paired t-tests, SUS scoring.

## **Setup Instructions**

To run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/joyelpbiju/incident-response-system.git
   cd incident-response-system
2.Run the Flask application:
python src/app.py
then open 
http://127.0.0.1:5000
### **Limitations**
This project was conducted in a controlled environment and has the following limitations:

-**Predefined Answers**: The study assumes that users provide exact predefined answers, which may not always happen in real-world scenarios.

-**Controlled Environment:** The system was not deployed but tested in a structured setting.

-**Task Familiarity:** Users interacted with Prototype A first, which may have influenced their experience with Prototype B.

-**Limited Sample Size:** The study involved 30 participants, limiting generalizability.

-**No AI Adaptability:** The chatbot (Prototype B) follows a fixed script and does not adapt dynamically to user behavior.

### **Project Documentation**
For a detailed analysis, methodology, experimental results, and discussion, refer to the Short Report:

📄 [Short Report](short report/Short Report.pdf)



