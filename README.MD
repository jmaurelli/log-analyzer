# Log Analyzer

A modular tool for analyzing log files and generating detailed reports.

## Installation

```bash
pip install -e .


Usage
Basic Usage
log-analyzer analyze /path/to/logs --workers 4 --output report.json


Command Options
Usage: log-analyzer analyze [OPTIONS] LOG_PATH

Options:
  -w, --workers INTEGER     Number of worker threads [default: 4]
  -o, --output TEXT        Output file name [default: analysis_report.json]
  -f, --min-frequency INTEGER  Minimum frequency to include in report [default: 1]
  --help                   Show this message and exit
  
  
Input Formats
The analyzer supports:

Single log file: log-analyzer analyze app.log
Directory of logs: log-analyzer analyze /var/logs/
Multiple log formats: .log, .txt, etc.
Output Format
The analyzer generates a JSON report with the following structure:
{
  "summary": {
    "total_files": 1,
    "total_lines": 1000,
    "total_unique_lines": 800,
    "total_repeated_lines": 200,
    "unique_pids": 5,
    "unique_threads": 10,
    "unique_functions": 20,
    "total_errors": 50,
    "total_warnings": 100
  },
  "files": [
    {
      "filename": "app.log",
      "file_size": 1024,
      "line_count": 1000,
      "patterns": {
        "errors": [...],
        "warnings": [...],
        "info": [...]
      }
    }
  ]
}


Examples
Analyze a single log file:
log-analyzer analyze app.log


Analyze multiple logs with 8 worker threads:
log-analyzer analyze /var/logs/ -w 8


Custom output location:
log-analyzer analyze app.log -o custom_report.json


Filter by minimum frequency:
log-analyzer analyze app.log -f 5  # Only show patterns occurring 5+ times


Pattern Recognition
The analyzer automatically identifies:

Error and warning patterns
Process IDs (PIDs)
Thread IDs
Function names
Repeated log patterns



Performance Tips
# For 8-core CPU
log-analyzer analyze large_logs/ -w 8

For large log files
# Increase minimum frequency to reduce output size
log-analyzer analyze huge.log -f 10


Module Structure
core/: Core analysis functionality
utils/: Utility functions and patterns
cli/: Command-line interface


