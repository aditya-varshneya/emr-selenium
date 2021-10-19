cd C:\Users\Lenovo\Documents\GitHub\emr-selenium-automation\jenkins
pytest "test_setup.py"
pytest -v --tb=short --html=Automation_report.html --self-contained-html
pause