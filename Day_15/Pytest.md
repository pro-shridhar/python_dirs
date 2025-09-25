## FIXTURES
 pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite. Any test that wants to use a fixture must explicitly use this fixture function as an argument to the test function, so dependencies are always stated up front:

## When to not use Fixture
 they aren’t always as good for tests that require slight variations in the data.

## Marks: Categorizing Tests
  pytest enables you to define categories for your tests and provides options for including or excluding categories when you run your suite. You can mark a test with any number of categories.

## Syntax
  @pytest.mark.<name you want to provide>

  When the time comes to run your tests, you can still run them all by default with the pytest command. If you’d like to run only those tests that require database access, then you can use pytest -m database_access. To run all tests except those that require database access, you can use pytest -m "not database_access". You can even use an autouse fixture to limit database access to those tests marked with database_access.

## Parametrization: Combining Tests
  parametrize a single test definition, and pytest will create variants of the test for you with the parameters you specify.

  @pytest.mark.parametrize() to fill in this shape with different values, reducing your test code significantly:

## Durations Reports: Fighting Slow Tests
  If you want to improve the speed of your tests, then it’s useful to know which tests might offer the biggest improvements. pytest can automatically record test durations for you and report the top offenders.

## Syntax
   pytest --durations

## pytest-randomly
  pytest-randomly forces your tests to run in a random order. pytest always collects all the tests it can find before running them. pytest-randomly just shuffles that list of tests before execution.
  
## Command to run unittest 
 python -m unittest discover

## Command to run pytest
 pytest