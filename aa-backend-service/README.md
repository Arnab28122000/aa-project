# aa-backend-service

# Step1: Setup environment variables
This is required to setup environmemnt variables<br>
`echo $variable_name`<br>
`export variable_name=value`<br>
<h3>Variables to set: </h3>
<li>DATABASE_URL</li>

# Step 2: Start the application
`uvicorn main:app --reload`<br>
# Step 3: Create docker container
`docker build -t cloud-analytics-service .`