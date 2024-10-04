# PACE Probe

Welcome to the PACE Probe project! This Django application aims to provide tailored educational resources for users based on their profiles.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- Git

## Getting Started

Follow these steps to set up the project on your local machine.

| Step | Command | Description |
|------|---------|-------------|
| 1    | `git clone https://github.com/frankmathewsajan/pace_probe.git` | Clone the repository. |
|      | `cd pace_probe` | Navigate into the cloned directory. |
| 2    | `python -m venv venv` (Windows) <br> `python3 -m venv venv` (macOS/Linux) | Create a virtual environment. |
| 3    | `venv\Scripts\activate` (Windows) <br> `source venv/bin/activate` (macOS/Linux) | Activate the virtual environment. |
| 4    | `pip install -r requirements.txt` | Install the required packages from `requirements.txt`. |
| 5    | `python manage.py migrate` | Apply the database migrations. |
| 6    | `python manage.py runserver` | Start the Django development server. |

## Usage

After starting the server, open your web browser and navigate to `http://127.0.0.1:8000/` to access the application. Follow the on-screen instructions to use the PACE Probe features.

## Contributing

Contributions are welcome! If you want to contribute, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using PACE Probe! If you have any questions or issues, please open an issue on the GitHub repository.
