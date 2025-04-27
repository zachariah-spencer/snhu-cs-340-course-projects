# CS 340 Grazioso Salvare Dashboard Web Application <br> by Zachariah Spencer

## About the Project
The Grazioso Salvare Dashboard Web Application is an open‑source, interactive dashboard built with Python, MongoDB, and Dash. It enables Grazioso Salvare staff to easily filter, visualize, and map potential search‑and‑rescue candidates from shelter data around Austin, TX. Users can filter dogs by rescue type (Water, Mountain, Disaster), view detailed tables, pie‑chart breakdowns of breeds, and see geographic markers of selected animals.

## Motivation
Grazioso Salvare trains dogs for life‑saving missions—such as water rescues, wilderness searches, and disaster tracking—and relies on shelter data to find ideal candidates. Manually sifting through large datasets is time‑consuming and error‑prone. This dashboard provides a user‑friendly interface that reduces training time, minimizes selection errors, and can be adapted by other organizations via its open‑source GitHub repository.

## Getting Started
### Prerequisites <br>
* Python 3.8 or newer <br>
* pip (Python package installer) <br>
* Access to a MongoDB instance with the shelter data (host, port, username, password) <br>
* A modern web browser (Chrome, Firefox, Edge, Safari) <br>
  * <i>Optionally the latest version of Jupyter Notebook</i>

## Installation
1. Clone the repository
2. Set up a virtual environment
3. Install required packages
4. Configure database credentials: Open the primary .py file and replace the username, password, HOST, and PORT values in the CRUD initialization with your MongoDB connection details.

## Usage
1. Run the dashboard
2. Access in your browser
    1. Navigate to http://127.0.0.1:8050 (or the URL shown in the console).
3. Interact
    1. Select a rescue type via the radio buttons to filter the table.
    2. Click table rows to highlight and view location markers on the map.
    3. Hover or click on pie‑chart segments to inspect breed proportions.
### Code Example
Below is a simplified callback snippet showing how filtering logic is applied:  

  
![unnamed](https://github.com/user-attachments/assets/686cef2c-c885-40ce-b49c-7881aaa29d35)



### Tests
No formal test suite is included with this initial release. Future contributions are welcome to add:
* Unit tests for crud_module.py using pytest and a MongoDB test fixture.
* Integration tests for Dash callbacks with Dash’s testing framework.


### Screenshots
![unnamed2](https://github.com/user-attachments/assets/6bf837bb-ba4a-4268-ad3b-776a9599e496)
![unnamed3](https://github.com/user-attachments/assets/fbcf7e63-4b11-452a-9e52-460028f743bd)
![unnamed4](https://github.com/user-attachments/assets/2f5ee50b-079e-4241-a475-03cee849d5ec)

## Retrospective
### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future? <br>

By isolating all database interactions in a single, well-documented CRUD module, I enforced a clear separation of concerns: the module handles connection setup, query logic, and error handling, while the dashboard code simply imports and calls its methods. Consistent naming conventions, comprehensive docstrings, and adherence to PEP 8 made the module’s interface both predictable and self-explanatory. When I built the Dashboard in Project Two, I didn’t have to rewrite any connection logic or duplicate query code; any change to how we authenticate, throttle, or log queries happens in one place. This approach drastically reduced boilerplate, minimized the surface for bugs, and made it trivial to onboard new developers or extend functionality without wading through UI code.

Because the CRUD module exposes only generic create/read/update/delete methods parameterized by collection and filter criteria, I can reuse it wherever I need database access. In the future, I could wrap it behind a Flask or FastAPI layer to expose our MongoDB as a public API, plug it into ETL pipelines for nightly data migrations, or connect it to different front-end frameworks with zero changes. If we ever decide to swap MongoDB for another datastore, I’d only need to rewrite the module’s internal logic; our dashboard and any other consuming code would remain completely unaffected.

<br>

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests? <br>

I start every problem by first clarifying requirements with stakeholders, defining what data needs to be captured, which queries will drive decisions, and what success looks like. I then translate these into an abstract model and a minimal set of core operations. For the Grazioso Salvare project, that meant sketching out dog profiles, rescue type filters, and outcome metrics before writing any code. I built a quick prototype in MongoDB using the CRUD module, validated it against real shelter data, and iterated based on client feedback. Unlike many course assignments where specs are fixed and toy-scale, this real-world project demanded an agile, user-centered cycle of build, demo, and refine. By separating data access in the CRUD module from presentation in the dashboard, I could rapidly adjust schemas or queries without rewriting UI code and ensure every change delivered immediate value.

Going forward, I would formalize this process with ER diagrams or JSON schema definitions up front, enforce schema validation via MongoDB’s JSON Schema or a lightweight ORM, and introduce automated tests for each CRUD operation. I would also plan indexes and sharding strategies early to handle growth and integrate continuous integration pipelines to run both unit tests and performance benchmarks. For any future client, this combination of clear requirement gathering, iterative prototyping, modular abstractions, and test-driven schema design creates databases that not only meet immediate needs but remain robust, scalable, and easy to evolve.

<br>

### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better? <br>

Computer scientists translate real‐world problems into precise data structures and algorithms, then build and maintain systems that automate those solutions at scale. They begin by modeling the problem domain, choose or design appropriate algorithms and data stores, and implement software that is reliable, efficient, and secure. By applying principles of modular design, testing, and performance optimization, computer scientists ensure that systems not only solve the immediate need but can adapt to evolving requirements and growing data volumes. This work matters because it turns raw data into actionable insights, reduces manual effort, and drives innovation across industries.

In a project like the one for Grazioso Salvare, my role as a computer scientist means creating a robust database layer and an intuitive dashboard that together streamline the identification of rescue‐trainable dogs. By encapsulating database logic in a reusable CRUD module and presenting dynamic filters and visualizations, staff can instantly pinpoint candidates by age, breed, or rescue specialty without sifting through spreadsheets. This increases accuracy, saves countless hours of manual work, and lets the organization focus resources on training rather than data wrangling. As the code is open source, similar agencies can adapt and extend the tools, multiplying the project’s impact across the animal‐rescue community.

<br>

## Contact
Your name: Zachariah Spencer
