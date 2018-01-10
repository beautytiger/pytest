# -*- coding: utf8 -*-

print 'import a'
import modu_a
print 'import b'
import modu_b
print 'import c'
import modu_c

print '-' * 10
i = modu_a.data
print i
print '-' * 10

# no effect
print 're-import c'
import modu_c

print 'reload c'
reload(modu_c)

print 'reload b'
reload(modu_b)

# no effect
print 're-import a'
import modu_a

print 'reload a'
reload(modu_a)

print i
j = modu_a.data
print j
