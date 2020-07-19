# pdf_splitmer.py

import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

# splits pdf into individual pages
def splitter(path):
  # fname = os.path.splitext(os.path.basename(path))[0]
  pdf = PdfFileReader(path)
  # print("# of pages before splitting: " + str(pdf.getNumPages()))
  for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(page))

    output_filename = 'page_{}.pdf'.format(page + 1)

    with open(output_filename, 'wb') as out:
      pdf_writer.write(out)

# merges a list of pdfs into one
def merger(output_path, input_paths):
  pdf_merger = PdfFileMerger()

  for path in input_paths:
    pdf_merger.append(path)
  
  with open(output_path, 'wb') as fileobj:
    pdf_merger.write(fileobj)

if __name__ == '__main__':
  # read in .pdf and .txt location and store in a list
  #                0              1               2
  # arg lists: [PDF.pdf] [Ch_break_down.txt] [PAGE-OFFSET]
  cmnd_line_arg_list = []
  for arg in sys.argv[1:]:
    cmnd_line_arg_list.append(arg)
  
  # step 1: split pdf
  # it works!
  print("Splitting pdf . . .")
  splitter(cmnd_line_arg_list[0])
  print("Splitting complete")

  # step 2: open text file and start creating seperate pdfs for each ch
  print("Reading ", cmnd_line_arg_list[1], " . . . ")
  txt_file = open(cmnd_line_arg_list[1], 'r')
  line_list = [()]
  for line in txt_file:
    #                        0    1        2           3
    # items in line_list[0]: CH, CH-TITLE, PAGE-START, PAGE-END (strings)
    line_list[0] = line.split()
    paths = []
    ch = int(line_list[0][0])
    ch_title = line_list[0][1]
    start_page = int(line_list[0][2])
    end_page = int(line_list[0][3])
    page_offset = int(cmnd_line_arg_list[-1])

    while start_page <= end_page:
      paths.append('page_{}.pdf'.format(start_page + page_offset))
      start_page += 1
    
    print("Merging CH{}".format(ch))
    merger('CH{}_{}.pdf'.format(ch,ch_title), paths)
    print("Merge Complete")