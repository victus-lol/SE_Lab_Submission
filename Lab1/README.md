# Lab 1 - Requirements Engineering & UML Use Case Modelling
**Course:** Software Engineering Lab (CSE, PES University)  
**Name:** Aaryan Dubey  
**SRN:** PES2UG24CS016  
**Problem Statement 14:** Corporate Mental Wellness & Counseling Platform (Healthcare & Telemedicine)

### About the Project
This project is about a corporate mental wellness platform where employees can check their stress levels, book confidential sessions with therapists and track their wellness over time. The main idea is to keep everything anonymous - the employer or even the therapist should not see the employee's real identity (email, ID, name). Instead the system gives a pseudo-ID like EMP-XXXX for all bookings and records.

We are using this repo to submit Lab 1 deliverables as per the handout given in class.

---

### Folder Structure

```
PES2UG24CS016_Lab1_MentalWellness/
├── README.md
├── requirements/
│   ├── requirements_table.md      # Requirements table in markdown
│   ├── requirements_table.docx    # Same table in Word format
│   └── requirements_table.xlsx    # Excel version with peer comments
├── uml/
│   ├── use_case_diagram.puml      # PlantUML source file
│   ├── use_case_diagram.dot       # Graphviz DOT source
│   ├── use_case_diagram.svg       # Vector image
│   ├── use_case_diagram.png       # PNG image
│   └── use_case_diagram.pdf       # Final PDF for submission
└── specifications/
    ├── use_case_flow_spec.md      # Flow spec in markdown
    ├── use_case_flow_spec.docx    # Word version
    └── use_case_flow_spec.pdf     # 1 page PDF
```

---

### What is submitted

**1. Requirements Table (5 FR + 2 NFR)**
All requirements are written in "The system shall..." format with Req ID, Type, Priority, Acceptance Criteria and Rationale. Peer comments column also added after review with classmate. FR-001 and NFR-001 are as per the problem statement given.

**2. UML Use Case Diagram**
Actors: Corporate Employee, Licensed Therapist, System Administrator
Use Cases: UC-01 to UC-10 (10 use cases total)
Relationships: 
- UC-03 includes UC-01 and UC-08
- UC-09 extends UC-02 (when stress score >=15)
- UC-10 extends UC-03 (when schedule conflict)

Diagram made in draw.io / PlantUML and exported to PDF.

**3. Use Case Flow Specification**
Detailed flow for UC-03 - Book Confidential Counseling Session. It has preconditions, postconditions, main success scenario (10 steps) and 3 alternate flows (slot conflict, cancellation, crisis escalation).

---

### How to push to GitHub (for submission)
```bash
git init
git add .
git commit -m "Lab 1 submission - PES2UG24CS016"
git branch -M main
git remote add origin https://github.com/<your-username>/Lab-1.git
git push -u origin main
```

> Note: This README is the main documentation for Lab 1. All files are kept in submission-ready formats.
