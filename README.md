# hw-parse
- `hw-parse` is used to parse hw specs to TeX
- it's not dynamic and currently expects [this kind of format](sample_formats/sample_format.pdf)
    - given that format it creates [this homework TeX file](sample_formats/101_hw1.tex)
    - the sample format pdf was created using [this sample format TeX file](sample_formats/sample_format.tex)

## Installation
- Clone the repo
- run `pip install -r requirements.txt`
    - we need [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- run `./setup.py` to create a config file which is stored by default in `$HOME/.config/hw-parse/hw-parse.cfg`
- the config has two variables:
    - `preamblepath` is the path to your LaTeX preamble which is inserted as `\input{/path/to/preamble}` in the preamble of the created TeX file
    - `authorname` is the `\author{First Last}` or author of the TeX file
- add `hw-parse` to your `$PATH` in your .zshrc/equivalent
## Usage
- Assuming `hw-parse` is not in your `$PATH`:
    - `./hw-parse [-h] [--verbose] [--dry-run] hw_pdf class_name`
- You can always run `./hw-parse --help` to determine usage.
