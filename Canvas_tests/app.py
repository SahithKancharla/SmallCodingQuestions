import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Canvas API URL
CANVAS_URL = "https://canvas.vt.edu"

# Endpoint to get courses for the current user
COURSES_URL = f"{CANVAS_URL}/api/v1/courses"

# Retrieve Canvas API token from environment variable
API_TOKEN = os.getenv("CANVAS_CODE")
if not API_TOKEN:
    print(
        "Canvas API token not found. Make sure to set the CANVAS_CODE environment variable."
    )
    exit()

# Set the Authorization header with the API token
headers = {"Authorization": f"Bearer {API_TOKEN}"}

try:
    # Get current year
    current_year = datetime.utcnow().year

    # Make a GET request to retrieve courses the user is enrolled in
    courses_response = requests.get(COURSES_URL, headers=headers)

    # Check if the request was successful (status code 200)
    if courses_response.status_code == 200:
        courses = courses_response.json()

        # Iterate over each course to filter and retrieve data for this year's courses
        for course in courses:
            # Check if the 'start_at' field exists and is in the expected format
            print(course)
            if "start_at" in course and isinstance(course["start_at"], str):
                print("reached here")
                try:
                    course_start_year = datetime.strptime(
                        course["start_at"], "%Y-%m-%dT%H:%M:%SZ"
                    ).year
                except ValueError:
                    print(f"Invalid 'start_at' format for course: {course['name']}")
                    continue

                if course_start_year == current_year:
                    course_id = course["id"]
                    course_name = course["name"]
                    print(f"Course: {course_name}")

                    # Make a GET request to retrieve assignments for the course
                    assignments_response = requests.get(
                        f"{CANVAS_URL}/api/v1/courses/{course_id}/assignments",
                        headers=headers,
                    )

                    # Check if the request was successful (status code 200)
                    if assignments_response.status_code == 200:
                        assignments = assignments_response.json()

                        # Print upcoming assignments for the course
                        for assignment in assignments:
                            if assignment.get("due_at"):
                                due_date = assignment["due_at"]
                                assignment_name = assignment["name"]
                                print(
                                    f"\tAssignment: {assignment_name} - Due: {due_date}"
                                )
                    else:
                        print(
                            f"\tFailed to retrieve assignments. Status code: {assignments_response.status_code}"
                        )
            else:
                print(
                    f"Missing or invalid 'start_at' field for course: {course['name']}"
                )

    else:
        print(
            f"Failed to retrieve courses. Status code: {courses_response.status_code}"
        )

except requests.RequestException as e:
    print("A request error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
