# TODO
## env setup
- make preamble.tex an environemnt variable
- use a .env and [python-dotenv](https://pypi.org/project/python-dotenv/) for env variables such as path to preamble, name of author, etc
## brew setup
- have installation be via `brew tap` instead of clone
## pdf parsing
- use [pdfminer.six](https://github.com/pdfminer/pdfminer.six) instead of `PyPDF2` as it can maintain spaces and other formatting when parsing pdfs
