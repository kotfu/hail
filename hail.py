#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2017 Jared Crapo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""Usage: hail [OPTION]... to-addr


  -h, --help        display this help and exit
  -s, --subject     subject for the email
  -r, --from        the from address
  -q, --plainfile   the file containing the plain email message
  -Q, --htmlfile    the file containing the html email message
  -S, --smtpserver  the smtp server to use, defaults to localhost

to-addr is the email address you want to send the message to
"""
import sys
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def main(argv=None):

	# TODO add -b for bcc-addr
	# TODO add -c for cc-addr
	parser = argparse.ArgumentParser(description='Send html emails from the command line')
	parser.add_argument('-s', '--subject', required=True, help='subject of the email')
	parser.add_argument('-r', '--from-addr', required=True, help='address to send email from')
	parser.add_argument('-q', '--plainfile', required=True, help='file containing the plain text version of the message')
	parser.add_argument('-Q', '--htmlfile', required=True, help='file containing the html version of the message')
	parser.add_argument('-S', '--smtpserver', default='localhost', help='smtp server to use, default is localhost')
	parser.add_argument('to-addr', nargs='+', help='email address to send to')
	args = parser.parse_args()
	
	# open an SMTP connection
	smtp = smtplib.SMTP()
	smtp.connect(args.smtpserver)

	for to_addr in args.to_addr:

		# Create the root message and fill in the from, to, and subject headers
		msgRoot = MIMEMultipart('related')
		msgRoot['Subject'] = args.subject
		msgRoot['From'] = args.from_addr
		msgRoot['To'] = to_addr
		msgRoot.preamble = 'This is a multi-part message in MIME format.'

		# Encapsulate the plain and HTML versions of the message body in an
		# 'alternative' part, so message agents can decide which they want to display.
		msgAlternative = MIMEMultipart("alternative")
		msgRoot.attach(msgAlternative)

		# make the plain text version
		msgText = MIMEText("".join(open(plainFile).readlines()))
		msgAlternative.attach(msgText)

		# make the html version of the email
		msgText = MIMEText("".join(open(htmlFile).readlines()), "html")
		msgAlternative.attach(msgText)

		# send the email
		smtp.sendmail(args.from_addr, to_addr, msgRoot.as_string())

	# all done sending, clean up
	smtp.quit()

if __name__ == "__main__":
	sys.exit(main())