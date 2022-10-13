## Monitoring Test Solution

Monitoring system, that alerts the team if denied, failed or reversed transactions are above normal levels.

### How to run the project

```bash
    # Clone the repository
    $ git clone git@github.com:RafaelCunhaS/Monitoring-Test.git

    # Go into the project's directory
    $ cd Monitoring-Test

    # Create your own virtual environment
    $ python3 -m venv .venv && source .venv/bin/activate
    
    # Install the dependencies
    $ python3 -m pip install -r dev-requirements.txt
    
    # And run the API
    $ uvicorn main:app --reload
```
You can test the POST method of the API on [localhost:8000/docs](http://127.0.0.1:8000/docs)