# universiti-website
University Management System (Flask/MySQL)
Developed a full-stack web application to automate university operations, including student/teacher portals, course registration, and campus services.

Core Features:

User Roles: Separate interfaces for students (course selection, exam schedules, food reservations) and teachers (grading, attendance).

Academic Workflows: Implemented course enrollment, grade calculation, and exam scheduling using MySQL stored procedures.

Campus Services: Integrated food reservation system with automated wallet deductions via SQL triggers.

Data Management: Designed relational database schema with 15+ tables (student, teacher, subject, presence) and views for reporting.

Backend Logic:

Utilized MySQL triggers to dynamically update student averages and financial transactions.

Built stored procedures for CRUD operations, ensuring data integrity and business logic compliance.

Frontend/API:

Developed RESTful routes with Flask for profile management, authentication, and form submissions.

Integrated WTForms for validation of user inputs (e.g., personal info, course selection).
