#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2007 Jared Crapo
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
# Version 1.0
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
import getopt
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

class Usage(Exception):
	def __init__(self,msg):
		self.msg = msg

def main(argv=None):
	if argv is None:
		argv = sys.argv

	# TODO add -b for bcc-addr
	# TODO add -c for cc-addr
	shortopts = "hs:r:q:Q:S:"
	longopts = [ "help", "subject=", "from=", "plainfile=", "htmlfile=", "smtpserver=" ]
	
	# initialize
	fromAddy = None
	plainFile = None
	htmlFile = None
	toAddrs = None
	subject = None
	smtpServer = "localhost"
	
	# parse command line options
	try:
		try:
			opts, args = getopt.getopt(argv[1:], shortopts, longopts)
		except getopt.error, msg:
			raise Usage(msg)
	
		# process options
		for opt, parm in opts:
			if opt in ("-h", "--help"):
				print >>sys.stderr, __doc__
				return 0
			if opt in ("-s", "--subject"):
				subject = parm
			if opt in ("-r", "--from"):
				fromAddy = parm
			if opt in ("-q", "--plainfile"):
				plainFile = parm
			if opt in ("-Q", "--htmlfile"):
				htmlFile = parm	
			if opt in ("-S", "--smtpserver"):
				smtpServer = parm
		if subject == None:
			raise Usage("no subject")
		if fromAddy == None:
			raise Usage("no from address")
		if plainFile == None:
			raise Usage("no plain message file")
		if htmlFile == None:
			raise Usage("no html message file")

		# process arguments
		toAddrs = args
		if len(toAddrs) == 0:
			raise Usage("no recipients")

		# go do it
		sendmail(smtpServer, fromAddy, toAddrs, subject, plainFile, htmlFile)
	except Usage, err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2

def sendmail(smtpServer, fromAddy, toAddrs, subject, plainFile, htmlFile):
	# Create the root message and fill in the from, to, and subject headers
	toAddr = toAddrs[0]
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = subject
	msgRoot['From'] = fromAddy
	msgRoot['To'] = toAddr
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
	smtp = smtplib.SMTP()
	smtp.connect(smtpServer)
	smtp.sendmail(fromAddy, toAddr, msgRoot.as_string())
	smtp.quit()

if __name__ == "__main__":
	sys.exit(main())