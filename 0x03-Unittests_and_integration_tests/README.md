# 0x03. Unittests and Integration Tests

## Overview
The project "0x03. Unittests and Integration Tests" focuses on unit testing and integration testing for the back-end code. The main goal is to ensure that functions and code paths return expected results for different inputs and scenarios. We will use the Python `unittest` framework and `unittest.mock` library to perform the tests and mock external calls such as HTTP requests and database I/O.

## UnitTests
Unit testing is the process of testing a specific function's behavior with various inputs, including standard inputs and corner cases. The primary focus of unit tests is to check the logic defined inside the tested function independently. If necessary, additional functions should be mocked, especially for network or database calls.

## Integration Tests
Integration tests aim to test the flow of the code end-to-end, verifying interactions between various parts of the code. For integration tests, low-level functions that make external calls (HTTP requests, file I/O, database I/O, etc.) should be mocked to avoid making actual external calls during testing.

## Learning Objectives
By the end of this project, you will be able to:

- Differentiate between unit and integration tests.
- Apply common testing patterns like mocking, parametrizations, and fixtures.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Code should adhere to the `pycodestyle` style (version 2.5).
- All files must be executable.
- All modules, classes, and functions should have proper documentation.
- Functions and coroutines must be type-annotated.

## Resources
Read or watch:

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/41504187/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)

## Tasks
### 0. Parameterize a unit test
In this task, we will write the first unit test for the `utils.access_nested_map` function. We will create a `TestAccessNestedMap` class that inherits from `unittest.TestCase` and implement the `TestAccessNestedMap.test_access_nested_map` method to test the function for specific inputs.

The method should be decorated with `@parameterized.expand` to test the function for the following inputs:

- `nested_map={"a": 1}, path=("a",)`
- `nested_map={"a": {"b": 2}}, path=("a",)`
- `nested_map={"a": {"b": 2}}, path=("a", "b")`

For each of these inputs, test with `assertEqual` that the function returns the expected result.

### 1. Parameterize a unit test
In this task, we will implement the `TestAccessNestedMap.test_access_nested_map_exception` method to test that a `KeyError` is raised for specific inputs. We will use `@parameterized.expand` to test the function for the following inputs:

- `nested_map={}, path=("a",)`
- `nested_map={"a": 1}, path=("a", "b")`

Additionally, we will ensure that the exception message is as expected.

### 2. Mock HTTP calls
In this task, we will test the `utils.get_json` function without making actual external HTTP calls. We will use `unittest.mock.patch` to mock `requests.get` and return a known payload. The method will be parametrized with different `test_url` and `test_payload` inputs to test the function for different scenarios.

### 3. Parameterize and patch
This task involves testing the memoization functionality provided by the `utils.memoize` decorator. We will use `unittest.mock.patch` to mock the underlying method and check that it is only called once when calling the memoized property twice.

### 4. Parameterize and patch as decorators
In this task, we will use `@patch` as a decorator to mock the `get_json` method of the `client.GithubOrgClient` class. We will also use `@parameterized.expand` to parametrize the test with different `org` examples and ensure no external HTTP calls are made.

### 5. Mocking a property
In this task, we will test the `GithubOrgClient._public_repos_url` method by mocking the `GithubOrgClient.org` property and returning a known payload. We will then test that the result of `_public_repos_url` is the expected one based on the mocked payload.

### 6. More patching
This task involves testing the `GithubOrgClient.public_repos` method. We will use `@patch` as a decorator to mock `get_json` and `GithubOrgClient._public_repos_url`. We will then test that the list of repos is as expected and that the mocked property and `get_json` are called once.

### 7. Parameterize
In this task, we will test the `GithubOrgClient.has_license` method. We will parametrize the test with different `repo` inputs and the expected returned value.

### 8. Integration test: fixtures
This task involves creating an integration test for the `GithubOrgClient.public_repos` method. We will use fixtures to mock external requests and ensure that the method returns the expected results.

### 9. Integration tests (Advanced)
In this advanced task, we will create an integration test for the `GithubOrgClient.public_repos` method, including additional tests with a specific license. We will use fixtures to mock external requests and ensure the method behaves as expected.

---

*This project is part of the back-end Python curriculum for ALX.*
