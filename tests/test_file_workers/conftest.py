import pytest

count = 0
@pytest.fixture(autouse=True)
def clean_test_file():
    global count
    with open("tests/testfile.txt", 'w'):
        pass
    print(count)
    count += 1