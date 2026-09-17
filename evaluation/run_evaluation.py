import json
import subprocess

with open("evaluation/test_cases.json") as f:
    test_cases = json.load(f)

passed = 0

for i, test in enumerate(test_cases, start=1):
    question = test["question"]
    expected_answer = test["expected_answer"]
    expected_source = test["expected_source"]

    result = subprocess.run(
        ["python", "src/main.py", "--data", "data", "--question", question],
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr

    answer_pass = all(word in output.lower() for word in expected_answer.lower().split())
    source_pass = expected_source.lower() in output.lower()
    test_pass = answer_pass and source_pass

    if test_pass:
        passed += 1

    print(f"\nTest {i}: {question}")
    print(f"Answer check: {'PASS' if answer_pass else 'FAIL'}")
    print(f"Source check: {'PASS' if source_pass else 'FAIL'}")
    print(f"Result: {'PASS' if test_pass else 'FAIL'}")

print(f"\nEvaluation Score: {passed}/{len(test_cases)} passed")
