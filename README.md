# Pokersonic
### Our Spring 2025 User Interface Design Project
# Pot Odds Learning Application

A web-based interactive application to teach poker players how to calculate and use pot odds for better decision-making. This application includes learning modules and quiz sections to help players understand when to call or fold based on mathematical probability.

## Project Overview

This application was developed as part of CS 4170 coursework to create an interactive learning experience for poker players. The app guides users through concepts of pot odds calculation, equity estimation, and decision-making in poker.

### Features

- **Interactive Learning Modules**: Step-by-step explanations of pot odds concepts
- **Visual Examples**: Clear examples with calculations and visual aids
- **Practice Quiz**: Test your understanding with real poker scenarios
- **Detailed Feedback**: Receive explanations for correct and incorrect answers
- **Mobile-Friendly Design**: Works on both desktop and mobile devices

## Repository Structure

```
/4170PotOdds
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── calc_font.ttf
│   ├── images/
│   │   ├── image1.png
│   │   ├── image2.png
│   │   └── ...
│   └── js/
│       └── script.js
├── templates/
│   ├── index.html
│   ├── layout.html
│   ├── learn.html
│   ├── quiz.html
│   ├── quiz_results.html
│   ├── text_content.html
│   ├── slider_content.html
│   └── transition.html
├── data.py
├── server.py
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Flask

### Installation

1. Clone the repository:
```
git clone https://github.com/Ferperlex/4170PotOdds.git
cd 4170PotOdds
```

2. Create a virtual environment (optional but recommended):
```
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```
   source venv/bin/activate
   ```

4. Install Flask:
```
pip install Flask
```

### Running the Application

1. Start the Flask server:
```
python server.py
```

2. Open a web browser and navigate to:
```
http://127.0.0.1:5000/
```

## Application Flow

1. **Home Page**: Introduction to the application with navigation options
2. **Learning Modules**:
   - What are pot odds?
   - When do pot odds matter?
   - Estimating equity
   - How to use pot odds
3. **Quiz**: Test your understanding with practical poker scenarios
4. **Results**: Get feedback on your answers with explanations

## Learning Content

The application covers the following key concepts:

- **Pot Odds Calculation**: How to calculate the ratio between the pot size and the cost of a call
- **Equity Estimation**: Using the "Rule of 4 and 2" to estimate your chances of winning
- **Decision Making**: Comparing pot odds to equity to make mathematically sound decisions
- **Practical Application**: Real-world poker scenarios to practice your skills

## Development Notes

- Built with Flask for the backend
- Uses Jinja2 templates for dynamic content
- Session management for tracking user progress
- Modular content structure for easy updates and maintenance

## Contributors

- Team members from CS 4170: Hannah, Sandy, Fernando

## License

This project was developed as part of a course assignment and is not licensed for public use.

---

## Acknowledgments

- CS 4170 instructors and TAs for guidance
- Poker resources and reference materials used for content development
