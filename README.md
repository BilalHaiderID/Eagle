# Eagle 🦅

A Multi-Functional Toolkit for Hackers and Programmers in Python including Information Gathering, Brute Force Attacks, Social Media Toolkit, and Phishing tools - Open Source.

**Current Version:** 0.0.6

## Features

- **Temporary Email**: Create and listen to temporary email addresses
- **Search Query**: Search across Google, Wikipedia, and DuckDuckGo
- **IBAN Validation**: Validate International Bank Account Numbers
- **Email Validation**: Verify email addresses
- **IP Information**: Gather information about IP addresses
- **Phone Information**: Get details about phone numbers
- **Fake Profile Generation**: Generate fake profile information for testing
- **Facebook Token Generation**: Extract Facebook access tokens

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/BilalHaiderID/Eagle.git
cd Eagle
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure API keys:
```bash
cp .env.example .env
# Edit .env and add your API keys:
# - VERIPHONE_APKKEY (from https://www.veriphone.io)
# - ABSTRACT_EMAIL_APIKEY (from https://www.abstractapi.com)
# - ABSTRACT_IBAN_APIKEY (from https://www.abstractapi.com)
```

4. Make the script executable:
```bash
chmod +x eagle
```

5. Run the application:
```bash
python3 eagle
```

## Usage

Run the script and select from the menu:

```
[01] Temporary Email
[02] Search Query [Google, Wikipedia, DuckDuckGo]
[03] IBAN Validation
[04] Email Validation
[05] IP Information Gathering
[06] Phone Number Information Gathering
[07] Fake Profile Information
[08] Facebook Token Generation
[00] Exit
```

## Security

⚠️ **IMPORTANT SECURITY NOTES:**

- **Never commit API keys to the repository.** Use `.env` files instead.
- Always use environment variables for sensitive configuration.
- The `.env` file is excluded from version control (see `.gitignore`).
- Use `.env.example` as a template for required variables.
- Rotate API keys if they are ever exposed.

## Configuration

All API keys and settings are managed through environment variables in the `.env` file.

### Required Environment Variables

```
VERIPHONE_APKKEY=your_api_key
ABSTRACT_EMAIL_APIKEY=your_api_key
ABSTRACT_IBAN_APIKEY=your_api_key
DISPLAY_COLOR=green  # Optional: green, red, white, blue, or empty
```

## Improvements in v0.0.6

- ✅ Removed hardcoded API keys
- ✅ Added environment variable support
- ✅ Improved error handling with logging
- ✅ Fixed security vulnerabilities
- ✅ Better input validation
- ✅ Replaced unsafe `os.system()` with `subprocess`
- ✅ Added proper timeout handling for requests
- ✅ Fixed typos and code quality issues
- ✅ Added configuration validation
- ✅ Improved user experience with menu system

## File Structure

```
Eagle/
├── eagle              # Main Python script
├── requirements.txt   # Python dependencies
├── .env.example      # Example environment configuration
├── .env              # Your local configuration (NOT committed)
├── .gitignore        # Git ignore file
├── install.sh        # Installation script
├── LICENSE           # MIT License
└── README.md         # This file
```

## License

MIT License - See LICENSE file for details

## Author

Created by [@bilalhaiderid](https://github.com/BilalHaiderID)

## Disclaimer

This tool is provided for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. Users are responsible for ensuring they have proper authorization before using this toolkit.

## Contributing

Feel free to submit issues and enhancement requests!

## Support

For issues and questions, please open an issue on GitHub.