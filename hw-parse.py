#!/opt/homebrew/bin/python3
import argparse
from PyPDF2 import PdfFileReader
import datetime as dt

def add_preamble(output, class_name, hw_num, date):
  output += '\input{../../preamble.tex}\n'
  output += '\\title{' + f'{class_name}'.title() + ' - Homework' + f' {hw_num}' + '}\n'
  output += f'\\date{{{date}}}\n'
  output += '\\author{Jonathan Carlson}\n'
  output += "\n\\begin{document}\n"
  output += "\\maketitle\n\n"
  return output

parser = argparse.ArgumentParser(description='Create TeX from HW spec')
parser.add_argument('hw_pdf', type=str, help='Path to HW pdf')
parser.add_argument('class_name', type=str, help='The class the HW is for')
# source for how to have bool arg
# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
parser.add_argument('--verbose', '-v', dest='verbose', action='store_true',  help='Print out finalized output')
parser.set_defaults(verbose=False)
args = parser.parse_args()

class_name = args.class_name
filename = args.hw_pdf

content = ''
# help with PyPDF2 - https://stackoverflow.com/questions/55991402/valueerror-seek-of-closed-file-working-on-pypdf2-and-getting-this-error
with open(filename, 'rb') as f:
  pdf = PdfFileReader(f)
  # FIXME: assuming hw is only one page long
  page = pdf.getPage(0)
  content = page.extractText()

content = content.split('\n')

hw_num = [c for c in filename if c.isnumeric()][0]
output_filename = f'{class_name}_hw{hw_num}.tex'
output = ''

section_problems = {}
date = ''

for line in content:
  if "Due" in line:
    # remove Duedate
    date = line.split('date')[1]
    # TODO: use Todoist/task warrior api to add as hw
    month_day, time =  date.split('at')
    # drop rd, th, nd from date (3rd, 4th, 2nd)
    month_day = month_day[:-2]
    month_day_dt = dt.datetime.strptime(month_day, "%B%d")
    # change year to current year
    current_year = int(dt.datetime.today().strftime("%Y"))
    month_day_dt = month_day_dt.replace(year=current_year)
    date = month_day_dt.strftime('%B %d, %Y')
    # now that we have date, we can add our preamble
    output = add_preamble(output, class_name=class_name, hw_num=hw_num, date=date)
  section_in_line = None
  if "Section" in line:
    # remove section
    sec_line = line[len('Section'):]
    section_in_line, sec_line = sec_line.split(':')
    section_problems[section_in_line] = []
    if "Problems" in sec_line:
      # remove problems
      problems = sec_line[len('Problems'):]
      problems = problems.split(',')
      for problem in problems:
        if "and" in problem:
          # remove and and ending period
          problem = problem[len('and'):-1]
        section_problems[section_in_line].append(problem)
    else:
     continue

for sec in section_problems.keys():
  output += '\section*{Section' + f' {sec}' + '}\n'
  for prob in section_problems[sec]:
    output += f'\problem{{{sec}}}{{{prob}}}\n'
output += '\n\\end{document}'
if args.verbose:
  print(output)
with open(output_filename, 'w') as f:
  f.write(output)