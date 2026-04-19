# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

import re
import itertools
import textwrap
import functools

try:
    from importlib.resources import files
    from jaraco.functools import compose, method_cache
    from jaraco.context import ExceptionTrap
    
    def substitution(old, new):
        '''
    Return a function that will perform a substitution on a string
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def multi_substitution(*substitutions):
        """
    Take a sequence of pairs specifying substitutions, and create
    a function that performs those substitutions.

    >>> multi_substitution(('foo', 'bar'), ('bar', 'baz'))('foo')
    'baz'
    """
        substitutions = itertools.starmap(substitution, substitutions)
        substitutions = reversed(tuple(substitutions))
    # WARNING: Decompyle incomplete

    
    class FoldedCase(str):
        pass
    # WARNING: Decompyle incomplete

    _unicode_trap = ExceptionTrap(UnicodeDecodeError)
    is_decodable = (lambda value: value.decode())()
    
    def is_binary(value):
        """
    Return True if the value appears to be binary (that is, it's a byte
    string and isn't decodable).

    >>> is_binary(b'\\xff')
    True
    >>> is_binary('\\xff')
    False
    """
        if isinstance(value, bytes):
            isinstance(value, bytes)
        return not is_decodable(value)

    
    def trim(s):
        '''
    Trim something like a docstring to remove the whitespace that
    is common due to indentation and formatting.

    >>> trim("\\n\\tfoo = bar\\n\\t\\tbar = baz\\n")
    \'foo = bar\\n\\tbar = baz\'
    '''
        return textwrap.dedent(s).strip()

    
    def wrap(s):
        '''
    Wrap lines of text, retaining existing newlines as
    paragraph markers.

    >>> print(wrap(lorem_ipsum))
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
    minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum.
    <BLANKLINE>
    Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam
    varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus
    magna felis sollicitudin mauris. Integer in mauris eu nibh euismod
    gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis
    risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue,
    eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas
    fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla
    a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis,
    neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing
    sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque
    nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus
    quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis,
    molestie eu, feugiat in, orci. In hac habitasse platea dictumst.
    '''
        paragraphs = s.splitlines()
        wrapped = paragraphs()
        return '\n\n'.join(wrapped)

    
    def unwrap(s):
        """
    Given a multi-line string, return an unwrapped version.

    >>> wrapped = wrap(lorem_ipsum)
    >>> wrapped.count('\\n')
    20
    >>> unwrapped = unwrap(wrapped)
    >>> unwrapped.count('\\n')
    1
    >>> print(unwrapped)
    Lorem ipsum dolor sit amet, consectetur adipiscing ...
    Curabitur pretium tincidunt lacus. Nulla gravida orci ...

    """
        paragraphs = re.split('\\n\\n+', s)
        cleaned = paragraphs()
        return '\n'.join(cleaned)

    lorem_ipsum: str = files(__name__).joinpath('Lorem ipsum.txt').read_text(encoding = 'utf-8')
    
    class Splitter:
        """object that will split a string with the given arguments for each call

    >>> s = Splitter(',')
    >>> s('hello, world, this is your, master calling')
    ['hello', ' world', ' this is your', ' master calling']
    """
        
        def __init__(self, *args):
            self.args = args

        
        def __call__(self, s):
            pass
        # WARNING: Decompyle incomplete


    
    def indent(string, prefix = ('    ',)):
        """
    >>> indent('foo')
    '    foo'
    """
        return prefix + string

    
    class WordSet(tuple):
        pass
    # WARNING: Decompyle incomplete

    words = WordSet.parse
    
    def simple_html_strip(s):
        """
    Remove HTML from the string `s`.

    >>> str(simple_html_strip(''))
    ''

    >>> print(simple_html_strip('A <bold>stormy</bold> day in paradise'))
    A stormy day in paradise

    >>> print(simple_html_strip('Somebody <!-- do not --> tell the truth.'))
    Somebody  tell the truth.

    >>> print(simple_html_strip('What about<br/>\\nmultiple lines?'))
    What about
    multiple lines?
    """
        html_stripper = re.compile('(<!--.*?-->)|(<[^>]*>)|([^<]+)', re.DOTALL)
        texts = html_stripper.finditer(s)()
        return ''.join(texts)

    
    class SeparatedValues(str):
        """
    A string separated by a separator. Overrides __iter__ for getting
    the values.

    >>> list(SeparatedValues('a,b,c'))
    ['a', 'b', 'c']

    Whitespace is stripped and empty values are discarded.

    >>> list(SeparatedValues(' a,   b   , c,  '))
    ['a', 'b', 'c']
    """
        separator = ','
        
        def __iter__(self):
            parts = self.split(self.separator)
            
            def <genexpr>(.0):
                pass
            # WARNING: Decompyle incomplete

            return None(<genexpr>, parts())


    
    class Stripper:
        """
    Given a series of lines, find the common prefix and strip it from them.

    >>> lines = [
    ...     'abcdefg\\n',
    ...     'abc\\n',
    ...     'abcde\\n',
    ... ]
    >>> res = Stripper.strip_prefix(lines)
    >>> res.prefix
    'abc'
    >>> list(res.lines)
    ['defg\\n', '\\n', 'de\\n']

    If no prefix is common, nothing should be stripped.

    >>> lines = [
    ...     'abcd\\n',
    ...     '1234\\n',
    ... ]
    >>> res = Stripper.strip_prefix(lines)
    >>> res.prefix = ''
    >>> list(res.lines)
    ['abcd\\n', '1234\\n']
    """
        
        def __init__(self, prefix, lines):
            self.prefix = prefix
            self.lines = map(self, lines)

        strip_prefix = (lambda cls, lines: (prefix_lines, lines) = itertools.tee(lines)prefix = functools.reduce(cls.common_prefix, prefix_lines)cls(prefix, lines))()
        
        def __call__(self, line):
            if not self.prefix:
                return line
            (null, prefix, rest) = None.partition(self.prefix)
            return rest

        common_prefix = (lambda s1, s2: index = min(len(s1), len(s2))if s1[:index] != s2[:index]:
index -= 1if s1[:index] != s2[:index]:
continues1[:index])()

    
    def remove_prefix(text, prefix):
        """
    Remove the prefix from the text if it exists.

    >>> remove_prefix('underwhelming performance', 'underwhelming ')
    'performance'

    >>> remove_prefix('something special', 'sample')
    'something special'
    """
        (null, prefix, rest) = text.rpartition(prefix)
        return rest

    
    def remove_suffix(text, suffix):
        """
    Remove the suffix from the text if it exists.

    >>> remove_suffix('name.git', '.git')
    'name'

    >>> remove_suffix('something special', 'sample')
    'something special'
    """
        (rest, suffix, null) = text.partition(suffix)
        return rest

    
    def normalize_newlines(text):
        """
    Replace alternate newlines with the canonical newline.

    >>> normalize_newlines('Lorem Ipsum\\u2029')
    'Lorem Ipsum\\n'
    >>> normalize_newlines('Lorem Ipsum\\r\\n')
    'Lorem Ipsum\\n'
    >>> normalize_newlines('Lorem Ipsum\\x85')
    'Lorem Ipsum\\n'
    """
        newlines = [
            '\r\n',
            '\r',
            '\n',
            '\xc2\x85',
            ' ',
            ' ']
        pattern = '|'.join(newlines)
        return re.sub(pattern, '\n', text)

    
    def _nonblank(str):
        if str:
            str
        return not str.startswith('#')

    yield_lines = (lambda iterable: itertools.chain.from_iterable(map(yield_lines, iterable)))()
    _ = (lambda text: filter(_nonblank, map(str.strip, text.splitlines())))()
    
    def drop_comment(line):
        """
    Drop comments.

    >>> drop_comment('foo # bar')
    'foo'

    A hash without a space may be in a URL.

    >>> drop_comment('http://example.com/foo#bar')
    'http://example.com/foo#bar'
    """
        return line.partition(' #')[0]

    
    def join_continuation(lines):
        """
    Join lines continued by a trailing backslash.

    >>> list(join_continuation(['foo \\\\', 'bar', 'baz']))
    ['foobar', 'baz']
    >>> list(join_continuation(['foo \\\\', 'bar', 'baz']))
    ['foobar', 'baz']
    >>> list(join_continuation(['foo \\\\', 'bar \\\\', 'baz']))
    ['foobarbaz']

    Not sure why, but...
    The character preceding the backslash is also elided.

    >>> list(join_continuation(['goo\\\\', 'dly']))
    ['godly']

    A terrible idea, but...
    If no line is available to continue, suppress the lines.

    >>> list(join_continuation(['foo', 'bar\\\\', 'baz\\\\']))
    ['foo']
    """
        pass
    # WARNING: Decompyle incomplete

    
    def read_newlines(filename, limit = (1024,)):
        """
    >>> tmp_path = getfixture('tmp_path')
    >>> filename = tmp_path / 'out.txt'
    >>> _ = filename.write_text('foo\\n', newline='', encoding='utf-8')
    >>> read_newlines(filename)
    '\\n'
    >>> _ = filename.write_text('foo\\r\\n', newline='', encoding='utf-8')
    >>> read_newlines(filename)
    '\\r\\n'
    >>> _ = filename.write_text('foo\\r\\nbar\\nbing\\r', newline='', encoding='utf-8')
    >>> read_newlines(filename)
    ('\\r', '\\n', '\\r\\n')
    """
        fp = open(filename, encoding = 'utf-8')
        fp.read(limit)
        None(None, None)
        return fp.newlines
        with None:
            if not None:
                pass
    # WARNING: Decompyle incomplete

    return None
except ImportError:
    from importlib_resources import files
    continue

