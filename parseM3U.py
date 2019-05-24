"""ParseM3U
A simple script for parsing M3U playlists into HTML files

Usage: parseM3U.py [filename]
If no filename is specified, ParseM3U will prompt for one.
"""
__author__ = "David Osolkowski (qid@wadny.com)"
__version__ = "1.2"
__date__ = "2010-08-21"
__copyright__ = "Copyright (c) 2010, David Osolkowski, http://www.wadny.com/ All rights reserved."
__license__ = """
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""
__history__ = """
    1.0 - 2003-03-19 - initial release
    1.1 - 2003-03-19 - added option to enter filename after program has started, removed debug info
    1.2 - 2010-08-21 - updated for Python 3.0 syntax changes
"""

# CONFIGURATION:

# Text to insert at the beginning of the HTML file.
# This is a """triple-quoted string""" so it can extend over multiple lines.
BEGIN_TEXT = """"""

# Formatting string for each line.  The first %s will become the name, the
# second %s becomes the number of minutes, and the third %s becomes the
# number of seconds.
FORMAT_STRING = "<li>%s <em>(%s:%s)</em></li>"

# Text to insert at the end of the HTML file.
# This is triple-quoted like BEGIN_TEXT.
END_TEXT = """"""

# END CONFIGURATION

def parsem3u(filename):
    import re

    m3ufile = open(filename)
    htmlfile = open("output.html", "w")

    htmlfile.write(BEGIN_TEXT)

    entries = m3ufile.readlines()
    regex = re.compile(r"#EXTINF:(\d+),(.+)")
    for entry in entries:
        data = regex.match(entry)
        if (data != None):
            time = int(data.group(1))
            name = data.group(2)
            mins = str(int(time / 60))
            secs = str(int(time % 60))
            if (len(secs) == 1):
                secs = "0" + secs

            htmlfile.write(FORMAT_STRING % (name.replace("&", "&amp;"), mins, secs) + "\n")

    htmlfile.write(END_TEXT)

    m3ufile.close()
    htmlfile.close()

if __name__ == "__main__":
    import sys
    if (len(sys.argv) != 2):
        filename = input("Filename: ")
    else:
        filename = sys.argv[1]

    print("Parsing...")
    parsem3u(filename)
    print("Done.")
    input("Press any key to continue...")
