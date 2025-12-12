# Contributing to Entity

Thank you for your interest in contributing to Entity! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your environment (OS, Python version, etc.)
- Relevant logs or screenshots

### Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature has already been requested
- Provide a clear use case
- Explain how it aligns with Entity's vision
- Consider implementation complexity

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python entity.py  # Test core
   python database.py  # Test database
   ```

5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description"
   ```

6. **Push and create a PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📝 Code Style

### Python
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and small

### JavaScript
- Use modern ES6+ syntax
- Use meaningful variable names
- Add comments for complex logic
- Follow the existing formatting

### CSS
- Use CSS custom properties (variables)
- Maintain the existing naming conventions
- Keep selectors specific but not overly nested

## 🧪 Testing

Currently, Entity uses manual testing. If you add automated tests:
- Use pytest for Python
- Use Jest for JavaScript
- Ensure all tests pass before submitting PR

## 🏗️ Architecture Guidelines

When adding new features:

### For Cortex Extensions
- Add new cortex methods in `entity.py`
- Update the routing logic in `_route_to_cortex()`
- Ensure voice unification is applied
- Add fallback handling

### For API Endpoints
- Add routes in `api.py`
- Include authentication where needed
- Validate input with Pydantic models
- Handle errors gracefully
- Update API documentation

### For Frontend Features
- Maintain the glassmorphic design language
- Ensure mobile responsiveness
- Add loading states for async operations
- Follow the existing animation patterns

## 🔒 Security

- Never commit API keys or secrets
- Use environment variables for configuration
- Validate and sanitize all user input
- Follow OWASP guidelines for web security
- Report security issues privately to maintainers

## 📚 Documentation

- Update README.md for major features
- Add inline comments for complex code
- Update SETUP.md if installation changes
- Keep the API documentation current

## 🎯 Priority Areas

We especially welcome contributions in:

1. **Testing**: Automated tests for core functionality
2. **Performance**: Optimizations for large-scale deployments
3. **Accessibility**: ARIA labels and keyboard navigation
4. **Internationalization**: Multi-language support
5. **Mobile**: Enhanced mobile experience
6. **Cortex Extensions**: New AI model integrations

## 💬 Communication

- Be respectful and constructive
- Ask questions if anything is unclear
- Provide context in discussions
- Be patient with review feedback

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

All contributors will be acknowledged in the project README and release notes.

---

Thank you for helping make Entity better! 🧠✨
