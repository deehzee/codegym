import json
from textwrap import indent


def run_tests(test_cases, soln_fn):
    total = len(test_cases)
    passed = 0
    indentation = ' ' * 4
    for i, case in enumerate(test_cases):
        params = case["params"]
        expected = case["expected"]
        got = soln_fn(**params)
        if got == expected:
            passed += 1
        else:
            print(f"Failed with test case [{i}]:")
            print(indent(f"params: {json.dumps(params)}", indentation))
            print(indent(f"expected: {expected}", indentation))
            print(indent(f"got: {got}", indentation))
    print(f"Passed {passed}/{total} test{'s' if passed > 1 else ''}.")
