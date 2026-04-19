# Source Generated with Decompyle++
# File: headerregistry.pyc (Python 3.12)

__doc__ = 'Representing and manipulating email headers via custom objects.\n\nThis module provides an implementation of the HeaderRegistry API.\nThe implementation is designed to flexibly follow RFC5322 rules.\n'
from types import MappingProxyType
from email import utils
from email import errors
from email import _header_value_parser as parser

class Address:
    
    def __init__(self, display_name, username, domain, addr_spec = ('', '', '', None)):
        """Create an object representing a full email address.

        An address can have a 'display_name', a 'username', and a 'domain'.  In
        addition to specifying the username and domain separately, they may be
        specified together by using the addr_spec keyword *instead of* the
        username and domain keywords.  If an addr_spec string is specified it
        must be properly quoted according to RFC 5322 rules; an error will be
        raised if it is not.

        An Address object has display_name, username, domain, and addr_spec
        attributes, all of which are read-only.  The addr_spec and the string
        value of the object are both quoted according to RFC5322 rules, but
        without any Content Transfer Encoding.

        """
        inputs = ''.join(filter(None, (display_name, username, domain, addr_spec)))
        if '\r' in inputs or '\n' in inputs:
            raise ValueError('invalid arguments; address parts cannot contain CR or LF')
    # WARNING: Decompyle incomplete

    display_name = (lambda self: self._display_name)()
    username = (lambda self: self._username)()
    domain = (lambda self: self._domain)()
    addr_spec = (lambda self: lp = self.usernameif not parser.DOT_ATOM_ENDS.isdisjoint(lp):
lp = parser.quote_string(lp)if self.domain:
lp + '@' + self.domainif not None:
'<>'lp)()
    
    def __repr__(self):
        return '{}(display_name={!r}, username={!r}, domain={!r})'.format(self.__class__.__name__, self.display_name, self.username, self.domain)

    
    def __str__(self):
        disp = self.display_name
        if not parser.SPECIALS.isdisjoint(disp):
            disp = parser.quote_string(disp)
        if disp:
            addr_spec = '' if self.addr_spec == '<>' else self.addr_spec
            return '{} <{}>'.format(disp, addr_spec)
        return None.addr_spec

    
    def __eq__(self, other):
        if not isinstance(other, Address):
            return NotImplemented
        if None.display_name == other.display_name:
            None.display_name == other.display_name
            if self.username == other.username:
                self.username == other.username
        return self.domain == other.domain



class Group:
    
    def __init__(self, display_name, addresses = (None, None)):
        '''Create an object representing an address group.

        An address group consists of a display_name followed by colon and a
        list of addresses (see Address) terminated by a semi-colon.  The Group
        is created by specifying a display_name and a possibly empty list of
        Address objects.  A Group can also be used to represent a single
        address that is not in a group, which is convenient when manipulating
        lists that are a combination of Groups and individual Addresses.  In
        this case the display_name should be set to None.  In particular, the
        string representation of a Group whose display_name is None is the same
        as the Address object, if there is one and only one Address object in
        the addresses list.

        '''
        self._display_name = display_name
        if addresses:
            self._addresses = tuple(addresses)
            return None
        self._addresses = tuple()

    display_name = (lambda self: self._display_name)()
    addresses = (lambda self: self._addresses)()
    
    def __repr__(self):
        return '{}(display_name={!r}, addresses={!r}'.format(self.__class__.__name__, self.display_name, self.addresses)

    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        if not isinstance(other, Group):
            return NotImplemented
        if None.display_name == other.display_name:
            None.display_name == other.display_name
        return self.addresses == other.addresses



class BaseHeader(str):
    """Base class for message headers.

    Implements generic behavior and provides tools for subclasses.

    A subclass must define a classmethod named 'parse' that takes an unfolded
    value string and a dictionary as its arguments.  The dictionary will
    contain one key, 'defects', initialized to an empty list.  After the call
    the dictionary must contain two additional keys: parse_tree, set to the
    parse tree obtained from parsing the header, and 'decoded', set to the
    string value of the idealized representation of the data from the value.
    (That is, encoded words are decoded, and values that have canonical
    representations are so represented.)

    The defects key is intended to collect parsing defects, which the message
    parser will subsequently dispose of as appropriate.  The parser should not,
    insofar as practical, raise any errors.  Defects should be added to the
    list instead.  The standard header parsers register defects for RFC
    compliance issues, for obsolete RFC syntax, and for unrecoverable parsing
    errors.

    The parse method may add additional keys to the dictionary.  In this case
    the subclass must define an 'init' method, which will be passed the
    dictionary as its keyword arguments.  The method should use (usually by
    setting them as the value of similarly named attributes) and remove all the
    extra keys added by its parse method, and then use super to call its parent
    class with the remaining arguments and keywords.

    The subclass should also make sure that a 'max_count' attribute is defined
    that is either None or 1. XXX: need to better define this API.

    """
    
    def __new__(cls, name, value):
        kwds = {
            'defects': [] }
        cls.parse(value, kwds)
        if utils._has_surrogates(kwds['decoded']):
            kwds['decoded'] = utils._sanitize(kwds['decoded'])
        self = str.__new__(cls, kwds['decoded'])
        del kwds['decoded']
    # WARNING: Decompyle incomplete

    
    def init(self, name, *, parse_tree, defects):
        self._name = name
        self._parse_tree = parse_tree
        self._defects = defects

    name = (lambda self: self._name)()
    defects = (lambda self: tuple(self._defects))()
    
    def __reduce__(self):
        return (_reconstruct_header, (self.__class__.__name__, self.__class__.__bases__, str(self)), self.__getstate__())

    _reconstruct = (lambda cls, value: str.__new__(cls, value))()
    
    def fold(self, *, policy):
        '''Fold header according to policy.

        The parsed representation of the header is folded according to
        RFC5322 rules, as modified by the policy.  If the parse tree
        contains surrogateescaped bytes, the bytes are CTE encoded using
        the charset \'unknown-8bit".

        Any non-ASCII characters in the parse tree are CTE encoded using
        charset utf-8. XXX: make this a policy setting.

        The returned value is an ASCII-only string possibly containing linesep
        characters, and ending with a linesep character.  The string includes
        the header name and the \': \' separator.

        '''
        header = parser.Header([
            parser.HeaderLabel([
                parser.ValueTerminal(self.name, 'header-name'),
                parser.ValueTerminal(':', 'header-sep')])])
        if self._parse_tree:
            header.append(parser.CFWSList([
                parser.WhiteSpaceTerminal(' ', 'fws')]))
        header.append(self._parse_tree)
        return header.fold(policy = policy)



def _reconstruct_header(cls_name, bases, value):
    return type(cls_name, bases, { })._reconstruct(value)


class UnstructuredHeader:
    max_count = None
    value_parser = staticmethod(parser.get_unstructured)
    parse = (lambda cls, value, kwds: kwds['parse_tree'] = cls.value_parser(value)kwds['decoded'] = str(kwds['parse_tree']))()


class UniqueUnstructuredHeader(UnstructuredHeader):
    max_count = 1


class DateHeader:
    pass
# WARNING: Decompyle incomplete


class UniqueDateHeader(DateHeader):
    max_count = 1


class AddressHeader:
    pass
# WARNING: Decompyle incomplete


class UniqueAddressHeader(AddressHeader):
    max_count = 1


class SingleAddressHeader(AddressHeader):
    address = (lambda self: if len(self.addresses) != 1:
raise ValueError('value of single address header {} is not a single address'.format(self.name))self.addresses[0])()


class UniqueSingleAddressHeader(SingleAddressHeader):
    max_count = 1


class MIMEVersionHeader:
    pass
# WARNING: Decompyle incomplete


class ParameterizedMIMEHeader:
    pass
# WARNING: Decompyle incomplete


class ContentTypeHeader(ParameterizedMIMEHeader):
    pass
# WARNING: Decompyle incomplete


class ContentDispositionHeader(ParameterizedMIMEHeader):
    pass
# WARNING: Decompyle incomplete


class ContentTransferEncodingHeader:
    pass
# WARNING: Decompyle incomplete


class MessageIDHeader:
    max_count = 1
    value_parser = staticmethod(parser.parse_message_id)
    parse = (lambda cls, value, kwds: kwds['parse_tree'] = cls.value_parser(value)parse_tree = cls.value_parser(value)kwds['decoded'] = str(parse_tree)kwds['defects'].extend(parse_tree.all_defects))()

# WARNING: Decompyle incomplete
