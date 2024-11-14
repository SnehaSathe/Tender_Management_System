
### Project Title
```
# Tender Management System
```

### Project Description

```
The Tender Management System is a web-based platform that automates the tendering process, aiming to achieve transparency and efficiency in the selection of the best bids. The system allows vendors to view and bid on tenders, while administrators manage tenders, view quotations, and finalize results.
```

### Key Features
- User roles: Admin and Vendor
- Admins can create and manage tenders.
- Vendors can view tenders and place bids.
- System sorts bids by the lowest quote and vendor feedback.
- Secure document management and notifications.

---

## 3. **Technology Stack**

### Frontend:
- HTML
- CSS
- JavaScript

### Backend:
- Python (Django Framework)
- SQLite Database

### Additional Tools:
- Django templates for dynamic content rendering.
- Python libraries for backend logic.
  
---

## 4. **Installation Instructions**

### Prerequisites:
- Python 3.x
- Django 3.x
- SQLite

### Setup Instructions:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/tender-management-system.git
   cd tender-management-system
   ```

2. **Create Virtual Environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   - Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 5. **Usage**

### Admin User Flow:
- Admins can log in, create tenders, view submitted quotations, and finalize the tendering process.
- Tenders can be categorized, and admin can select vendors based on bid values.

### Vendor User Flow:
- Vendors register and log in to the system.
- Vendors can view available tenders, place bids, and receive notifications about the status of their bids.

---

## 6. **Screenshots**

Include some screenshots of the system for visual representation.

![image](https://github.com/user-attachments/assets/a30b09f2-e346-4edd-b06a-dd447727b4fa)

![image](https://github.com/user-attachments/assets/d98eaaeb-23a7-49f6-8a5f-b3177f7c5ba7)


### Admin Dashboard:

*Admin functionalities: Create/View tenders and see submitted bids.*

![image](https://github.com/user-attachments/assets/99087df2-7b8e-427c-884d-390a0d65a679)

![image](https://github.com/user-attachments/assets/15fbe744-4bd1-4ec2-b209-67c3389af666)

![image](https://github.com/user-attachments/assets/8d3d69c1-34e7-43d4-98c6-ee727bbf3c85)

![image](https://github.com/user-attachments/assets/70d89016-1c33-4e04-8d1e-1efc83d7fca1)



### Vendor Dashboard:
*Vendor functionalities: View tenders, submit quotations.*

![image](https://github.com/user-attachments/assets/18394b4f-286b-4f02-9458-4f4e73dcd43b)

Bid Details

![image](https://github.com/user-attachments/assets/fa6af959-2ad6-40c6-ba48-2b9e25927af1)

Bid Form

![image](https://github.com/user-attachments/assets/02e2945b-da9e-428d-8219-28a4d12b9bac)

Bid List

![image](https://github.com/user-attachments/assets/d8f46288-52e7-4028-b080-82c492ff299b)

Bid Approval

![image](https://github.com/user-attachments/assets/1d32fd8f-f2ad-4c6b-826f-fd830fb65f77)



---

## 7. **Contributing**

### Contribution Guidelines:

- Fork the repository.
- Create a new branch (`git checkout -b feature-name`).
- Make changes and commit (`git commit -m 'Add feature'`).
- Push the branch (`git push origin feature-name`).
- Submit a Pull Request.

---

## 8. **License**

This project is licensed under the MIT License.

---

## 9. **References**
- [Django Framework](https://www.djangoproject.com/)
- [SQLite Database](https://www.sqlite.org/index.html)
  
---
