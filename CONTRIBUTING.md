# Contributing to PyTradingView

First off, thank you for considering contributing to PyTradingView! It's people like you that make PyTradingView such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
  - [Development Environment Setup](#development-environment-setup)
  - [Project Structure](#project-structure)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Guidelines](#development-guidelines)
  - [Code Style](#code-style)
  - [Commit Messages](#commit-messages)
  - [Testing](#testing)
  - [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- **Be Respectful**: Treat everyone with respect and consideration
- **Be Collaborative**: Work together and help each other
- **Be Inclusive**: Welcome newcomers and diverse perspectives
- **Be Professional**: Focus on constructive feedback

## Getting Started

### Development Environment Setup

#### 1. Fork and Clone the Repository

```bash
# Fork the repository on GitHub first, then clone your fork
git clone https://github.com/great-bounty/pytradingview.git
cd pytradingview

# Add upstream remote
git remote add upstream https://github.com/great-bounty/pytradingview.git
```

#### 2. Create a Virtual Environment

```bash
# Using venv (Python 3.8+)
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### 3. Install Development Dependencies

```bash
# Install the package in editable mode with dev dependencies
pip install -e ".[dev]"

# Or install from requirements files
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

#### 4. Verify Installation

```bash
# Run tests to verify everything is working
pytest tests/

# Check code formatting
black --check pytradingview/

# Run linter
ruff check pytradingview/

# Type checking
mypy pytradingview/
```

### Project Structure

```
pytradingview/
├── core/                 # Core widget and chart APIs
│   ├── TVWidget.py      # Main widget controller
│   ├── TVChart.py       # Chart API interface
│   ├── TVBridge.py      # Python-JavaScript bridge
│   └── ...
├── datafeed/            # Datafeed interfaces and implementations
│   ├── TVDatafeed.py    # Base datafeed class
│   ├── TVSymbolInfo.py  # Symbol information structures
│   └── ...
├── indicators/          # Indicator engine and base classes
│   ├── engine/          # Modular engine components
│   ├── indicator_base.py
│   ├── indicator_config.py
│   └── indicator_engine.py
├── shapes/              # Drawing shapes (100+ types)
│   ├── TVTrendLine.py
│   ├── TVArrow*.py
│   └── ...
├── models/              # Data models
├── server/              # Web server
├── trading/             # Trading interface
├── ui/                  # UI components
└── utils/               # Utility functions

examples/                # Example code
├── indicators/          # Example indicators
│   └── false_breakout_indicator.py
└── example.py          # Basic usage example

tests/                   # Test files
docs/                    # Documentation
```

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

**Bug Report Template:**

```markdown
**Description**
A clear and concise description of the bug.

**To Reproduce**
Steps to reproduce the behavior:
1. Initialize engine with '...'
2. Call method '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment:**
- OS: [e.g., macOS 13.0, Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.10.5]
- PyTradingView Version: [e.g., 1.0.0]
- TradingView Library Version: [if applicable]

**Code Sample**
```python
# Minimal code to reproduce the issue
from pytradingview import TVEngine
# ...
```

**Error Messages**
```
Full error traceback here
```

**Additional Context**
Any other relevant information.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

**Enhancement Template:**

```markdown
**Feature Description**
Clear description of the feature.

**Use Case**
Why would this feature be useful? What problem does it solve?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Other approaches you've considered.

**Additional Context**
Screenshots, mockups, or examples.
```

### Pull Requests

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make Your Changes**
   - Write clean, documented code
   - Follow the code style guidelines
   - Add tests for new features
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   # Run all tests
   pytest tests/
   
   # Run specific test file
   pytest tests/test_your_feature.py
   
   # Run with coverage
   pytest --cov=pytradingview tests/
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template
   - Wait for review

**Pull Request Template:**

```markdown
**Description**
Brief description of changes.

**Type of Change**
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

**Testing**
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Manual testing performed

**Checklist**
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added to complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added and passing
- [ ] Dependent changes merged
```

## Development Guidelines

### Code Style

We follow **PEP 8** and use automated tools to enforce consistency.

#### Python Code Standards

```python
# Good: Clear, documented, type-hinted
from typing import Optional, List
import pandas as pd

def calculate_indicator(
    df: pd.DataFrame,
    period: int = 14,
    smoothing: Optional[str] = None
) -> List[float]:
    """Calculate custom indicator values.
    
    Args:
        df: DataFrame containing OHLC data
        period: Lookback period for calculation
        smoothing: Optional smoothing method
        
    Returns:
        List of calculated indicator values
        
    Raises:
        ValueError: If period is less than 1
    """
    if period < 1:
        raise ValueError("Period must be positive")
    
    # Implementation here
    result = []
    return result
```

#### Formatting Tools

```bash
# Format code with Black
black pytradingview/

# Check formatting
black --check pytradingview/

# Sort imports
isort pytradingview/
```

#### Linting

```bash
# Run Ruff linter
ruff check pytradingview/

# Fix auto-fixable issues
ruff check --fix pytradingview/
```

#### Type Checking

```bash
# Run MyPy type checker
mypy pytradingview/
```

### Code Quality Requirements

1. **Type Hints**: All function signatures must have type hints
2. **Docstrings**: All public functions/classes must have docstrings
3. **Comments**: Use English for all comments and logs (as per project standard)
4. **Line Length**: Maximum 100 characters (configured in pyproject.toml)
5. **Imports**: Organized and sorted (stdlib, third-party, local)

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

#### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Build process or auxiliary tool changes
- `ci`: CI/CD changes

#### Examples

```bash
# Feature
git commit -m "feat(indicators): add RSI indicator implementation"

# Bug fix
git commit -m "fix(datafeed): resolve timezone conversion issue"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Multiple paragraphs
git commit -m "refactor(engine): improve indicator loading performance

- Implement lazy loading for indicators
- Add caching mechanism
- Reduce startup time by 40%

Closes #123"
```

### Testing

#### Writing Tests

```python
# tests/test_indicator.py
import pytest
from pytradingview.indicators import TVIndicator, IndicatorConfig

def test_indicator_initialization():
    """Test indicator can be initialized correctly."""
    # Arrange
    indicator = MyIndicator()
    
    # Act
    config = indicator.get_config()
    
    # Assert
    assert config.name == "My Indicator"
    assert config.version == "1.0.0"

@pytest.mark.asyncio
async def test_async_method():
    """Test async indicator methods."""
    indicator = MyIndicator()
    result = await indicator.calculate(sample_data)
    assert len(result) > 0
```

#### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_indicator.py

# Run specific test
pytest tests/test_indicator.py::test_indicator_initialization

# Run with coverage
pytest --cov=pytradingview --cov-report=html

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

#### Test Coverage

- Aim for **80%+ code coverage**
- All new features must include tests
- Bug fixes should include regression tests

### Documentation

#### Code Documentation

```python
class MyClass:
    """Brief description of the class.
    
    Longer description explaining the purpose and usage.
    This can span multiple lines.
    
    Attributes:
        attribute1: Description of attribute1
        attribute2: Description of attribute2
        
    Example:
        >>> obj = MyClass()
        >>> obj.method()
        'result'
    """
    
    def method(self, param: str) -> str:
        """Brief description of method.
        
        Args:
            param: Description of parameter
            
        Returns:
            Description of return value
            
        Raises:
            ValueError: When param is invalid
        """
        pass
```

#### Documentation Updates

When adding features:
1. Update relevant docstrings
2. Add examples if helpful
3. Update README.md if it's a major feature
4. Add entry to CHANGELOG.md

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and general discussions
- **Pull Requests**: Code contributions

### Getting Help

- Check existing documentation
- Search closed issues
- Ask in GitHub Discussions
- Provide minimal reproducible examples

### Recognition

Contributors will be recognized in:
- Project README
- Release notes
- Git commit history

## Thank You!

Your contributions to open source make projects like this possible. We appreciate your time and effort! 🎉

---

**Questions?** Feel free to open an issue or discussion on GitHub.

**Happy Coding!** 🚀
