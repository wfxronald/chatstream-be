## chatstream-be

A simple mock implementation of text streaming in Flask.

### How to setup the project
1. Create a virtual environment `python -m venv env`
2. Activate the virtual environment `env/Scripts/activate.bat`
3. Install all the requirements `pip install -r requirements.txt`
4. Run the backend server `python main.py`

### API documentation
Only one endpoint is available: http://localhost:5000/chat.  
The API must be called using method POST and the following body.
```json
{
  "message": "sample message goes here"
}
```
It will return a text stream.
