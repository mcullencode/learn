"""
HTML has a body, has a header. Indicates we can use composition
"""

class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  #DOCtype doesnt have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        self._title_tag = Tag('title', title)
        self.contents = str(self._title_tag)



class Body(Tag):

    def __init__(self):
        super().__init__('body', '') #body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


# in composition, the objects that other objects are composed of, dont exist outside of their container.
# i.e. init method for HtmlDoc class, there are instances of a doctype, head body. all instances of their
# respective classes. which only exist within the HtmlDoc class


class HtmlDoc(object):

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc('DemoHTML Document')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'subheading')
    my_page.add_tag('p', 'This is a paragraph tht will appear on page')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)



#AGGREGATION
#aggregation is just a weaker composition. both have 'has a' relationships,
#just ownership of instances change.
#depends on functon of your program, on what you should choose.
new_body = Body()
new_body.add_tag('h1', 'Aggregation')
new_body.add_tag('p', "Unlike<strong><composition</strong>, aggregation uses existing instances"
                       "of objects to build up another object.")
new_body.add_tag('p', "The compsed object doesnt actually own the objects that its composed of"
                      " - if it's destroyed, those objects contnue to exist")

my_page._body = new_body
with open('test2.html', 'w') as test_doc:
    my_page.display(file=test_doc)