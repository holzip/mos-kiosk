# Source Generated with Decompyle++
# File: _header_value_parser.pyc (Python 3.12)

'''Header value parser implementing various email-related RFC parsing rules.

The parsing methods defined in this module implement various email related
parsing rules.  Principal among them is RFC 5322, which is the followon
to RFC 2822 and primarily a clarification of the former.  It also implements
RFC 2047 encoded word decoding.

RFC 5322 goes to considerable trouble to maintain backward compatibility with
RFC 822 in the parse phase, while cleaning up the structure on the generation
phase.  This parser supports correct RFC 5322 generation by tagging white space
as folding white space only when folding is allowed in the non-obsolete rule
sets.  Actually, the parser is even more generous when accepting input than RFC
5322 mandates, following the spirit of Postel\'s Law, which RFC 5322 encourages.
Where possible deviations from the standard are annotated on the \'defects\'
attribute of tokens that deviate.

The general structure of the parser follows RFC 5322, and uses its terminology
where there is a direct correspondence.  Where the implementation requires a
somewhat different structure than that used by the formal grammar, new terms
that mimic the closest existing terms are used.  Thus, it really helps to have
a copy of RFC 5322 handy when studying this code.

Input to the parser is a string that has already been unfolded according to
RFC 5322 rules.  According to the RFC this unfolding is the very first step, and
this parser leaves the unfolding step to a higher level message parser, which
will have already detected the line breaks that need unfolding while
determining the beginning and end of each header.

The output of the parser is a TokenList object, which is a list subclass.  A
TokenList is a recursive data structure.  The terminal nodes of the structure
are Terminal objects, which are subclasses of str.  These do not correspond
directly to terminal objects in the formal grammar, but are instead more
practical higher level combinations of true terminals.

All TokenList and Terminal objects have a \'value\' attribute, which produces the
semantically meaningful value of that part of the parse subtree.  The value of
all whitespace tokens (no matter how many sub-tokens they may contain) is a
single space, as per the RFC rules.  This includes \'CFWS\', which is herein
included in the general class of whitespace tokens.  There is one exception to
the rule that whitespace tokens are collapsed into single spaces in values: in
the value of a \'bare-quoted-string\' (a quoted-string with no leading or
trailing whitespace), any whitespace that appeared between the quotation marks
is preserved in the returned value.  Note that in all Terminal strings quoted
pairs are turned into their unquoted values.

All TokenList and Terminal objects also have a string value, which attempts to
be a "canonical" representation of the RFC-compliant form of the substring that
produced the parsed subtree, including minimal use of quoted pair quoting.
Whitespace runs are not collapsed.

Comment tokens also have a \'content\' attribute providing the string found
between the parens (including any nested comments) with whitespace preserved.

All TokenList and Terminal objects have a \'defects\' attribute which is a
possibly empty list all of the defects found while creating the token.  Defects
may appear on any token in the tree, and a composite list of all defects in the
subtree is available through the \'all_defects\' attribute of any node.  (For
Terminal notes x.defects == x.all_defects.)

Each object in a parse tree is called a \'token\', and each has a \'token_type\'
attribute that gives the name from the RFC 5322 grammar that it represents.
Not all RFC 5322 nodes are produced, and there is one non-RFC 5322 node that
may be produced: \'ptext\'.  A \'ptext\' is a string of printable ascii characters.
It is returned in place of lists of (ctext/quoted-pair) and
(qtext/quoted-pair).

XXX: provide complete list of token types.
'''
import re
import sys
import urllib
from string import hexdigits
from operator import itemgetter
from email import _encoded_words as _ew
from email import errors
from email import utils
WSP = set(' \t')
CFWS_LEADER = WSP | set('(')
SPECIALS = set('()<>@,:;.\\"[]')
ATOM_ENDS = SPECIALS | WSP
DOT_ATOM_ENDS = ATOM_ENDS - set('.')
PHRASE_ENDS = SPECIALS - set('."(')
TSPECIALS = (SPECIALS | set('/?=')) - set('.')
TOKEN_ENDS = TSPECIALS | WSP
ASPECIALS = TSPECIALS | set("*'%")
ATTRIBUTE_ENDS = ASPECIALS | WSP
EXTENDED_ATTRIBUTE_ENDS = ATTRIBUTE_ENDS - set('%')
NLSET = {
    '\n',
    '\r'}
SPECIALSNL = SPECIALS | NLSET

def make_quoted_pairs(value):
    '''Escape dquote and backslash for use within a quoted-string.'''
    return str(value).replace('\\', '\\\\').replace('"', '\\"')


def quote_string(value):
    escaped = make_quoted_pairs(value)
    return f'''"{escaped}"'''

rfc2047_matcher = re.compile("\n   =\\?            # literal =?\n   [^?]*          # charset\n   \\?             # literal ?\n   [qQbB]         # literal 'q' or 'b', case insensitive\n   \\?             # literal ?\n  .*?             # encoded word\n  \\?=             # literal ?=\n", re.VERBOSE | re.MULTILINE)

class TokenList(list):
    pass
# WARNING: Decompyle incomplete


class WhiteSpaceTokenList(TokenList):
    value = (lambda self: ' ')()
    comments = (lambda self: pass# WARNING: Decompyle incomplete
)()


class UnstructuredTokenList(TokenList):
    token_type = 'unstructured'


class Phrase(TokenList):
    token_type = 'phrase'


class Word(TokenList):
    token_type = 'word'


class CFWSList(WhiteSpaceTokenList):
    token_type = 'cfws'


class Atom(TokenList):
    token_type = 'atom'


class Token(TokenList):
    token_type = 'token'
    encode_as_ew = False


class EncodedWord(TokenList):
    token_type = 'encoded-word'
    cte = None
    charset = None
    lang = None


class QuotedString(TokenList):
    token_type = 'quoted-string'
    content = (lambda self: for x in self:
if not x.token_type == 'bare-quoted-string':
continueself, x.value)()
    quoted_value = (lambda self: res = []for x in self:
if x.token_type == 'bare-quoted-string':
res.append(str(x))continueres.append(x.value)''.join(res))()
    stripped_value = (lambda self: for token in self:
if not token.token_type == 'bare-quoted-string':
continueself, token.value)()


class BareQuotedString(QuotedString):
    token_type = 'bare-quoted-string'
    
    def __str__(self):
        return ''.join((lambda .0: pass# WARNING: Decompyle incomplete
)(self()))

    value = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self())
)()


class Comment(WhiteSpaceTokenList):
    token_type = 'comment'
    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def quote(self, value):
        if value.token_type == 'comment':
            return str(value)
        return None(value).replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

    content = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self())
)()
    comments = (lambda self: [
self.content])()


class AddressList(TokenList):
    token_type = 'address-list'
    addresses = (lambda self: pass# WARNING: Decompyle incomplete
)()
    mailboxes = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self(), [])
)()
    all_mailboxes = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self(), [])
)()


class Address(TokenList):
    token_type = 'address'
    display_name = (lambda self: if self[0].token_type == 'group':
self[0].display_name)()
    mailboxes = (lambda self: if self[0].token_type == 'mailbox':
[
self[0]]if None[0].token_type == 'invalid-mailbox':
[]None[0].mailboxes)()
    all_mailboxes = (lambda self: if self[0].token_type == 'mailbox':
[
self[0]]if None[0].token_type == 'invalid-mailbox':
[
self[0]]None[0].all_mailboxes)()


class MailboxList(TokenList):
    token_type = 'mailbox-list'
    mailboxes = (lambda self: pass# WARNING: Decompyle incomplete
)()
    all_mailboxes = (lambda self: pass# WARNING: Decompyle incomplete
)()


class GroupList(TokenList):
    token_type = 'group-list'
    mailboxes = (lambda self: if self or self[0].token_type != 'mailbox-list':
[]None[0].mailboxes)()
    all_mailboxes = (lambda self: if self or self[0].token_type != 'mailbox-list':
[]None[0].all_mailboxes)()


class Group(TokenList):
    token_type = 'group'
    mailboxes = (lambda self: if self[2].token_type != 'group-list':
[]None[2].mailboxes)()
    all_mailboxes = (lambda self: if self[2].token_type != 'group-list':
[]None[2].all_mailboxes)()
    display_name = (lambda self: self[0].display_name)()


class NameAddr(TokenList):
    token_type = 'name-addr'
    display_name = (lambda self: if len(self) == 1:
Noneself[0].display_name)()
    local_part = (lambda self: self[-1].local_part)()
    domain = (lambda self: self[-1].domain)()
    route = (lambda self: self[-1].route)()
    addr_spec = (lambda self: self[-1].addr_spec)()


class AngleAddr(TokenList):
    token_type = 'angle-addr'
    local_part = (lambda self: for x in self:
if not x.token_type == 'addr-spec':
continueself, x.local_part)()
    domain = (lambda self: for x in self:
if not x.token_type == 'addr-spec':
continueself, x.domain)()
    route = (lambda self: for x in self:
if not x.token_type == 'obs-route':
continueself, x.domains)()
    addr_spec = (lambda self: for x in self:
if not x.token_type == 'addr-spec':
continueif x.local_part:
self, x.addr_specNone, self(x.local_part) + x.addr_spec'<>')()


class ObsRoute(TokenList):
    token_type = 'obs-route'
    domains = (lambda self: pass# WARNING: Decompyle incomplete
)()


class Mailbox(TokenList):
    token_type = 'mailbox'
    display_name = (lambda self: if self[0].token_type == 'name-addr':
self[0].display_name)()
    local_part = (lambda self: self[0].local_part)()
    domain = (lambda self: self[0].domain)()
    route = (lambda self: if self[0].token_type == 'name-addr':
self[0].route)()
    addr_spec = (lambda self: self[0].addr_spec)()


class InvalidMailbox(TokenList):
    token_type = 'invalid-mailbox'
    display_name = (lambda self: pass)()
    local_part = display_name
    domain = display_name
    route = display_name
    addr_spec = display_name


class Domain(TokenList):
    pass
# WARNING: Decompyle incomplete


class DotAtom(TokenList):
    token_type = 'dot-atom'


class DotAtomText(TokenList):
    token_type = 'dot-atom-text'
    as_ew_allowed = True


class NoFoldLiteral(TokenList):
    token_type = 'no-fold-literal'
    as_ew_allowed = False


class AddrSpec(TokenList):
    token_type = 'addr-spec'
    as_ew_allowed = False
    local_part = (lambda self: self[0].local_part)()
    domain = (lambda self: if len(self) < 3:
Noneself[-1].domain)()
    value = (lambda self: if len(self) < 3:
self[0].valueNone[0].value.rstrip() + self[1].value + self[2].value.lstrip())()
    addr_spec = (lambda self: nameset = set(self.local_part)if len(nameset) > len(nameset - DOT_ATOM_ENDS):
lp = quote_string(self.local_part)else:
lp = self.local_part# WARNING: Decompyle incomplete
)()


class ObsLocalPart(TokenList):
    token_type = 'obs-local-part'
    as_ew_allowed = False


class DisplayName(Phrase):
    pass
# WARNING: Decompyle incomplete


class LocalPart(TokenList):
    token_type = 'local-part'
    as_ew_allowed = False
    value = (lambda self: if self[0].token_type == 'quoted-string':
self[0].quoted_valueNone[0].value)()
    local_part = (lambda self: res = [
DOT]last = DOTlast_is_tl = Falsefor tok in self[0] + [
DOT]:
if tok.token_type == 'cfws':
continueif last_is_tl and tok.token_type == 'dot' and last[-1].token_type == 'cfws':
res[-1] = TokenList(last[:-1])is_tl = isinstance(tok, TokenList)last = res[-1]last_is_tl = is_tlres = TokenList(res[1:-1])res.value)()


class DomainLiteral(TokenList):
    pass
# WARNING: Decompyle incomplete


class MIMEVersion(TokenList):
    token_type = 'mime-version'
    major = None
    minor = None


class Parameter(TokenList):
    token_type = 'parameter'
    sectioned = False
    extended = False
    charset = 'us-ascii'
    section_number = (lambda self: if self.sectioned:
self[1].number)()
    param_value = (lambda self: for token in self:
if token.token_type == 'value':
self, token.stripped_valueif not self.token_type == 'quoted-string':
continuefor None in token:
if not token.token_type == 'bare-quoted-string':
continuefor None in token:
if not token.token_type == 'value':
continueNone, token, None, token.stripped_value'')()


class InvalidParameter(Parameter):
    token_type = 'invalid-parameter'


class Attribute(TokenList):
    token_type = 'attribute'
    stripped_value = (lambda self: for token in self:
if not token.token_type.endswith('attrtext'):
continueself, token.value)()


class Section(TokenList):
    token_type = 'section'
    number = None


class Value(TokenList):
    token_type = 'value'
    stripped_value = (lambda self: token = self[0]if token.token_type == 'cfws':
token = self[1]if token.token_type.endswith(('quoted-string', 'attribute', 'extended-attribute')):
token.stripped_valueNone.value)()


class MimeParameters(TokenList):
    token_type = 'mime-parameters'
    syntactic_break = False
    params = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def __str__(self):
        params = []
        for name, value in self.params:
            if value:
                params.append('{}={}'.format(name, quote_string(value)))
                continue
            params.append(name)
        params = '; '.join(params)
        if params:
            return ' ' + params



class ParameterizedHeaderValue(TokenList):
    syntactic_break = False
    params = (lambda self: for token in reversed(self):
if not token.token_type == 'mime-parameters':
continuereversed(self), token.params{ })()


class ContentType(ParameterizedHeaderValue):
    token_type = 'content-type'
    as_ew_allowed = False
    maintype = 'text'
    subtype = 'plain'


class ContentDisposition(ParameterizedHeaderValue):
    token_type = 'content-disposition'
    as_ew_allowed = False
    content_disposition = None


class ContentTransferEncoding(TokenList):
    token_type = 'content-transfer-encoding'
    as_ew_allowed = False
    cte = '7bit'


class HeaderLabel(TokenList):
    token_type = 'header-label'
    as_ew_allowed = False


class MsgID(TokenList):
    token_type = 'msg-id'
    as_ew_allowed = False
    
    def fold(self, policy):
        return str(self) + policy.linesep



class MessageID(MsgID):
    token_type = 'message-id'


class InvalidMessageID(MessageID):
    token_type = 'invalid-message-id'


class Header(TokenList):
    token_type = 'header'


class Terminal(str):
    pass
# WARNING: Decompyle incomplete


class WhiteSpaceTerminal(Terminal):
    value = (lambda self: ' ')()
    
    def startswith_fws(self):
        return True



class ValueTerminal(Terminal):
    value = (lambda self: self)()
    
    def startswith_fws(self):
        return False



class EWWhiteSpaceTerminal(WhiteSpaceTerminal):
    value = (lambda self: '')()
    
    def __str__(self):
        return ''



class _InvalidEwError(errors.HeaderParseError):
    '''Invalid encoded word found while parsing headers.'''
    pass

DOT = ValueTerminal('.', 'dot')
ListSeparator = ValueTerminal(',', 'list-separator')
ListSeparator.as_ew_allowed = False
ListSeparator.syntactic_break = False
RouteComponentMarker = ValueTerminal('@', 'route-component-marker')
_wsp_splitter = re.compile('([{}]+)'.format(''.join(WSP))).split
_non_atom_end_matcher = re.compile('[^{}]+'.format(re.escape(''.join(ATOM_ENDS)))).match
_non_printable_finder = re.compile('[\\x00-\\x20\\x7F]').findall
_non_token_end_matcher = re.compile('[^{}]+'.format(re.escape(''.join(TOKEN_ENDS)))).match
_non_attribute_end_matcher = re.compile('[^{}]+'.format(re.escape(''.join(ATTRIBUTE_ENDS)))).match
_non_extended_attribute_end_matcher = re.compile('[^{}]+'.format(re.escape(''.join(EXTENDED_ATTRIBUTE_ENDS)))).match

def _validate_xtext(xtext):
    '''If input token contains ASCII non-printables, register a defect.'''
    non_printables = _non_printable_finder(xtext)
    if non_printables:
        xtext.defects.append(errors.NonPrintableDefect(non_printables))
    if utils._has_surrogates(xtext):
        xtext.defects.append(errors.UndecodableBytesDefect('Non-ASCII characters found in header token'))
        return None


def _get_ptext_to_endchars(value, endchars):
    '''Scan printables/quoted-pairs until endchars and return unquoted ptext.

    This function turns a run of qcontent, ccontent-without-comments, or
    dtext-with-quoted-printables into a single string by unquoting any
    quoted printables.  It returns the string, the remaining value, and
    a flag that is True iff there were any quoted printables decoded.

    '''
    pass
# WARNING: Decompyle incomplete


def get_fws(value):
    """FWS = 1*WSP

    This isn't the RFC definition.  We're using fws to represent tokens where
    folding can be done, but when we are parsing the *un*folding has already
    been done so we don't need to watch out for CRLF.

    """
    newvalue = value.lstrip()
    fws = WhiteSpaceTerminal(value[:len(value) - len(newvalue)], 'fws')
    return (fws, newvalue)


def get_encoded_word(value, terminal_type = ('vtext',)):
    ''' encoded-word = "=?" charset "?" encoding "?" encoded-text "?="

    '''
    ew = EncodedWord()
    if not value.startswith('=?'):
        raise errors.HeaderParseError('expected encoded word but found {}'.format(value))
# WARNING: Decompyle incomplete


def get_unstructured(value):
    """unstructured = (*([FWS] vchar) *WSP) / obs-unstruct
       obs-unstruct = *((*LF *CR *(obs-utext) *LF *CR)) / FWS)
       obs-utext = %d0 / obs-NO-WS-CTL / LF / CR

       obs-NO-WS-CTL is control characters except WSP/CR/LF.

    So, basically, we have printable runs, plus control characters or nulls in
    the obsolete syntax, separated by whitespace.  Since RFC 2047 uses the
    obsolete syntax in its specification, but requires whitespace on either
    side of the encoded words, I can see no reason to need to separate the
    non-printable-non-whitespace from the printable runs if they occur, so we
    parse this into xtext tokens separated by WSP tokens.

    Because an 'unstructured' value must by definition constitute the entire
    value, this 'get' routine does not return a remaining value, only the
    parsed TokenList.

    """
    unstructured = UnstructuredTokenList()
# WARNING: Decompyle incomplete


def get_qp_ctext(value):
    """ctext = <printable ascii except \\ ( )>

    This is not the RFC ctext, since we are handling nested comments in comment
    and unquoting quoted-pairs here.  We allow anything except the '()'
    characters, but if we find any ASCII other than the RFC defined printable
    ASCII, a NonPrintableDefect is added to the token's defects list.  Since
    quoted pairs are converted to their unquoted values, what is returned is
    a 'ptext' token.  In this case it is a WhiteSpaceTerminal, so it's value
    is ' '.

    """
    (ptext, value, _) = _get_ptext_to_endchars(value, '()')
    ptext = WhiteSpaceTerminal(ptext, 'ptext')
    _validate_xtext(ptext)
    return (ptext, value)


def get_qcontent(value):
    """qcontent = qtext / quoted-pair

    We allow anything except the DQUOTE character, but if we find any ASCII
    other than the RFC defined printable ASCII, a NonPrintableDefect is
    added to the token's defects list.  Any quoted pairs are converted to their
    unquoted values, so what is returned is a 'ptext' token.  In this case it
    is a ValueTerminal.

    """
    (ptext, value, _) = _get_ptext_to_endchars(value, '"')
    ptext = ValueTerminal(ptext, 'ptext')
    _validate_xtext(ptext)
    return (ptext, value)


def get_atext(value):
    """atext = <matches _atext_matcher>

    We allow any non-ATOM_ENDS in atext, but add an InvalidATextDefect to
    the token's defects list if we find non-atext characters.
    """
    m = _non_atom_end_matcher(value)
    if not m:
        raise errors.HeaderParseError("expected atext but found '{}'".format(value))
    atext = m.group()
    value = value[len(atext):]
    atext = ValueTerminal(atext, 'atext')
    _validate_xtext(atext)
    return (atext, value)


def get_bare_quoted_string(value):
    '''bare-quoted-string = DQUOTE *([FWS] qcontent) [FWS] DQUOTE

    A quoted-string without the leading or trailing white space.  Its
    value is the text between the quote marks, with whitespace
    preserved and quoted pairs decoded.
    '''
    if value or value[0] != '"':
        raise errors.HeaderParseError('expected \'"\' but found \'{}\''.format(value))
    bare_quoted_string = BareQuotedString()
    value = value[1:]
    if value and value[0] == '"':
        (token, value) = get_qcontent(value)
        bare_quoted_string.append(token)
    if value and value[0] != '"':
        if value[0] in WSP:
            (token, value) = get_fws(value)
        elif value[:2] == '=?':
            valid_ew = False
            
            try:
                (token, value) = get_encoded_word(value)
                bare_quoted_string.defects.append(errors.InvalidHeaderDefect('encoded word inside quoted string'))
                valid_ew = True
                if valid_ew and len(bare_quoted_string) > 1 and bare_quoted_string[-1].token_type == 'fws' and bare_quoted_string[-2].token_type == 'encoded-word':
                    bare_quoted_string[-1] = EWWhiteSpaceTerminal(bare_quoted_string[-1], 'fws')
                else:
                    (token, value) = get_qcontent(value)
                bare_quoted_string.append(token)
                if value and value[0] != '"':
                    continue
                if not value:
                    bare_quoted_string.defects.append(errors.InvalidHeaderDefect('end of header inside quoted string'))
                    return (bare_quoted_string, value)
                return (None, value[1:])
            except errors.HeaderParseError:
                (token, value) = get_qcontent(value)
                continue



def get_comment(value):
    '''comment = "(" *([FWS] ccontent) [FWS] ")"
       ccontent = ctext / quoted-pair / comment

    We handle nested comments here, and quoted-pair in our qp-ctext routine.
    '''
    if value and value[0] != '(':
        raise errors.HeaderParseError("expected '(' but found '{}'".format(value))
    comment = Comment()
    value = value[1:]
    if value and value[0] != ')':
        if value[0] in WSP:
            (token, value) = get_fws(value)
        elif value[0] == '(':
            (token, value) = get_comment(value)
        else:
            (token, value) = get_qp_ctext(value)
        comment.append(token)
        if value and value[0] != ')':
            continue
    if not value:
        comment.defects.append(errors.InvalidHeaderDefect('end of header inside comment'))
        return (comment, value)
    return (None, value[1:])


def get_cfws(value):
    '''CFWS = (1*([FWS] comment) [FWS]) / FWS

    '''
    cfws = CFWSList()
    if value and value[0] in CFWS_LEADER:
        if value[0] in WSP:
            (token, value) = get_fws(value)
        else:
            (token, value) = get_comment(value)
        cfws.append(token)
        if value and value[0] in CFWS_LEADER:
            continue
    return (cfws, value)


def get_quoted_string(value):
    """quoted-string = [CFWS] <bare-quoted-string> [CFWS]

    'bare-quoted-string' is an intermediate class defined by this
    parser and not by the RFC grammar.  It is the quoted string
    without any attached CFWS.
    """
    quoted_string = QuotedString()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        quoted_string.append(token)
    (token, value) = get_bare_quoted_string(value)
    quoted_string.append(token)
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        quoted_string.append(token)
    return (quoted_string, value)


def get_atom(value):
    '''atom = [CFWS] 1*atext [CFWS]

    An atom could be an rfc2047 encoded word.
    '''
    atom = Atom()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        atom.append(token)
    if value and value[0] in ATOM_ENDS:
        raise errors.HeaderParseError("expected atom but found '{}'".format(value))
    if value.startswith('=?'):
        
        try:
            (token, value) = get_encoded_word(value)
        (token, value) = get_atext(value)
        if value and value[0] in CFWS_LEADER:
            (token, value) = get_cfws(value)
            atom.append(token)

    return (atom, value)
    except errors.HeaderParseError:
        (token, value) = get_atext(value)
        continue


def get_dot_atom_text(value):
    ''' dot-text = 1*atext *("." 1*atext)

    '''
    dot_atom_text = DotAtomText()
    if value or value[0] in ATOM_ENDS:
        raise errors.HeaderParseError("expected atom at a start of dot-atom-text but found '{}'".format(value))
    if value and value[0] not in ATOM_ENDS:
        (token, value) = get_atext(value)
        dot_atom_text.append(token)
        if value and value[0] == '.':
            dot_atom_text.append(DOT)
            value = value[1:]
        if value and value[0] not in ATOM_ENDS:
            continue
    if dot_atom_text[-1] is DOT:
        raise errors.HeaderParseError("expected atom at end of dot-atom-text but found '{}'".format('.' + value))
    return (dot_atom_text, value)


def get_dot_atom(value):
    ''' dot-atom = [CFWS] dot-atom-text [CFWS]

    Any place we can have a dot atom, we could instead have an rfc2047 encoded
    word.
    '''
    dot_atom = DotAtom()
    if value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        dot_atom.append(token)
    if value.startswith('=?'):
        
        try:
            (token, value) = get_encoded_word(value)
        (token, value) = get_dot_atom_text(value)
        if value and value[0] in CFWS_LEADER:
            (token, value) = get_cfws(value)
            dot_atom.append(token)

    return (dot_atom, value)
    except errors.HeaderParseError:
        (token, value) = get_dot_atom_text(value)
        continue


def get_word(value):
    """word = atom / quoted-string

    Either atom or quoted-string may start with CFWS.  We have to peel off this
    CFWS first to determine which type of word to parse.  Afterward we splice
    the leading CFWS, if any, into the parsed sub-token.

    If neither an atom or a quoted-string is found before the next special, a
    HeaderParseError is raised.

    The token returned is either an Atom or a QuotedString, as appropriate.
    This means the 'word' level of the formal grammar is not represented in the
    parse tree; this is because having that extra layer when manipulating the
    parse tree is more confusing than it is helpful.

    """
    if value[0] in CFWS_LEADER:
        (leader, value) = get_cfws(value)
    else:
        leader = None
    if not value:
        raise errors.HeaderParseError("Expected 'atom' or 'quoted-string' but found nothing.")
    if value[0] == '"':
        (token, value) = get_quoted_string(value)
    elif value[0] in SPECIALS:
        raise errors.HeaderParseError("Expected 'atom' or 'quoted-string' but found '{}'".format(value))
    (token, value) = get_atom(value)
# WARNING: Decompyle incomplete


def get_phrase(value):
    ''' phrase = 1*word / obs-phrase
        obs-phrase = word *(word / "." / CFWS)

    This means a phrase can be a sequence of words, periods, and CFWS in any
    order as long as it starts with at least one word.  If anything other than
    words is detected, an ObsoleteHeaderDefect is added to the token\'s defect
    list.  We also accept a phrase that starts with CFWS followed by a dot;
    this is registered as an InvalidHeaderDefect, since it is not supported by
    even the obsolete grammar.

    '''
    phrase = Phrase()
    
    try:
        (token, value) = get_word(value)
        phrase.append(token)
        if value and value[0] not in PHRASE_ENDS:
            if value[0] == '.':
                phrase.append(DOT)
                phrase.defects.append(errors.ObsoleteHeaderDefect("period in 'phrase'"))
                value = value[1:]
            else:
                
                try:
                    (token, value) = get_word(value)
                    phrase.append(token)
                    if value and value[0] not in PHRASE_ENDS:
                        continue
                    return (phrase, value)
                    except errors.HeaderParseError:
                        phrase.defects.append(errors.InvalidHeaderDefect('phrase does not start with word'))
                        continue
                except errors.HeaderParseError:
                    if value[0] in CFWS_LEADER:
                        (token, value) = get_cfws(value)
                        phrase.defects.append(errors.ObsoleteHeaderDefect('comment found without atom'))
                    else:
                        raise 
                    continue




def get_local_part(value):
    ''' local-part = dot-atom / quoted-string / obs-local-part

    '''
    local_part = LocalPart()
    leader = None
    if value and value[0] in CFWS_LEADER:
        (leader, value) = get_cfws(value)
    if not value:
        raise errors.HeaderParseError("expected local-part but found '{}'".format(value))
# WARNING: Decompyle incomplete


def get_obs_local_part(value):
    ''' obs-local-part = word *("." word)
    '''
    obs_local_part = ObsLocalPart()
    last_non_ws_was_dot = False
    if value:
        if value[0] == '\\' or value[0] not in PHRASE_ENDS:
            if value[0] == '.':
                if last_non_ws_was_dot:
                    obs_local_part.defects.append(errors.InvalidHeaderDefect("invalid repeated '.'"))
                obs_local_part.append(DOT)
                last_non_ws_was_dot = True
                value = value[1:]
                continue
            if value[0] == '\\':
                obs_local_part.append(ValueTerminal(value[0], 'misplaced-special'))
                value = value[1:]
                obs_local_part.defects.append(errors.InvalidHeaderDefect("'\\' character outside of quoted-string/ccontent"))
                last_non_ws_was_dot = False
                continue
            if obs_local_part and obs_local_part[-1].token_type != 'dot':
                obs_local_part.defects.append(errors.InvalidHeaderDefect("missing '.' between words"))
            
            try:
                (token, value) = get_word(value)
                last_non_ws_was_dot = False
                obs_local_part.append(token)
                if value:
                    if value[0] == '\\':
                        continue
                    if value[0] not in PHRASE_ENDS:
                        continue
                if not obs_local_part:
                    raise errors.HeaderParseError("expected obs-local-part but found '{}'".format(value))
                if (obs_local_part[0].token_type == 'dot' or obs_local_part[0].token_type == 'cfws') and len(obs_local_part) > 1 and obs_local_part[1].token_type == 'dot':
                    obs_local_part.defects.append(errors.InvalidHeaderDefect("Invalid leading '.' in local part"))
                if (obs_local_part[-1].token_type == 'dot' or obs_local_part[-1].token_type == 'cfws') and len(obs_local_part) > 1 and obs_local_part[-2].token_type == 'dot':
                    obs_local_part.defects.append(errors.InvalidHeaderDefect("Invalid trailing '.' in local part"))
                if obs_local_part.defects:
                    obs_local_part.token_type = 'invalid-obs-local-part'
                return (obs_local_part, value)
            except errors.HeaderParseError:
                if value[0] not in CFWS_LEADER:
                    raise 
                (token, value) = get_cfws(value)
                continue



def get_dtext(value):
    """ dtext = <printable ascii except \\ [ ]> / obs-dtext
        obs-dtext = obs-NO-WS-CTL / quoted-pair

    We allow anything except the excluded characters, but if we find any
    ASCII other than the RFC defined printable ASCII, a NonPrintableDefect is
    added to the token's defects list.  Quoted pairs are converted to their
    unquoted values, so what is returned is a ptext token, in this case a
    ValueTerminal.  If there were quoted-printables, an ObsoleteHeaderDefect is
    added to the returned token's defect list.

    """
    (ptext, value, had_qp) = _get_ptext_to_endchars(value, '[]')
    ptext = ValueTerminal(ptext, 'ptext')
    if had_qp:
        ptext.defects.append(errors.ObsoleteHeaderDefect('quoted printable found in domain-literal'))
    _validate_xtext(ptext)
    return (ptext, value)


def _check_for_early_dl_end(value, domain_literal):
    if value:
        return False
    domain_literal.append(errors.InvalidHeaderDefect('end of input inside domain-literal'))
    domain_literal.append(ValueTerminal(']', 'domain-literal-end'))
    return True


def get_domain_literal(value):
    ''' domain-literal = [CFWS] "[" *([FWS] dtext) [FWS] "]" [CFWS]

    '''
    domain_literal = DomainLiteral()
    if value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        domain_literal.append(token)
    if not value:
        raise errors.HeaderParseError('expected domain-literal')
    if value[0] != '[':
        raise errors.HeaderParseError("expected '[' at start of domain-literal but found '{}'".format(value))
    value = value[1:]
    if _check_for_early_dl_end(value, domain_literal):
        return (domain_literal, value)
    None.append(ValueTerminal('[', 'domain-literal-start'))
    if value[0] in WSP:
        (token, value) = get_fws(value)
        domain_literal.append(token)
    (token, value) = get_dtext(value)
    domain_literal.append(token)
    if _check_for_early_dl_end(value, domain_literal):
        return (domain_literal, value)
    if None[0] in WSP:
        (token, value) = get_fws(value)
        domain_literal.append(token)
    if _check_for_early_dl_end(value, domain_literal):
        return (domain_literal, value)
    if None[0] != ']':
        raise errors.HeaderParseError("expected ']' at end of domain-literal but found '{}'".format(value))
    domain_literal.append(ValueTerminal(']', 'domain-literal-end'))
    value = value[1:]
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        domain_literal.append(token)
    return (domain_literal, value)


def get_domain(value):
    ''' domain = dot-atom / domain-literal / obs-domain
        obs-domain = atom *("." atom))

    '''
    domain = Domain()
    leader = None
    if value and value[0] in CFWS_LEADER:
        (leader, value) = get_cfws(value)
    if not value:
        raise errors.HeaderParseError("expected domain but found '{}'".format(value))
# WARNING: Decompyle incomplete


def get_addr_spec(value):
    ''' addr-spec = local-part "@" domain

    '''
    addr_spec = AddrSpec()
    (token, value) = get_local_part(value)
    addr_spec.append(token)
    if value or value[0] != '@':
        addr_spec.defects.append(errors.InvalidHeaderDefect('addr-spec local part with no domain'))
        return (addr_spec, value)
    None.append(ValueTerminal('@', 'address-at-symbol'))
    (token, value) = get_domain(value[1:])
    addr_spec.append(token)
    return (addr_spec, value)


def get_obs_route(value):
    ''' obs-route = obs-domain-list ":"
        obs-domain-list = *(CFWS / ",") "@" domain *("," [CFWS] ["@" domain])

        Returns an obs-route token with the appropriate sub-tokens (that is,
        there is no obs-domain-list in the parse tree).
    '''
    obs_route = ObsRoute()
    if value:
        if value[0] == ',' or value[0] in CFWS_LEADER:
            if value[0] in CFWS_LEADER:
                (token, value) = get_cfws(value)
                obs_route.append(token)
            elif value[0] == ',':
                obs_route.append(ListSeparator)
                value = value[1:]
            if value:
                if value[0] == ',':
                    continue
                if value[0] in CFWS_LEADER:
                    continue
    if value or value[0] != '@':
        raise errors.HeaderParseError("expected obs-route domain but found '{}'".format(value))
    obs_route.append(RouteComponentMarker)
    (token, value) = get_domain(value[1:])
    obs_route.append(token)
    if value and value[0] == ',':
        obs_route.append(ListSeparator)
        value = value[1:]
        if not value:
            pass
        elif value[0] in CFWS_LEADER:
            (token, value) = get_cfws(value)
            obs_route.append(token)
        if not value:
            pass
        elif value[0] == '@':
            obs_route.append(RouteComponentMarker)
            (token, value) = get_domain(value[1:])
            obs_route.append(token)
        if value and value[0] == ',':
            continue
    if not value:
        raise errors.HeaderParseError('end of header while parsing obs-route')
    if value[0] != ':':
        raise errors.HeaderParseError("expected ':' marking end of obs-route but found '{}'".format(value))
    obs_route.append(ValueTerminal(':', 'end-of-obs-route-marker'))
    return (obs_route, value[1:])


def get_angle_addr(value):
    ''' angle-addr = [CFWS] "<" addr-spec ">" [CFWS] / obs-angle-addr
        obs-angle-addr = [CFWS] "<" obs-route addr-spec ">" [CFWS]

    '''
    angle_addr = AngleAddr()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        angle_addr.append(token)
    if value or value[0] != '<':
        raise errors.HeaderParseError("expected angle-addr but found '{}'".format(value))
    angle_addr.append(ValueTerminal('<', 'angle-addr-start'))
    value = value[1:]
    if value and value[0] == '>':
        angle_addr.append(ValueTerminal('>', 'angle-addr-end'))
        angle_addr.defects.append(errors.InvalidHeaderDefect('null addr-spec in angle-addr'))
        value = value[1:]
        return (angle_addr, value)
    
    try:
        (token, value) = get_addr_spec(value)
        angle_addr.append(token)
        if value and value[0] == '>':
            value = value[1:]
        else:
            angle_addr.defects.append(errors.InvalidHeaderDefect("missing trailing '>' on angle-addr"))
        angle_addr.append(ValueTerminal('>', 'angle-addr-end'))
        if value and value[0] in CFWS_LEADER:
            (token, value) = get_cfws(value)
            angle_addr.append(token)
        return (angle_addr, value)
    except errors.HeaderParseError:
        (token, value) = get_obs_route(value)
        angle_addr.defects.append(errors.ObsoleteHeaderDefect('obsolete route specification in angle-addr'))
    except errors.HeaderParseError:
        raise errors.HeaderParseError("expected addr-spec or obs-route but found '{}'".format(value))

    angle_addr.append(token)
    (token, value) = get_addr_spec(value)
    continue


def get_display_name(value):
    """ display-name = phrase

    Because this is simply a name-rule, we don't return a display-name
    token containing a phrase, but rather a display-name token with
    the content of the phrase.

    """
    display_name = DisplayName()
    (token, value) = get_phrase(value)
    display_name.extend(token[:])
    display_name.defects = token.defects[:]
    return (display_name, value)


def get_name_addr(value):
    ''' name-addr = [display-name] angle-addr

    '''
    name_addr = NameAddr()
    leader = None
    if not value:
        raise errors.HeaderParseError("expected name-addr but found '{}'".format(value))
    if value[0] in CFWS_LEADER:
        (leader, value) = get_cfws(value)
        if not value:
            raise errors.HeaderParseError("expected name-addr but found '{}'".format(leader))
# WARNING: Decompyle incomplete


def get_mailbox(value):
    ''' mailbox = name-addr / addr-spec

    '''
    mailbox = Mailbox()
    
    try:
        (token, value) = get_name_addr(value)
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(token.all_defects()):
            mailbox.token_type = 'invalid-mailbox'
        mailbox.append(token)
        return (mailbox, value)
    except errors.HeaderParseError:
        (token, value) = get_addr_spec(value)
    except errors.HeaderParseError:
        raise errors.HeaderParseError("expected mailbox but found '{}'".format(value))

    continue


def get_invalid_mailbox(value, endchars):
    ''' Read everything up to one of the chars in endchars.

    This is outside the formal grammar.  The InvalidMailbox TokenList that is
    returned acts like a Mailbox, but the data attributes are None.

    '''
    invalid_mailbox = InvalidMailbox()
    if value and value[0] not in endchars:
        if value[0] in PHRASE_ENDS:
            invalid_mailbox.append(ValueTerminal(value[0], 'misplaced-special'))
            value = value[1:]
        else:
            (token, value) = get_phrase(value)
            invalid_mailbox.append(token)
        if value and value[0] not in endchars:
            continue
    return (invalid_mailbox, value)


def get_mailbox_list(value):
    ''' mailbox-list = (mailbox *("," mailbox)) / obs-mbox-list
        obs-mbox-list = *([CFWS] ",") mailbox *("," [mailbox / CFWS])

    For this routine we go outside the formal grammar in order to improve error
    handling.  We recognize the end of the mailbox list only at the end of the
    value or at a \';\' (the group terminator).  This is so that we can turn
    invalid mailboxes into InvalidMailbox tokens and continue parsing any
    remaining valid mailboxes.  We also allow all mailbox entries to be null,
    and this condition is handled appropriately at a higher level.

    '''
    mailbox_list = MailboxList()
# WARNING: Decompyle incomplete


def get_group_list(value):
    ''' group-list = mailbox-list / CFWS / obs-group-list
        obs-group-list = 1*([CFWS] ",") [CFWS]

    '''
    group_list = GroupList()
    if not value:
        group_list.defects.append(errors.InvalidHeaderDefect('end of header before group-list'))
        return (group_list, value)
    leader = None
# WARNING: Decompyle incomplete


def get_group(value):
    ''' group = display-name ":" [group-list] ";" [CFWS]

    '''
    group = Group()
    (token, value) = get_display_name(value)
    if value or value[0] != ':':
        raise errors.HeaderParseError("expected ':' at end of group display name but found '{}'".format(value))
    group.append(token)
    group.append(ValueTerminal(':', 'group-display-name-terminator'))
    value = value[1:]
    if value and value[0] == ';':
        group.append(ValueTerminal(';', 'group-terminator'))
        return (group, value[1:])
    (token, value) = None(value)
    group.append(token)
    if not value:
        group.defects.append(errors.InvalidHeaderDefect('end of header in group'))
    elif value[0] != ';':
        raise errors.HeaderParseError("expected ';' at end of group but found {}".format(value))
    group.append(ValueTerminal(';', 'group-terminator'))
    value = value[1:]
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        group.append(token)
    return (group, value)


def get_address(value):
    """ address = mailbox / group

    Note that counter-intuitively, an address can be either a single address or
    a list of addresses (a group).  This is why the returned Address object has
    a 'mailboxes' attribute which treats a single address as a list of length
    one.  When you need to differentiate between to two cases, extract the single
    element, which is either a mailbox or a group token.

    """
    address = Address()
    
    try:
        (token, value) = get_group(value)
        address.append(token)
        return (address, value)
    except errors.HeaderParseError:
        (token, value) = get_mailbox(value)
    except errors.HeaderParseError:
        raise errors.HeaderParseError("expected address but found '{}'".format(value))

    continue


def get_address_list(value):
    ''' address_list = (address *("," address)) / obs-addr-list
        obs-addr-list = *([CFWS] ",") address *("," [address / CFWS])

    We depart from the formal grammar here by continuing to parse until the end
    of the input, assuming the input to be entirely composed of an
    address-list.  This is always true in email parsing, and allows us
    to skip invalid addresses to parse additional valid ones.

    '''
    address_list = AddressList()
# WARNING: Decompyle incomplete


def get_no_fold_literal(value):
    ''' no-fold-literal = "[" *dtext "]"
    '''
    no_fold_literal = NoFoldLiteral()
    if not value:
        raise errors.HeaderParseError("expected no-fold-literal but found '{}'".format(value))
    if value[0] != '[':
        raise errors.HeaderParseError("expected '[' at the start of no-fold-literal but found '{}'".format(value))
    no_fold_literal.append(ValueTerminal('[', 'no-fold-literal-start'))
    value = value[1:]
    (token, value) = get_dtext(value)
    no_fold_literal.append(token)
    if value or value[0] != ']':
        raise errors.HeaderParseError("expected ']' at the end of no-fold-literal but found '{}'".format(value))
    no_fold_literal.append(ValueTerminal(']', 'no-fold-literal-end'))
    return (no_fold_literal, value[1:])


def get_msg_id(value):
    '''msg-id = [CFWS] "<" id-left \'@\' id-right  ">" [CFWS]
       id-left = dot-atom-text / obs-id-left
       id-right = dot-atom-text / no-fold-literal / obs-id-right
       no-fold-literal = "[" *dtext "]"
    '''
    msg_id = MsgID()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        msg_id.append(token)
    if value or value[0] != '<':
        raise errors.HeaderParseError("expected msg-id but found '{}'".format(value))
    msg_id.append(ValueTerminal('<', 'msg-id-start'))
    value = value[1:]
    
    try:
        (token, value) = get_dot_atom_text(value)
        msg_id.append(token)
        if value or value[0] != '@':
            msg_id.defects.append(errors.InvalidHeaderDefect('msg-id with no id-right'))
            if value and value[0] == '>':
                msg_id.append(ValueTerminal('>', 'msg-id-end'))
                value = value[1:]
            return (msg_id, value)
        None.append(ValueTerminal('@', 'address-at-symbol'))
        value = value[1:]
        
        try:
            (token, value) = get_dot_atom_text(value)
            msg_id.append(token)
            if value and value[0] == '>':
                value = value[1:]
            else:
                msg_id.defects.append(errors.InvalidHeaderDefect("missing trailing '>' on msg-id"))
            msg_id.append(ValueTerminal('>', 'msg-id-end'))
            if value and value[0] in CFWS_LEADER:
                (token, value) = get_cfws(value)
                msg_id.append(token)
            return (msg_id, value)
            except errors.HeaderParseError:
                (token, value) = get_obs_local_part(value)
                msg_id.defects.append(errors.ObsoleteHeaderDefect('obsolete id-left in msg-id'))
            except errors.HeaderParseError:
                raise errors.HeaderParseError("expected dot-atom-text or obs-id-left but found '{}'".format(value))
            continue
        except errors.HeaderParseError:
            (token, value) = get_no_fold_literal(value)
        except errors.HeaderParseError:
            (token, value) = get_domain(value)
            msg_id.defects.append(errors.ObsoleteHeaderDefect('obsolete id-right in msg-id'))
        except errors.HeaderParseError:
            raise errors.HeaderParseError("expected dot-atom-text, no-fold-literal or obs-id-right but found '{}'".format(value))


    continue


def parse_message_id(value):
    '''message-id      =   "Message-ID:" msg-id CRLF
    '''
    message_id = MessageID()
    
    try:
        (token, value) = get_msg_id(value)
        message_id.append(token)
        if value:
            message_id.defects.append(errors.InvalidHeaderDefect('Unexpected {!r}'.format(value)))
        return message_id
    except errors.HeaderParseError:
        ex = None
        token = get_unstructured(value)
        message_id = InvalidMessageID(token)
        message_id.defects.append(errors.InvalidHeaderDefect('Invalid msg-id: {!r}'.format(ex)))
        ex = None
        del ex
        return message_id
        ex = None
        del ex



def parse_mime_version(value):
    ''' mime-version = [CFWS] 1*digit [CFWS] "." [CFWS] 1*digit [CFWS]

    '''
    mime_version = MIMEVersion()
    if not value:
        mime_version.defects.append(errors.HeaderMissingRequiredValue('Missing MIME version number (eg: 1.0)'))
        return mime_version
    if None[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        mime_version.append(token)
        if not value:
            mime_version.defects.append(errors.HeaderMissingRequiredValue('Expected MIME version number but found only CFWS'))
    digits = ''
    if value and value[0] != '.' and value[0] not in CFWS_LEADER:
        digits += value[0]
        value = value[1:]
        if value and value[0] != '.' and value[0] not in CFWS_LEADER:
            continue
    if not digits.isdigit():
        mime_version.defects.append(errors.InvalidHeaderDefect('Expected MIME major version number but found {!r}'.format(digits)))
        mime_version.append(ValueTerminal(digits, 'xtext'))
    else:
        mime_version.major = int(digits)
        mime_version.append(ValueTerminal(digits, 'digits'))
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        mime_version.append(token)
# WARNING: Decompyle incomplete


def get_invalid_parameter(value):
    """ Read everything up to the next ';'.

    This is outside the formal grammar.  The InvalidParameter TokenList that is
    returned acts like a Parameter, but the data attributes are None.

    """
    invalid_parameter = InvalidParameter()
    if value and value[0] != ';':
        if value[0] in PHRASE_ENDS:
            invalid_parameter.append(ValueTerminal(value[0], 'misplaced-special'))
            value = value[1:]
        else:
            (token, value) = get_phrase(value)
            invalid_parameter.append(token)
        if value and value[0] != ';':
            continue
    return (invalid_parameter, value)


def get_ttext(value):
    """ttext = <matches _ttext_matcher>

    We allow any non-TOKEN_ENDS in ttext, but add defects to the token's
    defects list if we find non-ttext characters.  We also register defects for
    *any* non-printables even though the RFC doesn't exclude all of them,
    because we follow the spirit of RFC 5322.

    """
    m = _non_token_end_matcher(value)
    if not m:
        raise errors.HeaderParseError("expected ttext but found '{}'".format(value))
    ttext = m.group()
    value = value[len(ttext):]
    ttext = ValueTerminal(ttext, 'ttext')
    _validate_xtext(ttext)
    return (ttext, value)


def get_token(value):
    """token = [CFWS] 1*ttext [CFWS]

    The RFC equivalent of ttext is any US-ASCII chars except space, ctls, or
    tspecials.  We also exclude tabs even though the RFC doesn't.

    The RFC implies the CFWS but is not explicit about it in the BNF.

    """
    mtoken = Token()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        mtoken.append(token)
    if value and value[0] in TOKEN_ENDS:
        raise errors.HeaderParseError("expected token but found '{}'".format(value))
    (token, value) = get_ttext(value)
    mtoken.append(token)
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        mtoken.append(token)
    return (mtoken, value)


def get_attrtext(value):
    """attrtext = 1*(any non-ATTRIBUTE_ENDS character)

    We allow any non-ATTRIBUTE_ENDS in attrtext, but add defects to the
    token's defects list if we find non-attrtext characters.  We also register
    defects for *any* non-printables even though the RFC doesn't exclude all of
    them, because we follow the spirit of RFC 5322.

    """
    m = _non_attribute_end_matcher(value)
    if not m:
        raise errors.HeaderParseError('expected attrtext but found {!r}'.format(value))
    attrtext = m.group()
    value = value[len(attrtext):]
    attrtext = ValueTerminal(attrtext, 'attrtext')
    _validate_xtext(attrtext)
    return (attrtext, value)


def get_attribute(value):
    ''' [CFWS] 1*attrtext [CFWS]

    This version of the BNF makes the CFWS explicit, and as usual we use a
    value terminal for the actual run of characters.  The RFC equivalent of
    attrtext is the token characters, with the subtraction of \'*\', "\'", and \'%\'.
    We include tab in the excluded set just as we do for token.

    '''
    attribute = Attribute()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        attribute.append(token)
    if value and value[0] in ATTRIBUTE_ENDS:
        raise errors.HeaderParseError("expected token but found '{}'".format(value))
    (token, value) = get_attrtext(value)
    attribute.append(token)
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        attribute.append(token)
    return (attribute, value)


def get_extended_attrtext(value):
    """attrtext = 1*(any non-ATTRIBUTE_ENDS character plus '%')

    This is a special parsing routine so that we get a value that
    includes % escapes as a single string (which we decode as a single
    string later).

    """
    m = _non_extended_attribute_end_matcher(value)
    if not m:
        raise errors.HeaderParseError('expected extended attrtext but found {!r}'.format(value))
    attrtext = m.group()
    value = value[len(attrtext):]
    attrtext = ValueTerminal(attrtext, 'extended-attrtext')
    _validate_xtext(attrtext)
    return (attrtext, value)


def get_extended_attribute(value):
    ''' [CFWS] 1*extended_attrtext [CFWS]

    This is like the non-extended version except we allow % characters, so that
    we can pick up an encoded value as a single string.

    '''
    attribute = Attribute()
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        attribute.append(token)
    if value and value[0] in EXTENDED_ATTRIBUTE_ENDS:
        raise errors.HeaderParseError("expected token but found '{}'".format(value))
    (token, value) = get_extended_attrtext(value)
    attribute.append(token)
    if value and value[0] in CFWS_LEADER:
        (token, value) = get_cfws(value)
        attribute.append(token)
    return (attribute, value)


def get_section(value):
    """ '*' digits

    The formal BNF is more complicated because leading 0s are not allowed.  We
    check for that and add a defect.  We also assume no CFWS is allowed between
    the '*' and the digits, though the RFC is not crystal clear on that.
    The caller should already have dealt with leading CFWS.

    """
    section = Section()
    if value or value[0] != '*':
        raise errors.HeaderParseError('Expected section but found {}'.format(value))
    section.append(ValueTerminal('*', 'section-marker'))
    value = value[1:]
    if not value or value[0].isdigit():
        raise errors.HeaderParseError('Expected section number but found {}'.format(value))
    digits = ''
    if value and value[0].isdigit():
        digits += value[0]
        value = value[1:]
        if value and value[0].isdigit():
            continue
    if digits[0] == '0' and digits != '0':
        section.defects.append(errors.InvalidHeaderDefect('section number has an invalid leading 0'))
    section.number = int(digits)
    section.append(ValueTerminal(digits, 'digits'))
    return (section, value)


def get_value(value):
    ''' quoted-string / attribute

    '''
    v = Value()
    if not value:
        raise errors.HeaderParseError('Expected value but found end of string')
    leader = None
    if value[0] in CFWS_LEADER:
        (leader, value) = get_cfws(value)
    if not value:
        raise errors.HeaderParseError('Expected value but found only {}'.format(leader))
    if value[0] == '"':
        (token, value) = get_quoted_string(value)
    else:
        (token, value) = get_extended_attribute(value)
# WARNING: Decompyle incomplete


def get_parameter(value):
    ''' attribute [section] ["*"] [CFWS] "=" value

    The CFWS is implied by the RFC but not made explicit in the BNF.  This
    simplified form of the BNF from the RFC is made to conform with the RFC BNF
    through some extra checks.  We do it this way because it makes both error
    recovery and working with the resulting parse tree easier.
    '''
    param = Parameter()
    (token, value) = get_attribute(value)
    param.append(token)
    if value or value[0] == ';':
        param.defects.append(errors.InvalidHeaderDefect('Parameter contains name ({}) but no value'.format(token)))
        return (param, value)
# WARNING: Decompyle incomplete


def parse_mime_parameters(value):
    ''' parameter *( ";" parameter )

    That BNF is meant to indicate this routine should only be called after
    finding and handling the leading \';\'.  There is no corresponding rule in
    the formal RFC grammar, but it is more convenient for us for the set of
    parameters to be treated as its own TokenList.

    This is \'parse\' routine because it consumes the remaining value, but it
    would never be called to parse a full header.  Instead it is called to
    parse everything after the non-parameter value of a specific MIME header.

    '''
    mime_parameters = MimeParameters()
# WARNING: Decompyle incomplete


def _find_mime_parameters(tokenlist, value):
    '''Do our best to find the parameters in an invalid MIME header

    '''
    if value and value[0] != ';':
        if value[0] in PHRASE_ENDS:
            tokenlist.append(ValueTerminal(value[0], 'misplaced-special'))
            value = value[1:]
        else:
            (token, value) = get_phrase(value)
            tokenlist.append(token)
        if value and value[0] != ';':
            continue
    if not value:
        return None
    tokenlist.append(ValueTerminal(';', 'parameter-separator'))
    tokenlist.append(parse_mime_parameters(value[1:]))


def parse_content_type_header(value):
    ''' maintype "/" subtype *( ";" parameter )

    The maintype and substype are tokens.  Theoretically they could
    be checked against the official IANA list + x-token, but we
    don\'t do that.
    '''
    ctype = ContentType()
    if not value:
        ctype.defects.append(errors.HeaderMissingRequiredValue('Missing content type specification'))
        return ctype
    
    try:
        (token, value) = get_token(value)
        ctype.append(token)
        if value or value[0] != '/':
            ctype.defects.append(errors.InvalidHeaderDefect('Invalid content type'))
            if value:
                _find_mime_parameters(ctype, value)
            return ctype
        ctype.maintype = None.value.strip().lower()
        ctype.append(ValueTerminal('/', 'content-type-separator'))
        value = value[1:]
        
        try:
            (token, value) = get_token(value)
            ctype.append(token)
            ctype.subtype = token.value.strip().lower()
            if not value:
                return ctype
            if None[0] != ';':
                ctype.defects.append(errors.InvalidHeaderDefect('Only parameters are valid after content type, but found {!r}'.format(value)))
                del ctype.maintype
                del ctype.subtype
                _find_mime_parameters(ctype, value)
                return ctype
            None.append(ValueTerminal(';', 'parameter-separator'))
            ctype.append(parse_mime_parameters(value[1:]))
            return ctype
            except errors.HeaderParseError:
                ctype.defects.append(errors.InvalidHeaderDefect('Expected content maintype but found {!r}'.format(value)))
                _find_mime_parameters(ctype, value)
                return 
        except errors.HeaderParseError:
            ctype.defects.append(errors.InvalidHeaderDefect('Expected content subtype but found {!r}'.format(value)))
            _find_mime_parameters(ctype, value)
            return 




def parse_content_disposition_header(value):
    ''' disposition-type *( ";" parameter )

    '''
    disp_header = ContentDisposition()
    if not value:
        disp_header.defects.append(errors.HeaderMissingRequiredValue('Missing content disposition'))
        return disp_header
    
    try:
        (token, value) = get_token(value)
        disp_header.append(token)
        disp_header.content_disposition = token.value.strip().lower()
        if not value:
            return disp_header
        if None[0] != ';':
            disp_header.defects.append(errors.InvalidHeaderDefect('Only parameters are valid after content disposition, but found {!r}'.format(value)))
            _find_mime_parameters(disp_header, value)
            return disp_header
        None.append(ValueTerminal(';', 'parameter-separator'))
        disp_header.append(parse_mime_parameters(value[1:]))
        return disp_header
    except errors.HeaderParseError:
        disp_header.defects.append(errors.InvalidHeaderDefect('Expected content disposition but found {!r}'.format(value)))
        _find_mime_parameters(disp_header, value)
        return 



def parse_content_transfer_encoding_header(value):
    ''' mechanism

    '''
    cte_header = ContentTransferEncoding()
    if not value:
        cte_header.defects.append(errors.HeaderMissingRequiredValue('Missing content transfer encoding'))
        return cte_header
    
    try:
        (token, value) = get_token(value)
        cte_header.append(token)
        cte_header.cte = token.value.strip().lower()
        if not value:
            return cte_header
        if None:
            cte_header.defects.append(errors.InvalidHeaderDefect('Extra text after content transfer encoding'))
            if value[0] in PHRASE_ENDS:
                cte_header.append(ValueTerminal(value[0], 'misplaced-special'))
                value = value[1:]
            else:
                (token, value) = get_phrase(value)
                cte_header.append(token)
            if value:
                continue
        return cte_header
    except errors.HeaderParseError:
        cte_header.defects.append(errors.InvalidHeaderDefect('Expected content transfer encoding but found {!r}'.format(value)))
        continue



def _steal_trailing_WSP_if_exists(lines):
    wsp = ''
    if lines and lines[-1] and lines[-1][-1] in WSP:
        wsp = lines[-1][-1]
        lines[-1] = lines[-1][:-1]
    return wsp


def _refold_parse_tree(parse_tree, *, policy):
    '''Return string of contents of parse_tree folded according to RFC rules.

    '''
    if not policy.max_line_length:
        policy.max_line_length
    maxlen = sys.maxsize
    encoding = 'utf-8' if policy.utf8 else 'us-ascii'
    lines = [
        '']
    leading_whitespace = ''
    last_ew = None
    last_charset = None
    wrap_as_ew_blocked = 0
    want_encoding = False
    end_ew_not_allowed = Terminal('', 'wrap_as_ew_blocked')
    parts = list(parse_tree)
# WARNING: Decompyle incomplete


def _fold_as_ew(to_encode, lines, maxlen, last_ew, ew_combine_allowed, charset, leading_whitespace):
    '''Fold string to_encode into lines as encoded word, combining if allowed.
    Return the new value for last_ew, or None if ew_combine_allowed is False.

    If there is already an encoded word in the last line of lines (indicated by
    a non-None value for last_ew) and ew_combine_allowed is true, decode the
    existing ew, combine it with to_encode, and re-encode.  Otherwise, encode
    to_encode.  In either case, split to_encode as necessary so that the
    encoded segments fit within maxlen.

    '''
    pass
# WARNING: Decompyle incomplete


def _fold_mime_parameters(part, lines, maxlen, encoding):
    """Fold TokenList 'part' into the 'lines' list as mime parameters.

    Using the decoded list of parameters and values, format them according to
    the RFC rules, including using RFC2231 encoding if the value cannot be
    expressed in 'encoding' and/or the parameter+value is too long to fit
    within 'maxlen'.

    """
    for name, value in part.params:
        if not lines[-1].rstrip().endswith(';'):
            pass
        encoding = part.params
        error_handler = 'strict'
        value.encode(encoding)
        encoding_required = False
        if encoding_required:
            encoded_value = urllib.parse.quote(value, safe = '', errors = error_handler)
            tstr = "{}*={}''{}".format(name, charset, encoded_value)
        else:
            tstr = '{}={}'.format(name, quote_string(value))
        if len(lines[-1]) + len(tstr) + 1 < maxlen:
            lines[-1] = lines[-1] + ' ' + tstr
            continue
        if len(tstr) + 2 <= maxlen:
            lines.append(' ' + tstr)
            continue
        section = 0
        extra_chrome = charset + "''"
        if not value:
            continue
        chrome_len = len(name) + len(str(section)) + 3 + len(extra_chrome)
        if maxlen <= chrome_len + 3:
            maxlen = 78
        splitpoint = maxlen - chrome_len - 2
        maxchars = maxlen - chrome_len - 2
        partial = value[:splitpoint]
        encoded_value = urllib.parse.quote(partial, safe = '', errors = error_handler)
        if len(encoded_value) <= maxchars:
            pass
        else:
            splitpoint -= 1
        lines.append(' {}*{}*={}{}'.format(name, section, extra_chrome, encoded_value))
        extra_chrome = ''
        section += 1
        value = value[splitpoint:]
        if value:
            pass
        if value:
            continue
    continue
    return None
    except UnicodeEncodeError:
        True = None
        if utils._has_surrogates(value):
            charset = 'unknown-8bit'
            error_handler = 'surrogateescape'
        else:
            charset = 'utf-8'
        continue

