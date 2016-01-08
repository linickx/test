#!/usr/bin/env python
import hello

def test_hello(capsys):
    hello.main()
    out, err = capsys.readouterr()
    assert out.strip() == "Hello World!"
