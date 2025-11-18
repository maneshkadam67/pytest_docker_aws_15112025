import pytest


@pytest.fixture(scope="function",autouse=True)
def setup():
    print("before execution of testcase...................before execution of testcase")
    yield
    print("after execution of testcase...................after execution of testcase")