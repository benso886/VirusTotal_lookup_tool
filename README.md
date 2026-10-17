# VirusTotal Hash Lookup Tool

A simple Python command-line tool that allows users to look up file hashes using the VirusTotal API.

The program retrieves antivirus detection statistics and provides a direct link to the corresponding VirusTotal report.

This project was developed as a Python learning exercise, focusing on API integration, input validation, virtual environments, and basic programming concepts.

## Features

- Supports MD5, SHA-1, and SHA-256 file hashes.
- Validates hash formats before sending API requests.
- Retrieves antivirus detection statistics from VirusTotal.
- Displays the number of malicious detections and total analysis results.
- Generates a direct link to the VirusTotal report.
- Supports multiple hash lookups in a single session.
- Allows users to exit the program by typing `exit`.
- Uses an environment variable to keep the VirusTotal API key out of the source code.

## Requirements

- Python 3.10 or newer
- A VirusTotal API key
- Internet connection

### Python dependencies

The program uses the following Python packages:

- `requests` — Sends HTTP requests to the VirusTotal API.
- `truststore` — Enables Python to use the operating system's trusted certificate store.

The `os` module is included with Python and does not require installation.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/virustotal-hash-lookup.git
cd virustotal-hash-lookup
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install requests truststore
```

### 4. Configure the VirusTotal API key

Obtain an API key from [VirusTotal](https://www.virustotal.com/).

The program reads the API key from an environment variable named `VT_API_KEY`.

In PyCharm:

1. Open **Run → Edit Configurations**.
2. Select your Python run configuration.
3. Find **Environment variables**.
4. Add `VT_API_KEY` as the variable name and your API key as its value.
5. Save the configuration.

**Security:** Never commit your API key to GitHub or include it directly in your Python source code.

## Usage

Run the program:

```bash
python main.py
```

Enter an MD5, SHA-1, or SHA-256 hash when prompted.

Example:

```text
Enter a file hash (or type 'exit'): 44d88612fea8a8f36de82e1278abb02f

Hash type: MD5
VirusTotal detection: 5 / 72
VirusTotal report: https://www.virustotal.com/gui/file/44d88612fea8a8f36de82e1278abb02f

Enter a file hash (or type 'exit'): exit
```

*Note: The detection numbers above are illustrative and do not represent actual VirusTotal results.*

The program continues accepting hashes until the user enters `exit`.

## How It Works

1. The user enters a file hash.
2. The program validates its length and hexadecimal characters.
3. A GET request is sent to the VirusTotal API.
4. VirusTotal returns file analysis information in JSON format.
5. The program extracts the malicious detection count and total analysis results.
6. The results and VirusTotal report URL are displayed.
7. The program waits for another hash or the `exit` command.

### VirusTotal API Endpoint

The program uses the VirusTotal API v3 file information endpoint:

```text
GET https://www.virustotal.com/api/v3/files/{hash}
```

Authentication is performed using the `x-apikey` HTTP header.

## Limitations

- Requires a valid VirusTotal API key and an active internet connection.
- Subject to VirusTotal API usage limits.
- Does not currently handle HTTP errors such as `401`, `404`, or `429`.
- A valid hash format does not guarantee that VirusTotal has a report for that hash.
- The displayed detection count includes engines reporting `malicious`; the denominator includes all categories in `last_analysis_stats`, including errors and timeouts.
- VirusTotal detections should not be treated as definitive proof that a file is malicious.

## Security Considerations

- Never hardcode API keys or other credentials.
- Do not commit `.env` files containing secrets.
- Keep HTTPS certificate verification enabled.
- Avoid submitting confidential or sensitive indicators without appropriate authorization.
- Follow VirusTotal's API usage policies and rate limits.

## Future Improvements

Potential enhancements include:

- HTTP error handling.
- Support for bulk hash lookups.
- Exporting results to CSV.
- Displaying additional VirusTotal information.
- Adding a graphical user interface.
- Improving detection statistics and result formatting.

## Disclaimer

This project is intended for educational purposes and basic security research.

VirusTotal results should be interpreted in context and should not be used as the sole basis for determining whether a file is malicious.

## Acknowledgements

- [VirusTotal](https://www.virustotal.com/)
- [VirusTotal API Documentation](https://docs.virustotal.com/)
