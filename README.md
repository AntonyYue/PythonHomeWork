# Python Homework Project


## Project Structure

```
.
├── poetry.lock
├── pyproject.toml
├── task1/
│   └── FizzBuzz.py
├── task2/
│   ├── bowling.py
│   └── test_bowling.py
├── task3/
│   ├── gilded_rose.py
│   ├── test_gilded_rose.py
│   └── texttest_fixture.py
├── task4/
│   ├── app.py
│   ├── instance/
│   │   └── todos.db
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   └── templates/
│       └── index.html
└── task5/
    ├── mnist_model.h5
    └── mnist_train.py
```

## Tasks Overview

### Task 1 - FizzBuzz

Implements the classic FizzBuzz problem using Python's control flow structures. Useful for understanding conditional logic and loops.

### Task 2 - Bowling Score Calculator

A program to calculate scores in a game of bowling. Includes unit tests to validate the correctness of the scoring logic.

### Task 3 - Gilded Rose Kata

A refactoring exercise based on the well-known Gilded Rose kata. Helps practice working with legacy code and improving design through unit testing.

### Task 4 - Flask Todo App

A simple web-based todo list application using the Flask framework. Features include:

* HTML templating with Jinja2
* Styling with CSS
* Interactivity using JavaScript
* Persistent storage using SQLite

### Task 5 - MNIST Digit Recognition

Trains a neural network on the MNIST dataset to recognize handwritten digits. Uses TensorFlow/Keras for model building and training.

## Setup Instructions

### Prerequisites

* Python 3.12+
* [Poetry](https://python-poetry.org/) for dependency management

### Installation

```bash
poetry install
```

### Running the Tasks

**Task 1: FizzBuzz**

```bash
python task1/FizzBuzz.py
```

**Task 2: Bowling Calculator Tests**

```bash
pytest task2/
```

**Task 3: Gilded Rose Tests**

```bash
pytest task3/
python task3/texttest_fixture.py 10
```

**Task 4: Run Flask App**

```bash
cd task4
flask run
```

**Task 5: Train MNIST Model**

```bash
python task5/mnist_train.py
```

## License

This project is provided for educational purposes.

## Author


