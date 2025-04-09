import json

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

tests = [
    {"name": "test_addition", "func": test_addition, "points": 2},
    {"name": "test_subtraction", "func": test_subtraction, "points": 3},
]

results = []
total_score = 0
max_score = sum(test["points"] for test in tests)

for test in tests:
    try:
        test["func"]()
        results.append({"name": test["name"], "status": "passed", "points": test["points"]})
        total_score += test["points"]
    except AssertionError:
        results.append({"name": test["name"], "status": "failed", "points": 0})

# Final JSON structure with the score included
output = {
    "score": total_score,  # This will show the total score
    "max_score": max_score,  # This shows the max score for the assignment
    "tests": results  # Detailed test results
}

# Write the results to the results.json file
with open("results.json", "w") as f:
    json.dump(output, f, indent=4)