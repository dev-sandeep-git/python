import pytest

# Example of a fixture to provide test data
@pytest.fixture
def sample_calculator():
    from calculator import Calculator  # Replace with your actual calculator class or function
    return Calculator()

# Example of a fixture for setting up a database connection
@pytest.fixture(scope="module")
def db_connection():
    # Set up the database connection (this is just an example)
    connection = create_db_connection()
    yield connection  # This will return the connection to the test functions
    connection.close()  # Clean up after tests

# Example of a fixture to create test data
@pytest.fixture
def test_data():
    return {
        "num1": 5,
        "num2": 3
    }

# Example of a fixture that could be used for cleanup after tests
@pytest.fixture(autouse=True)
def cleanup():
    # This will run automatically before and after each test
    print("Setting up test environment")
    yield
    print("Tearing down test environment")

