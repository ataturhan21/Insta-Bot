# InstaBot

A Streamlit interface for a Selenium-based Instagram automation experiment. This repository is a fork of [TOBB ETÜ CS Community's Social Master](https://github.com/TOBB-ETU-CS-Community/Social-Master).

## Implemented workflows

- Follow accounts from another account's followers list.
- Like and comment on posts found through hashtags.
- Unfollow accounts from the signed-in account's following list.

These workflows interact with Instagram through a browser session. They depend on the page structure and selectors implemented in [`insta_bot/app.py`](insta_bot/app.py).

## Local setup

The original setup uses Python 3.10.10 and Poetry 1.4.0. The dependency constraints and lockfile are preserved.

```bash
git clone https://github.com/ataturhan21/Insta-Bot.git
cd Insta-Bot
poetry install --no-root
poetry run streamlit run "insta_bot/app.py"
```

Run from the repository root so the `static/` images resolve. On Windows, use [`start.bat`](start.bat).

### Browser requirements

Install a Chrome or Chromium browser compatible with the selected ChromeDriver. The current implementation obtains its driver from `chromedriver_py.binary_path`, and the dependency file records the ChromeDriver 115 package line. [`packages.txt`](packages.txt) lists Chromium system packages for hosted Linux environments, but the Python code still controls which driver is launched.

Review the browser/driver combination and selectors before starting a live session. A documentation update does not verify compatibility with the current Instagram website.

## Operation

1. Start the local UI and enter the account credentials in the sidebar. The password field is masked.
2. Choose the browser options and select **Login Account**.
3. Select **Follow**, **Like & Comment**, or **Unfollow** and configure its inputs.
4. Use **Start the automation** to initiate the selected operation.

A successful login and a button click can cause real account changes. The project does not include a dry-run mode; inspect the requested operation before starting it.

## Project map

| Path                                                       | Purpose                                                           |
| ---------------------------------------------------------- | ----------------------------------------------------------------- |
| [`insta_bot/app.py`](insta_bot/app.py)                     | Selenium page interactions, session state, and Streamlit controls |
| [`insta_bot/modules/utils.py`](insta_bot/modules/utils.py) | Page setup and styling                                            |
| [`static/`](static/)                                       | Background assets                                                 |
| [`pyproject.toml`](pyproject.toml)                         | Python and browser-automation dependencies                        |

## License

[GNU General Public License v3.0](LICENSE). Upstream attribution is preserved.

## Offline operation checks

Run `poetry run python -m unittest discover -s tests -v`. The tests use fake
page actions and do not log in or contact Instagram. Follow and unfollow execute
1 requested batch and report its actual count; empty or partial batches are not
retried automatically against a dialog that the action already closed.
