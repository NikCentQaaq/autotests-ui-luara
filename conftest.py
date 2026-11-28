import pytest

pytest_plugins = (
    'fixtures.pages',
    'fixtures.browsers',
    'fixtures.page_states'
)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)