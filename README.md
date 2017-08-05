hail
----

Send HTML formatted emails from the command line.  For the impatient, it's written in python and works like the old BSD `mail` command.

A Brief History
---------------

Back in the dark ages, people used a program called `mail` to read and send electronic mail.  `mail` was pretty sweet for it's time, the man page calls it an _intelligent mail processing system_.  It lets you read your incoming mail (but not paginate it), and also can compose outbound mail (but no editing, once you typed the line you either sent it or started over) using nothing more than an account on a [VAX-11/780](http://www.netbsd.org/images/machines/vax/vax11-780.jpg) and a [VT100](http://vt100.net/docs/vt100-ug/contents.html) [terminal](http://www.catb.org/~esr/writings/taouu/html/graphics/vt100.jpg).  This was back before graphics were invented, and when unix programs did one thing well, and that's it.  If you wanted to edit your message before you sent it, you fired up `vi` and edited a text file, then piped that file into `mail` to send it.  No address book.  No spam.  Nothing fancy.  

Today, most *nix machines don't even have `mail` installed.  However, I still occasionally have a need to send emails from the command line, and `mail` works fine.  Except for one thing.  It can't send HTML formatted messages.

`hail` works kinda like `mail`, except it can send HTML formatted messages.  Oh yeah, and `hail` doesn't read mail.  There, I broke [Jamie Zawinski's](http://www.jwz.org/) [Law of Software Envelopment](http://www.jwz.org/hacks/) which states:

> "Every program attempts to expand until it can read mail. Those
> programs which cannot so expand are replaced by ones which can."

For all you kids out there who have never heard of Jamie Zawinski, he worked at [Mosiac Communications Corporation](http://home.mcom.com/)  back when Windows was still a 16 bit OS. He wrote the unix version of [Netscape](http://home.mcom.com/archives/) (which later became [Netscape Navigator](http://browser.netscape.com/releases) and which is now [Mozilla Firefox](http://www.mozilla.com/firefox)). And yes, he was the guy who wrote the first version of Netscape Mail and News.

Download and Install
--------------------

You need 2.7+ or 3+.  Rename `hail.py` to `hail`, make it executable, and put it in your path.

To run it on Windows, you may need to do some tweaking.

License
-------
Check the LICENSE file, but it's the MIT License, which means you can do whatever you want, as long as you keep the copyright notice.