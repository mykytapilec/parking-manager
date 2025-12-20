# Parking Manager Application

Parking Manager is a desktop application for managing a parking lot with support for both regular and electric vehicles.  
The project demonstrates a clean, layered architecture with domain-driven design principles and classic object-oriented design patterns.

The application provides a simple graphical interface for creating parking lots, parking and removing vehicles, and viewing the current parking and EV charging status.

---

## Features

- Create a parking lot with configurable capacity
- Support for:
  - Regular cars
  - Motorcycles
  - Electric cars
  - Electric motorcycles
- Separate handling of EV and non-EV parking slots
- EV charging status tracking
- Query vehicles by:
  - Registration number
  - Color
- Clean separation of UI, application logic, and domain logic
- Easily extensible architecture

---

## Tech Stack

- **Language:** Python 3.13+
- **GUI:** Tkinter
- **Architecture:** Layered Architecture
- **Design Patterns:**
  - Strategy Pattern (parking slot allocation)
  - Factory Pattern (vehicle creation)
- **Testing:** Python standard execution (no external frameworks required)

---

## Project Structure

parking-manager/
│
├─ domain/
│ ├─ vehicle.py
│ ├─ factory.py
│ └─ strategy.py
│
├─ application/
│ └─ parking_service.py
│
├─ ui/
│ └─ parking_manager.py
│
├─ tests/
│ ├─ main_test.py
│ └─ test_parking_service.py
│
├─ UML/
│ └─ (class and sequence diagrams)
│
├─ README.md
└─ ParkingManager.py


---

## How to Run the Application

### Prerequisites

- Python **3.13 or newer**
- Tkinter (included in most Python installations)

Check Python version:
```bash
python3 --version


### Run the UI

From the project root directory:
python3 ParkingManager.py

This will launch the Parking Lot Manager graphical interface.

### How to Run Tests

Run domain and service tests manually:

python3 tests/main_test.py
python3 tests/test_parking_service.py

Expected output will confirm correct slot allocation and removal logic.

### Architecture Overview

The application follows a layered architecture:

- UI Layer (ui/)
Handles user interaction (Tkinter)
Delegates all logic to the application layer

- Application Layer (application/)
Coordinates use cases
Acts as a facade between UI and domain

- Domain Layer (domain/)
Core business logic
Vehicle entities, parking lot logic
Strategy and Factory patterns

This structure improves testability, maintainability, and scalability.

## Future Improvements

- Persistence layer (database integration)
- REST API for remote access
- Support for multiple parking lots
- Real-time EV charging simulation
- Authentication and user roles

## License

This project is provided for educational and experimental purposes.