#!/usr/bin/env python

'''
Need to put your tty into utf8 mode? see utf-8(7) man page

    The official ESC sequence to switch from an ISO 2022 encoding scheme (as used for
    instance by VT100 terminals) to UTF-8 is ESC % G ("\x1b%G"). The corresponding
    return sequence from UTF-8 to ISO 2022 is ESC % @ ("\x1b%@"). Other ISO 2022
    sequences (such as for switching the G0 and G1 sets) are not applicable in UTF-8
    mode.

if not set as such already, you can set your terminal coding to utf8 mode by:

    printf "\033%s" "%G" > $(tty)

be mindful that your environment needs to support utf8 encoding. check that a utf8
encoding is marked available in /etc/locale.gen such as en_US.UTF-8. if commented, then
uncomment it and run locale-gen. your $LANG environment variable (or other LC*) will
also need to be set to a utf8 variant such as en_US.UTF-8.

glyph references: http://unicode-table.com/en/sections/block-elements/

'''

__version__  = '1.0'
__author__   = 'david ford <david@blue-labs.org> (also: firefighterblu3@gmail.com, rarely read)'
__copyright  = '2014 '+__author__
__license__  = 'Apache 2.0'
__released__ = '2014 July 25'

import sys, time
import codecs, locale

bfill = [' ', '\u258f', '\u258e', '\u258d', '\u258c', '\u258b', '\u258a', '\u2589', '\u2588']


def draw_completion_status_bar(percent_complete, text=''):
    ''' draw a granular text representation of a graphical 100% status bar. this uses utf8
        glyphs to fairly accurately represent a single 1% change across the range. however,
        there are only 8 glyphs to do this with instead of 10 so we jump at the first 1% as
        it looks better with a "burst" at the beginning instead of lacking the last 3 bars.
        
        this only takes a dozen character cells on your tty to represent a rather accurate
        view (it still takes 39 bytes).
    '''
    q,r = divmod(percent_complete and percent_complete+3 or 0, 8)

    box = '\u2588'*q                           # how many solid boxes to draw
    fc  = bfill[r]                             # choose the partially filled box
    pad = ' '*(11-q+1)                         # pad with spaces to the end
    pct = str(percent_complete).rjust(3)+' '   # right justify the numeric value

    # draw the bar with a mild white background and bright white foreground
    s   = '\r\x1b[1;37;47m' + box + fc + pad +'\x1b[0m ' + pct + text
    sys.stdout.write(s)    


def main():
    draw_completion_status_bar(0, 'status line #0')
    print()

    draw_completion_status_bar(1, 'status line #1')
    print()

    for n in range(19):
        draw_completion_status_bar(n, 'status line #2')
        time.sleep(0.1)
    print()

    draw_completion_status_bar(57, 'status line #3')
    print()
    
    draw_completion_status_bar(100, 'status line #4')
    print()


if __name__ == '__main__':
    if False: # want to see what your current encoding information is?
        print('STDOUT Encoding: %s, isatty(%s), locale.getpreferredencoding(%s), sys.getfilesystemencodig(%s)' %(
          sys.stdout.encoding, sys.stdout.isatty(), locale.getpreferredencoding(), sys.getfilesystemencoding()))
    main()
