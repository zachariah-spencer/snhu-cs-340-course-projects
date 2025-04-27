# CS 340 Grazioso Salvare Dashboard Web Application <br> by Zachariah Spencer

## About the Project
The Grazioso Salvare Dashboard Web Application is an open‑source, interactive dashboard built with Python, MongoDB, and Dash. It enables Grazioso Salvare staff to easily filter, visualize, and map potential search‑and‑rescue candidates from shelter data around Austin, TX. Users can filter dogs by rescue type (Water, Mountain, Disaster), view detailed tables, pie‑chart breakdowns of breeds, and see geographic markers of selected animals.

## Motivation
Grazioso Salvare trains dogs for life‑saving missions—such as water rescues, wilderness searches, and disaster tracking—and relies on shelter data to find ideal candidates. Manually sifting through large datasets is time‑consuming and error‑prone. This dashboard provides a user‑friendly interface that reduces training time, minimizes selection errors, and can be adapted by other organizations via its open‑source GitHub repository.

## Getting Started
### Prerequisites <br>
Python 3.8 or newer <br>
pip (Python package installer) <br>
Access to a MongoDB instance with the shelter data (host, port, username, password) <br>
A modern web browser (Chrome, Firefox, Edge, Safari) <br>
<i>Optionally the latest version of Jupyter Notebook</i>

## Installation
Clone the repository
Set up a virtual environment
Install required packages
Configure database credentials
Open the primary .py file and replace the username, password, HOST, and PORT values in the CRUD initialization with your MongoDB connection details.

## Usage
Run the dashboard
Access in your browser
Navigate to http://127.0.0.1:8050 (or the URL shown in the console).
Interact
Select a rescue type via the radio buttons to filter the table.
Click table rows to highlight and view location markers on the map.
Hover or click on pie‑chart segments to inspect breed proportions.
Code Example
Below is a simplified callback snippet showing how filtering logic is applied:

##Tests
No formal test suite is included with this initial release. Future contributions are welcome to add:
Unit tests for crud_module.py using pytest and a MongoDB test fixture.
Integration tests for Dash callbacks with Dash’s testing framework.


## Screenshots

## Contact
Your name: Zachariah Spencer
