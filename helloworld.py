from backend.soup import soupify
print 'Content-type: text/plain; charset=utf-8'
print ''
print 'Hello AppEngine!'
print soupify('Hello AppEngine!').encode('utf-8')
