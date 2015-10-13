FileExt
=======
 This filter allows for file names with (and without) extensions.
    
 The filter is intended to be useful when moving legacy filename based sites to 
    a bottle site with cleaner URLs.

Multiple extensions
-----------------------
Extention choices are separated by '.'
 '*' works as a wild card extension, and an empty choice will match a file with no extension.
 
for example  <f:fileExt:file.txt.md>  will match both 'file.txt' and 'file.md'
adding a trailing '.' <f:fileExt:file.txt.md> will also match 'file.' and 'file'
using without extentions, eg <f:fileExt:file>
will match with and without any file extentions::

    <page.htm.html.>

will match 'page.htm'  'page.html'  or simply 'page'
      
Multiple Pages
--------------
file choices are separated by ',' (comma). An empty choice (before or after ',' is valid.  
Consider three pages all delivered as templates with the same replacement dictionary::

    @rount('/page1')
    def page1():
        pages('page1')
    @route('/page2')
        pages('page2')
    @route('/page3')
        pages('page3')
    def pages(pg):
        ...

Could get tedious. Instead this filter allows::

    @route('/<pg:fileExt:page1,page2,page3'>
    def pages(pg):
        ...
 
To produce the same result.
Combining with muliple extensions would allow more flexibily.
 
Another usefel example would be::
 
     @route('/pg:fileExt:index,.htm.html.>')
     def index(pg):
         ...

This route would match '/' , 'index.html' 'index.htm' and 'index'
