# Source Generated with Decompyle++
# File: generator.pyc (Python 3.12)

'''Classes to generate plain text from a message object tree.'''
__all__ = [
    'Generator',
    'DecodedGenerator',
    'BytesGenerator']
import re
import sys
import time
import random
from copy import deepcopy
from io import StringIO, BytesIO
from email.utils import _has_surrogates
from email.errors import HeaderWriteError
UNDERSCORE = '_'
NL = '\n'
NLCRE = re.compile('\\r\\n|\\r|\\n')
fcre = re.compile('^From ', re.MULTILINE)
NEWLINE_WITHOUT_FWSP = re.compile('\\r\\n[^ \\t]|\\r[^ \\n\\t]|\\n[^ \\t]')

class Generator:
    '''Generates output from a Message object tree.

    This basic generator writes the message to the given file object as plain
    text.
    '''
    
    def __init__(self, outfp = None, mangle_from_ = (None, None), maxheaderlen = {
        'policy': None }, *, policy):
        """Create the generator for message flattening.

        outfp is the output file-like object for writing the message to.  It
        must have a write() method.

        Optional mangle_from_ is a flag that, when True (the default if policy
        is not set), escapes From_ lines in the body of the message by putting
        a `>' in front of them.

        Optional maxheaderlen specifies the longest length for a non-continued
        header.  When a header line is longer (in characters, with tabs
        expanded to 8 spaces) than maxheaderlen, the header will split as
        defined in the Header class.  Set maxheaderlen to zero to disable
        header wrapping.  The default is 78, as recommended (but not required)
        by RFC 2822.

        The policy keyword specifies a policy object that controls a number of
        aspects of the generator's operation.  If no policy is specified,
        the policy associated with the Message object passed to the
        flatten method is used.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def write(self, s):
        self._fp.write(s)

    
    def flatten(self, msg, unixfrom, linesep = (False, None)):
        """Print the message object tree rooted at msg to the output file
        specified when the Generator instance was created.

        unixfrom is a flag that forces the printing of a Unix From_ delimiter
        before the first object in the message tree.  If the original message
        has no From_ delimiter, a `standard' one is crafted.  By default, this
        is False to inhibit the printing of any From_ delimiter.

        Note that for subobjects, no From_ line is printed.

        linesep specifies the characters used to indicate a new line in
        the output.  The default value is determined by the policy specified
        when the Generator instance was created or, if none was specified,
        from the policy associated with the msg.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def clone(self, fp):
        '''Clone this generator with the exact same options.'''
        return self.__class__(fp, self._mangle_from_, None, policy = self.policy)

    
    def _new_buffer(self):
        return StringIO()

    
    def _encode(self, s):
        return s

    
    def _write_lines(self, lines):
        if not lines:
            return None
        lines = NLCRE.split(lines)
        for line in lines[:-1]:
            self.write(line)
            self.write(self._NL)
        if lines[-1]:
            self.write(lines[-1])
            return None

    
    def _write(self, msg):
        oldfp = self._fp
    # WARNING: Decompyle incomplete

    
    def _dispatch(self, msg):
        main = msg.get_content_maintype()
        sub = msg.get_content_subtype()
        specific = UNDERSCORE.join((main, sub)).replace('-', '_')
        meth = getattr(self, '_handle_' + specific, None)
    # WARNING: Decompyle incomplete

    
    def _write_headers(self, msg):
        for h, v in msg.raw_items():
            folded = self.policy.fold(h, v)
            if self.policy.verify_generated_headers:
                linesep = self.policy.linesep
                if not folded.endswith(self.policy.linesep):
                    raise HeaderWriteError(f'''folded header does not end with {linesep!r}: {folded!r}''')
                if NEWLINE_WITHOUT_FWSP.search(folded.removesuffix(linesep)):
                    raise HeaderWriteError(f'''folded header contains newline: {folded!r}''')
            self.write(folded)
        self.write(self._NL)

    
    def _handle_text(self, msg):
        payload = msg.get_payload()
    # WARNING: Decompyle incomplete

    _writeBody = _handle_text
    
    def _handle_multipart(self, msg):
        msgtexts = []
        subparts = msg.get_payload()
    # WARNING: Decompyle incomplete

    
    def _handle_multipart_signed(self, msg):
        p = self.policy
        self.policy = p.clone(max_line_length = 0)
        
        try:
            self._handle_multipart(msg)
            self.policy = p
            return None
        except:
            self.policy = p


    
    def _handle_message_delivery_status(self, msg):
        blocks = []
        for part in msg.get_payload():
            s = self._new_buffer()
            g = self.clone(s)
            g.flatten(part, unixfrom = False, linesep = self._NL)
            text = s.getvalue()
            lines = text.split(self._encoded_NL)
            if lines and lines[-1] == self._encoded_EMPTY:
                blocks.append(self._encoded_NL.join(lines[:-1]))
                continue
            blocks.append(text)
        self._fp.write(self._encoded_NL.join(blocks))

    
    def _handle_message(self, msg):
        s = self._new_buffer()
        g = self.clone(s)
        payload = msg._payload
        if isinstance(payload, list):
            g.flatten(msg.get_payload(0), unixfrom = False, linesep = self._NL)
            payload = s.getvalue()
        else:
            payload = self._encode(payload)
        self._fp.write(payload)

    _make_boundary = (lambda cls, text = (None,): token = random.randrange(sys.maxsize)boundary = '===============' + _fmt % token + '=='# WARNING: Decompyle incomplete
)()
    _compile_re = (lambda cls, s, flags: re.compile(s, flags))()


class BytesGenerator(Generator):
    pass
# WARNING: Decompyle incomplete

_FMT = '[Non-text (%(type)s) part of message omitted, filename %(filename)s]'

class DecodedGenerator(Generator):
    '''Generates a text representation of a message.

    Like the Generator base class, except that non-text parts are substituted
    with a format string representing the part.
    '''
    
    def __init__(self, outfp, mangle_from_ = None, maxheaderlen = (None, None, None), fmt = {
        'policy': None }, *, policy):
        """Like Generator.__init__() except that an additional optional
        argument is allowed.

        Walks through all subparts of a message.  If the subpart is of main
        type `text', then it prints the decoded payload of the subpart.

        Otherwise, fmt is a format string that is used instead of the message
        payload.  fmt is expanded with the following keywords (in
        %(keyword)s format):

        type       : Full MIME type of the non-text part
        maintype   : Main MIME type of the non-text part
        subtype    : Sub-MIME type of the non-text part
        filename   : Filename of the non-text part
        description: Description associated with the non-text part
        encoding   : Content transfer encoding of the non-text part

        The default value for fmt is None, meaning

        [Non-text (%(type)s) part of message omitted, filename %(filename)s]
        """
        Generator.__init__(self, outfp, mangle_from_, maxheaderlen, policy = policy)
    # WARNING: Decompyle incomplete

    
    def _dispatch(self, msg):
        for part in msg.walk():
            maintype = part.get_content_maintype()
            if maintype == 'text':
                print(part.get_payload(decode = False), file = self)
                continue
            if maintype == 'multipart':
                continue
            print(self._fmt % {
                'type': part.get_content_type(),
                'maintype': part.get_content_maintype(),
                'subtype': part.get_content_subtype(),
                'filename': part.get_filename('[no filename]'),
                'description': part.get('Content-Description', '[no description]'),
                'encoding': part.get('Content-Transfer-Encoding', '[no encoding]') }, file = self)


_width = len(repr(sys.maxsize - 1))
_fmt = '%%0%dd' % _width
_make_boundary = Generator._make_boundary
