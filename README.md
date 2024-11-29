# **Incident Response System**

This project is being developed by [Joshua Porunnedath Biju](https://github.com/JOSHUAPBIJU) and [Joyel Porunnedath Biju](https://github.com/joyelpbiju).

![License](https://img.shields.io/badge/license-MIT-green) ![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen) ![Status](https://img.shields.io/badge/status-active-brightgreen)

## **Project Overview**

The **Incident Response System** is part of the **Interactive Systems** subject, focusing on creating intuitive and user-friendly interfaces. This project includes two prototypes aimed at improving user interaction, making it more engaging and accessible:
- **Prototype A:** A multi-step form-based approach for user input.
- **Prototype B:** An interactive chatbot widget that offers a conversational interface for the same tasks.

The goal is to compare these prototypes and demonstrate how interactivity can enhance the user experience.

**This project is a work in progress, with additional features and refinements planned.**

---

## **Features**

- **Prototype A:**
  - Multi-step form for structured input collection.
  - Progress bar to track completion.
  - Traditional form-based structure.

- **Prototype B:**
  - Conversational chatbot for an engaging user experience.
  - Dynamic responses based on user inputs.
  - Interactive and intuitive design.

- **Other Features:**
  - Real-time input validation.
  - Responsive design for all devices.

---

## **Technologies Used**

### **Frontend**
- **HTML5**: For structuring the prototypes.
- **CSS3**: For styling and responsive design.
- **JavaScript**: For dynamic interactivity.

### **Backend**
- **Python (Flask)**: For serving templates and managing user interactions.

---

## **Folder Structure**

```
incident_response_system/
├── src/
│   └── app.py                 # Main application logic
├── static/
│   ├── prototype_a.css        # Styles for Prototype A
│   ├── prototype_b.css        # Styles for Prototype B
├── templates/
│   ├── prototype_a.html       # Multi-step form (Prototype A)
│   ├── prototype_b.html       # Chatbot widget (Prototype B)
│   └── success.html           # Submission success page
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---

## **How to Run the Project**

### **Prerequisites**
1. Install Python (version 3.8 or later).
2. Install `pip` for managing Python packages.

### **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/joyelpbiju/incident-response-system.git
   cd incident-response-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python src/app.py
   ```
4. Open the app in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## **Contributing**

We welcome contributions to enhance the project! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
