#!/usr/bin/env python3
import sys
import time
import importlib.util
from pathlib import Path

GREEN  = "\033[32m"
RED    = "\033[31m"
YELLOW = "\033[33m"
GRAY   = "\033[90m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def load_module(filepath: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    mod  = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"{RED}  ERROR loading {filepath.name}: {e}{RESET}")
        sys.exit(1)
    return mod


def find_solution(exercise_dir: Path, fn_name: str) -> Path:
    candidates = [
        p for p in exercise_dir.glob("*.py")
        if p.name != "tests.py"
    ]
    for p in candidates:
        if p.stem == fn_name:
            return p
    for p in candidates:
        if f"def {fn_name}" in p.read_text():
            return p
    return None


def run_exercise(exercise_dir: Path):
    exercise_dir = Path(exercise_dir)
    tests_path   = exercise_dir / "tests.py"

    if not tests_path.exists():
        print(f"{RED}  ERROR: missing tests.py in {exercise_dir}{RESET}")
        sys.exit(1)

    tests_mod = load_module(tests_path, "tests")

    if not hasattr(tests_mod, "FUNCTION"):
        print(f"{RED}  ERROR: tests.py must define FUNCTION{RESET}")
        sys.exit(1)
    if not hasattr(tests_mod, "TESTS"):
        print(f"{RED}  ERROR: tests.py must define TESTS{RESET}")
        sys.exit(1)

    fn_name = tests_mod.FUNCTION
    tests   = tests_mod.TESTS

    solution_path = find_solution(exercise_dir, fn_name)
    if solution_path is None:
        print(f"{RED}  ERROR: no .py file found containing 'def {fn_name}' in {exercise_dir}{RESET}")
        sys.exit(1)

    solution_mod = load_module(solution_path, fn_name)

    if not hasattr(solution_mod, fn_name):
        print(f"{RED}  ERROR: no function '{fn_name}' found in {solution_path.name}{RESET}")
        sys.exit(1)

    fn = getattr(solution_mod, fn_name)

    print(f"{GRAY}> building source...{RESET}")
    print(f"{GRAY}> executing {len(tests)} tests...{RESET}")

    passed = 0
    for i, (args, expected) in enumerate(tests):
        label = f"test_{i:02d}"
        start = time.time()
        try:
            result  = fn(*args)
            elapsed = int((time.time() - start) * 1000)
            if result == expected:
                print(f"{GREEN}{BOLD}{label} [PASS]{RESET} {GRAY}{elapsed}ms{RESET}")
                passed += 1
            else:
                print(f"{RED}{BOLD}{label} [FAIL]{RESET} {GRAY}{elapsed}ms{RESET}")
                print(f"{GRAY}         input:    {list(args)}{RESET}")
                print(f"{GRAY}         expected: {expected}{RESET}")
                print(f"{RED}         got:      {result}{RESET}")
        except Exception as e:
            elapsed = int((time.time() - start) * 1000)
            print(f"{YELLOW}{BOLD}{label} [ERROR]{RESET} {GRAY}{elapsed}ms — {e}{RESET}")

    total = len(tests)
    if passed == total:
        print(f"\n{GREEN}{BOLD}> {passed}/{total} tests passed ✓{RESET}")
    else:
        print(f"\n{RED}{BOLD}> {passed}/{total} tests passed{RESET}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 engine.py <path/to/exercise>")
        sys.exit(1)
    run_exercise(Path(sys.argv[1]))