# python2
try:
    print "中文"
except SyntaxError:
    print "print chinese failed"
try:
    print u"中文"
except SyntaxError:
    print "print chinese prefixed by u failed"
