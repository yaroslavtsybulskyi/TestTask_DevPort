# Test Task - DevPort

## Prerequisites

Before running the tests, ensure that the following dependencies are installed:

- `pytest`
- `selenium`
- `pytest-html`
- `allure` (for Allure report)
- `black` (optional, for code linting)

You can install these dependencies using pip:

```
pip install pytest selenium pytest-html allure black
```

## Running All Tests
To run all tests, simply execute the following command:

```
pytest
```

## Running Specific Test Files
To run tests from a specific test file, use the following command:

```
pytest tests/specific_file.py
```

##Running Specific Tests
To run a specific test, use the -k option followed by the test name:

```
pytest -k specific_test_name
```

## Generating HTML Report
To generate an HTML report for the test results, run:

```
pytest --html=report.html
```

## Running Tests with Allure

To run the tests and generate Allure reports, follow these steps:
1. Run the tests and generate the Allure results:

```
pytest --alluredir=allure_results
```

2. Serve the Allure report:

```
allure serve allure_results
```
   
Feel free to adjust the paths and commands according to your project structure and preferences.
