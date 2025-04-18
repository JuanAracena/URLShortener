# URLShortener

## Description
This project allows users to create unique URL shortcuts from a given name. Additionally, it lets users create URL shortcuts for files they upload. It uses flask to manage the web application and API.

## Technology Stack

### Backend
  - **Language**: Python (ver 3.12.2)
  - **Framework**: Flask
  - **API**: RESTful API

### Frontend
  - **Language**: JavaScript, HTML
  - **Framework**: Bootstrap
  - **Styling**: CSS

## Getting Started

### Prerequisites
Before you begin, ensure you have the following software installed:
  - [Python](https://www.python.org/downloads/)
  - [Git](https://git-scm.com/)

### Installation
To set up the project locally, follow these steps:
  1. Clone the repository:
      ####
         git clone https://github.com/JuanAracena/URLShortener.git
  2. Navigate to the project directory:
     ####
         cd URLShortener
  3. Install pipenv:
     ####
         pip install pipenv
  5. Create and start a virual environment:
     ####
         pipenv shell
  6. Install flask inside the virtual environment:
     ####
         pipenv install flask
  7. Set "urlshort" as the file flask is going to look for when executing the code:
     ####
         set FLASK_APP=urlshort
  8. Run flask:
     ####
         flask run
