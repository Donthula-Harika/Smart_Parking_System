# Smart Parking System 🚗

A Python-based simulation of a smart parking solution that applies advanced Object-Oriented Programming (OOP) principles in a structured, scalable way.

##  Key Highlights
-  **Encapsulation**: Secure vehicle data with private attributes and getter/setter methods  
-  **Inheritance**: Specialized vehicle types (Bike, Car, SUV, Truck) with unique properties  
-  **Polymorphism**: Dynamic parking fee calculation and method overriding  
-  **Abstraction**: Payment interface supporting multiple methods (Cash, Card, UPI)  
-  **Spot Management**: Assign vehicles based on size compatibility and availability  
-  **Interactive Simulation**: Demonstrates parking, unparking, and payment workflows

## 🚘 Vehicles & Fees

| Vehicle Type | Feature          | Fee per Hour |
|--------------|-----------------|--------------|
| Bike         | Helmet required | ₹20          |
| Car          | Number of seats | ₹50          |
| SUV          | 4-wheel drive   | ₹70          |
| Truck        | Load capacity   | ₹100         |


---

## 📂 Project Structure

- **Vehicle classes**: Base class and derived classes with encapsulated attributes  
- **ParkingSpot**: Size-based allocation and vehicle management  
- **ParkingLot**: Centralized management of spots and vehicles  
- **Payment (Abstract Class)**: Polymorphic handling of payments (Cash, Card, UPI)


## 🛠 How It Works
1. Creates a parking lot with various spot sizes  
2. Instantiates multiple vehicle objects with unique features  
3. Parks vehicles based on available spots and size constraints  
4. Calculates parking fees dynamically using polymorphism  
5. Processes payments using an abstract Payment interface  

---

## ▶ How to Run

```bash
git clone https://github.com/your-username/smart-parking-system.git
cd smart-parking-system
python smart_parking.py
```
Follow the prompts to park and unpark vehicles, and process payments.

---

📚 What You’ll Learn

Designing systems with clean, reusable OOP structures

Handling real-world scenarios like parking constraints and payments

Applying abstraction and runtime polymorphism in Python

Managing object states using encapsulation for data integrity

---

📌 Notes

This project simulates parking operations with predefined scenarios to showcase OOP principles. Minimal user input is required (only for selecting payment methods).
