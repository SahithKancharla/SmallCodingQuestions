import os
import requests
import json

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Canvas API URL
CANVAS_URL = "https://canvas.vt.edu"

# Endpoint to get courses for the current user
COURSES_URL = "{}/api/v1/courses".format(CANVAS_URL)

# Endpoint to get assignments for a course
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
    courses_response = requests.get(COURSES_URL, headers=headers)

    # Check if the request was successful (status code 200)
    if courses_response.status_code == 200:
        courses = courses_response.json()

        # Iterate over each course to retrieve assignments
        for course in courses:
            course_id = course["id"]
            if course.get('name') is not None:
                print(course["name"])
            # assignments_response = requests.get(ASSIGNMENTS_URL.format(course_id), headers=headers)

            # # Check if the request was successful (status code 200)
            # if assignments_response.status_code == 200:
            #     assignments = assignments_response.json()
            #     # Print assignments for the current course
            #     # print(f"Assignments for course {course['name']} (ID: {course_id}):")
            #     if assignments is not None:
            #         for assignment in assignments:
            #             print(assignment['due_at'])
            # else:
            #     print(f"Failed to retrieve assignments for course {course_id}. Status code: {assignments_response.status_code}")
    else:
        print(f"Failed to retrieve courses. Status code: {courses_response.status_code}")

except requests.RequestException as e:
    print("A request error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
