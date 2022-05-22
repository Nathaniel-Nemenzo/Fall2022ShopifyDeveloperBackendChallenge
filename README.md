Running the application:
- Setting up virtual environment
  - `python3 -m venv venv`
- Installing dependencies
  - `python3 -m pip install -r requirements.txt`
- Running the application
  - `flask run`
  - open using the provided url

Endpoints:
- /inventory/create
- /inventory
- /inventory/:id
- /inventory/:id/update
- /inventory/:id/delete

- /warehouse/create
- /warehouse
- /warehouse/:id
- /warehouse/:id/update
- /warehouse/:id/delete

Improvements:
- Changing warehouse allocations for inventory (can only be done upon creation)
- Changing inventory within a certain warehouse (can only be done upon creation)
- Error-handling
- Cleanliness (a lot of code-repeat in endpoints)
