# Guachi - Modern Python Version

This is an upgraded version of the Guachi configuration management system.

## Modernization Steps Completed

The following upgrades have been made to bring this legacy Python 2.5 project up to modern Python standards:

1. **Python Version Upgrade**: Updated from Python 2.5 to Python 3.6+ compatibility
   - Fixed exception handling syntax (try/except)
   - Updated imports (ConfigParser → configparser)
   - Removed unicode prefixes from strings

2. **Modern Testing**:
   - Added pytest-style test files alongside the legacy unittest-style tests
   - Implemented fixtures for better test organization
   - Updated test assertions to use pytest's approach

3. **Modern Packaging**:
   - Created a pyproject.toml file for modern Python packaging
   - Updated package metadata
   - Added compatibility information for Python 3.6 through 3.12

4. **Continuous Integration**:
   - Added GitHub Actions workflows for automated testing
   - Set up multi-Python-version testing
   - Added package build and validation

## Getting Started

### Installation

```bash
pip install .
```

Or for development:

```bash
pip install -e .
```

### Running Tests

```bash
pytest
```

## Project Structure

- `guachi/`: Main package directory
  - `__init__.py`: ConfigMapper class and package imports
  - `config.py`: Configuration handling
  - `database.py`: SQLite database interface
  - `tests/`: Test files for both unittest and pytest styles

## Dependencies

This project now has minimal dependencies:
- Python 3.6+
- pytest (for testing)
