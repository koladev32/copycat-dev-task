# copycat-dev-task

Run the project

```python
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

```

### Frontend

```
cd frontend
echo "REACT_APP_API_URL=http://localhost:8000/api" >> .env

yarn install
yarn start
```

Check localhost:3000 to use the React App.
