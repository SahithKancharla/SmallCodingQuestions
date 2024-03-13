import os
import requests
import json

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Canvas API URL
CANVAS_URL = "https://canvas.vt.edu"

# Endpoint to get assignments for the current user
ASSIGNMENTS_URL = "{}/api/v1/courses/{}/assignments".format(CANVAS_URL, "{}")

# Retrieve Canvas API token from environment variable
API_TOKEN = os.getenv("CANVAS_CODE")
if not API_TOKEN:
    print("Canvas API token not found. Make sure to set the CANVAS_CODE environment variable.")
    exit()

# Set the Authorization header with the API token
headers = {"Authorization": f"Bearer {API_TOKEN}"}

try:
    # Make a GET request to retrieve courses the user is enrolled in
    courses_response = requests.get(
        f"{CANVAS_URL}/api/v1/users/self/upcoming_events", headers=headers
    )

    # Check if the request was successful (status code 200)
    if courses_response.status_code == 200:
        courses = courses_response.json()
        json_data = json.dumps(courses, indent=4)

        # Output the JSON data to a file
        with open("data.json", "w") as f:
            f.write(json_data)

        # Iterate over each course to retrieve assignments
        for course in courses:
            course_id = course["id"]
            assignments_response = requests.get(ASSIGNMENTS_URL.format(course_id), headers=headers)

            # Check if the request was successful (status code 200)
            if assignments_response.status_code == 200:
                assignments = assignments_response.json()
                # Print assignments for the current course
                print(f"Assignments for course {course_id}:")
                for assignment in assignments:
                    print(assignment)
            else:
                print(f"Failed to retrieve assignments for course {course_id}. Status code: {assignments_response.status_code}")
    else:
        print(f"Failed to retrieve courses. Status code: {courses_response.status_code}")
except Exception as e:
    print("An error occurred:", e)
