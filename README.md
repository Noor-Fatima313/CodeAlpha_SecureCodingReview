# Secure Coding Review

## Objective
Perform a security audit of a Python Flask application.

## Tools Used
- Python
- Flask
- Bandit Static Analyzer
- Visual Studio Code

## Vulnerabilities Identified
1. Hardcoded Credentials
2. Plain Text Password Storage
3. Missing Input Validation
4. Debug Mode Enabled
5. Lack of Authentication Controls

## Security Recommendations
- Use environment variables
- Hash passwords
- Validate user input
- Disable debug mode
- Apply authentication and authorization
