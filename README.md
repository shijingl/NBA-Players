### **Project Description**

This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

**Preparation** 
1. Virtual environment set up
```
python3 -m venv venv_flask
```

2. Activate virtual environment
```
source venv_flask/bin/activate
```

3. Install all the dependencies
```
pip3 install -r requirements.txt
```

**How to Run** 
1. set up application database
```
python3 database_setup.py
```
2. Insert fake players data 
```
python3 players.py
```
3. Run the application 
```
python3 application.py
```
4. Access the application locally using
```
http://localhost:xxxx
```

**Using Google Login**
1. go to Google Dev Console
```
https://accounts.google.com/ServiceLogin/signinchooser?service=cloudconsole&passive=1209600&osid=1&continue=https%3A%2F%2Fconsole.developers.google.com%2F%3Fref%3Dhttps%3A%2F%2Fwww.google.com%2F&followup=https%3A%2F%2Fconsole.developers.google.com%2F%3Fref%3Dhttps%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin
```
2. Sign up or Login if promoted 
3. Go to Credentials
4. Select Create Credentials -> OAuth Client ID
5. Select Web Application
6. Enter name "Udacity-Item-Catalog"
7. Authorized JavaScript origins = http://localhost:xxxx
8. Authorized redirect URIs = 'http://localhost:xxxx/login' && 'http://localhost:xxxx/gconnect'
9. Select Create 
10. Copy the Client ID and paste it into the data-clientid in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run the application again
python application.py

**JSON Endpoints**

1. Catalog JSON: /catalog/JSON - Displays the whole catalog. Categories and all items. 
2. Category JSON: /catalog/<int:catalog_id>/JSON - Displays all categories 
3. Category Items JSON: /catalog/<int:catalog_id>/items/JSON - Displays items for a specific category
4. Category Item JSON: /catalog/<int:catalog_id>/items/<int:item_id>/JSON - Displays a specific category item
