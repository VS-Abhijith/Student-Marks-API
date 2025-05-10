import json

def handler(request):
    # Get 'name' query parameter
    query = request.args.get('name')
    names = query.split(",") if query else []

    # Load student data from JSON file
    with open("q-vercel-python.json", "r") as file:
        student_list = json.load(file)

    # Convert list to dictionary for easy lookup
    student_dict = {student["name"]: student["marks"] for student in student_list}

    # Find marks
    marks = [student_dict.get(n, None) for n in names]

    # Return JSON response with CORS headers
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({"marks": marks})
    }
