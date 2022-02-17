# hw-parse
- `hw-parse` is used to parse hw specs to TeX
- it's not dynamic and expects a certain format

## Installation
- Clone the repo
- run `pip install -r requirements.txt`
    - we need [pdfminer.six](https://github.com/pdfminer/pdfminer.six) and [python-dotenv](https://github.com/theskumar/python-dotenv)

## Usage
- Assuming `hw-parse` is not in your `$PATH`:
    - `./hw-parse [-h] [--verbose] [--dry-run] hw_pdf class_name`
- You can always run `./hw-parse --help` to determine usage.
- Store environement variables like the location to your preamble path and the author name in a .env file as follows:
    - `PREAMBLE_PATH='path/to/preamble'`
    - `AUTHOR_NAME='First Last'`
    - There's a sample .env in [.env](.env)
    - note that it's best practice to add .env to your gitignore but in our case the env variables are not important secrets so it's probably ok to commit them
