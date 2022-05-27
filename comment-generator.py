#!/bin/python3
import pyperclip as pc
import argparse

def get_comment(comment_start, comment_end, sep = '=', comment = None, size = None, only_sep = False):
	# First line
	new_comment = f"{comment_start}"
	for i in range(size):
		new_comment += sep
	new_comment += f"{comment_end}\n"

	if only_sep == True:
		return new_comment

	# Second line
	new_comment += f"{comment_start}"
	for i in range(int((size - len(comment) - len(comment_start))/2)):
		new_comment += sep
	new_comment += f" {comment} "
	for i in range(int((size - len(comment) - len(comment_start))/2)):
		new_comment += sep
	new_comment += f"{comment_end}\n"
	
	# Third line
	new_comment += f"{comment_start}"
	for i in range(size):
		new_comment += sep
	new_comment += f"{comment_end}\n"
	return new_comment


languages_supported = ['c', 'c++', 'python']

parser = argparse.ArgumentParser(description='Script to generate automatic comments')
parser.add_argument('comment', type=str, nargs='*')
parser.add_argument('-l', '--language', type=str, help='Language in which generate comments. Available: {}'.format(', '.join(languages_supported)), default='c')
parser.add_argument('-s', '--size', type=int, help='Comment size')
parser.add_argument('-w', '--wide', help='Wide comment', action='store_true')
parser.add_argument('--sep', help="Print separator", action='store_true')
args = parser.parse_args()

comment_start = None
comment_end = None
size = None
comment = None
only_sep = False

if args.language == 'c' or args.language == 'c++':
	comment_start = "/*"
	comment_end = "*/"
elif args.language == 'python':
	comment_start = comment_end = "#"

if args.sep == True:
	comment = '-'
	only_sep = True
	args.wide = True
else:
	comment = ' '.join(args.comment)

if args.size != None:
	size = args.size
elif args.wide == True:
	size = 74
else:
	size = len(comment) + 6
	

new_comm = get_comment(comment_start = comment_start, comment_end = comment_end, comment = comment, size = size, only_sep = only_sep)
print(new_comm)
pc.copy(new_comm)
print("Comment copyed to the clipboard")