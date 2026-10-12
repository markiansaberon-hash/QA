# Python with pytest

Notes and practice tests from learning pytest: BDD, fixtures, parametrization, marks and API testing. The API tests run against the public demo API at https://api.qaautomationlabs.com.

## Setup

From the repo root (`QA/`):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r "Python with pytest/requirements.txt"
```

On later runs, only `source venv/bin/activate` is needed.

## Running the tests

From inside `Python with pytest/`:

```bash
pytest                                    # everything
pytest tests/parametrization              # one folder
pytest tests/fixtures/test_format_data.py # one file
pytest -m smoke                           # only tests marked smoke
pytest -k palindrome                      # tests whose name contains "palindrome"
pytest -x                                 # stop at the first failure
```

`pytest.ini` already sets `-v -s`, so you get verbose names and `print` output by default, plus an HTML report at `reports/my_report.html`.

## Structure

| Path | What it covers |
|---|---|
| `conftest.py` | Shared fixtures: `base_url` and `auth_headers` (logs in once per run, logs out at the end) |
| `pytest.ini` | Registered marks, logging and the HTML report options |
| `tests/unittest vs pytest/` | The same tests written with `unittest` and with plain pytest `assert` |
| `tests/fixtures/` | Fixtures: `yield`, class fixtures, return values, scope, and a global fixture. `format_data.py` is the code under test |
| `tests/parametrization/` | `@pytest.mark.parametrize`: palindrome cases and registering users with different payloads |
| `tests/apiRequests/` | API tests with `requests`: GET, POST, product bulk and user registration |
| `test/BDD` | Pytest with `GIVEN, WHEN, THEN` |

## Marks

| Mark | Meaning |
|---|---|
| `smoke` | Quick basic checks |
| `slow` | Tests that take a while |
| `format` | Formatting tests |

Run a group with `pytest -m smoke`, or exclude one with `pytest -m "not slow"`.

## Notes

- API tests need internet access and use the demo account `qa@demo.io`. The credentials belong to a public demo API, so they are safe to keep in the repo.
- The access token expires after one hour, so a very long run could get 401 errors.
- Requirements are pinned in `requirements.txt` (pytest 9.1.1, requests 2.34.2, pytest-html 4.4.0).