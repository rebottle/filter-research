

def fileExt_filter(parms):
    ''' 
FileExt
=======
 This filter allows for file names with (and without) extensions.
    
 The filter is intended to be useful when moving legacy filename based sites to 
    a bottle site with cleaner URLs.
    
 File choices are separated by ',', and extention choices are separated by '.'
 '*' works as a wild card extension, and an empty file choice with match a 
 filename '' or '.extn' and an empty extenion will march files with no extention.
      '''
    assert parms,'fileext filter needs a paramater string after second :'
    plist= parms.split('.')
    filen=plist[0].replace(',','|')
    trail= '|' if '' in plist else ''
    exts = '|'.join( ['[.]'+p for p in plist[1:]]
           ) if not '*' in plist else '([.][^/<]*)?' 
    regexp = '({})({}{})'.format(filen,exts,trail)

    def to_python(match):
        return match

    def to_url(value):
        return value

    return regexp, to_python, to_url
