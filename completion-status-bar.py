#!/usr/bin/env python

# http://unicode-table.com/en/sections/block-elements/

__version__  = '1.0'
__author__   = 'david ford <david@blue-labs.org> (also: firefighterblu3@gmail.com, rarely read)'
__copyright  = '2014 '+__author__
__license__  = 'Apache 2.0'
__released__ = '2014 July 25'

import sys, time

bfill = [' ', '\u258f', '\u258e', '\u258d', '\u258c', '\u258b', '\u258a', '\u2589', '\u2588']


def draw_completion_status_bar(percent_complete, text=''):
    ''' draw a granular text representation of a graphical 100% status bar. this uses utf8
        glyphs to fairly accurately represent a single 1% change across the range. however,
        there are only 8 glyphs to do this with instead of 10 so we fake the first 3 % as
        it looks better with a "burst" at the beginning instead of lacking the last 3 bars.
    '''
    q,r = divmod(percent_complete+3, 8)

    box = '\u2588'*q            # how many solid boxes to draw
    fc  = bfill[r]              # choose the partially filled box
    pad = ' '*(11-q+1)          # pad with spaces to the end
    pct = str(n).rjust(3)+' '   # right justify the numeric value

    # draw the bar with a mild white background and bright white foreground
    s   = '\r\x1b[1;37;47m' + box + fc + pad +'\x1b[0m ' + pct + text
    sys.stdout.write(s)    

for n in range(19):
  draw_completion_status_bar(n, 'fatbawls')
  time.sleep(0.01)
