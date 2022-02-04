# hw-parse
- `hw-parse` is used to parse hw specs to TeX
- it's not dynamic and expects a certain format

## Installation
- Clone the repo
- run `pip install -r requirements.txt`
    - we need [PyPDF2](https://pythonhosted.org/PyPDF2/)

## Usage
- Assuming `hw-parse` is not in your `$PATH`:
    - `./hw-parse [-h] [--verbose] [--dry-run] hw_pdf class_name`
- You can always run `./hw-parse --help` to determine usage.
