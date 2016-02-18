#!/usr/bin/env python
# coding=utf-8
"""
.. module:: mytest
   :platform: Unix, Windows
   :synopsis: My Test module

.. moduleauthor:: Nick Bettison


"""

def simplefunction(text="default"):
    """This is a simple function

    Args:
       text (str):  Some Text.

    Returns:
       str.  The text

    A really great idea.  A way you might use me is

    >>> print(simplefunction("Hello World"))
    Hello World

    Blah, Blah.

    """
    return text

def main():
    """Main function
    
    """
    print(simplefunction("Hello World"))

if __name__ == "__main__":
    main()