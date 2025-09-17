# 🎓 School Management System

A modern web application for managing schools, teachers, classes, and curriculum distribution.  
Built with **Django** (backend), **React + Tailwind CSS** (frontend), and **PostgreSQL** (database).

---

## 🚀 Overview

This system provides a complete solution for organizing and tracking educational resources in schools.  
It helps administrators and teachers to plan curriculum, allocate teachers to classes, and verify distributions with an intuitive interface.

---

## 📑 Main Features

- **Curriculum Planning (Plan-cadru)**  
  View and filter the curriculum plan by educational level, class, subject, and area.

- **Teacher Allocations (Repartizare)**  
  Assign teachers to subjects and classes, with real-time validation and duplicate prevention.

- **Verification (Verificare)**  
  Visual overview of all allocations — which classes have which subjects and which teachers.

- **Teaching Staff (Cadre didactice)**  
  Manage educators (0–4) and class teachers (diriginți) with automatic allocations based on rules.

- **Data Import (Import)**  
  Upload CSV files with teachers, classes, and curriculum plans. Includes validation and error handling.

- **Settings (Setări)**  
  Manage educational areas (arii) and control their display order in the plan-cadru.

---

## 🛠️ Tech Stack

- **Backend:** Django + Django REST Framework  
- **Frontend:** React + Vite + Tailwind CSS  
- **Database:** PostgreSQL  
- **Containerization:** Docker & Docker Compose  

---

## 📂 Project Structure

school-mgmt/
│
├── backend/ # Django backend (API + models + import commands)
├── frontend/ # React frontend (UI with Tailwind CSS)
├── docker-compose.yml
└── README.md

yaml
Kód másolása

---

## 🎯 Goals

- Provide a **clear overview** of classes, teachers, and curriculum.  
- Automate repetitive tasks like teacher-class assignments.  
- Support **data import** from CSV for quick setup.  
- Ensure a **user-friendly, responsive interface** for administrators and staff.  

---

## 💡 Future Improvements

- Authentication & role-based access (Admin, Teacher, Student).  
- Export functionality (PDF/Excel reports).  
- Multi-language support.  
- Integration with scheduling & timetables.  

---

## 👩‍💻 Authors

Developed as a learning and practical project.  
