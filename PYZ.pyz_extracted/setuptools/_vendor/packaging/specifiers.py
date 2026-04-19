# Source Generated with Decompyle++
# File: specifiers.pyc (Python 3.12)

'''
.. testsetup::

    from packaging.specifiers import Specifier, SpecifierSet, InvalidSpecifier
    from packaging.version import Version
'''
from __future__ import annotations
import abc
import itertools
import re
from typing import Callable, Iterable, Iterator, TypeVar, Union
from utils import canonicalize_version
from version import Version
UnparsedVersion = Union[(Version, str)]
UnparsedVersionVar = TypeVar('UnparsedVersionVar', bound = UnparsedVersion)
CallableOperator = Callable[([
    Version,
    str], bool)]

def _coerce_version(version = None):
    if not isinstance(version, Version):
        version = Version(version)
    return version


class InvalidSpecifier(ValueError):
    '''
    Raised when attempting to create a :class:`Specifier` with a specifier
    string that is invalid.

    >>> Specifier("lolwat")
    Traceback (most recent call last):
        ...
    packaging.specifiers.InvalidSpecifier: Invalid specifier: \'lolwat\'
    '''
    pass


def BaseSpecifier():
    '''BaseSpecifier'''
    __str__ = (lambda self = None: pass)()
    __hash__ = (lambda self = None: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    prereleases = (lambda self = None: pass)()()
    prereleases = (lambda self = None, value = None: pass)()
    contains = (lambda self = None, item = None, prereleases = abc.abstractmethod: pass)()
    filter = (lambda self = None, iterable = None, prereleases = abc.abstractmethod: pass)()

BaseSpecifier = <NODE:27>(BaseSpecifier, 'BaseSpecifier', metaclass = abc.ABCMeta)

class Specifier(BaseSpecifier):
    '''This class abstracts handling of version specifiers.

    .. tip::

        It is generally not required to instantiate this manually. You should instead
        prefer to work with :class:`SpecifierSet` instead, which can parse
        comma-separated version specifiers (which is what package metadata contains).
    '''
    _operator_regex_str = '\n        (?P<operator>(~=|==|!=|<=|>=|<|>|===))\n        '
    _version_regex_str = "\n        (?P<version>\n            (?:\n                # The identity operators allow for an escape hatch that will\n                # do an exact string match of the version you wish to install.\n                # This will not be parsed by PEP 440 and we cannot determine\n                # any semantic meaning from it. This operator is discouraged\n                # but included entirely as an escape hatch.\n                (?<====)  # Only match for the identity operator\n                \\s*\n                [^\\s;)]*  # The arbitrary version can be just about anything,\n                          # we match everything except for whitespace, a\n                          # semi-colon for marker support, and a closing paren\n                          # since versions can be enclosed in them.\n            )\n            |\n            (?:\n                # The (non)equality operators allow for wild card and local\n                # versions to be specified so we have to define these two\n                # operators separately to enable that.\n                (?<===|!=)            # Only match for equals and not equals\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)*   # release\n\n                # You cannot use a wild card and a pre-release, post-release, a dev or\n                # local version together so group them with a | and make them optional.\n                (?:\n                    \\.\\*  # Wild card syntax of .*\n                    |\n                    (?:                                  # pre release\n                        [-_\\.]?\n                        (alpha|beta|preview|pre|a|b|c|rc)\n                        [-_\\.]?\n                        [0-9]*\n                    )?\n                    (?:                                  # post release\n                        (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                    )?\n                    (?:[-_\\.]?dev[-_\\.]?[0-9]*)?         # dev release\n                    (?:\\+[a-z0-9]+(?:[-_\\.][a-z0-9]+)*)? # local\n                )?\n            )\n            |\n            (?:\n                # The compatible operator requires at least two digits in the\n                # release segment.\n                (?<=~=)               # Only match for the compatible operator\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)+   # release  (We have a + instead of a *)\n                (?:                   # pre release\n                    [-_\\.]?\n                    (alpha|beta|preview|pre|a|b|c|rc)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n                (?:[-_\\.]?dev[-_\\.]?[0-9]*)?          # dev release\n            )\n            |\n            (?:\n                # All other operators only allow a sub set of what the\n                # (non)equality operators do. Specifically they do not allow\n                # local versions to be specified nor do they allow the prefix\n                # matching wild cards.\n                (?<!==|!=|~=)         # We have special cases for these\n                                      # operators so we want to make sure they\n                                      # don't match here.\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)*   # release\n                (?:                   # pre release\n                    [-_\\.]?\n                    (alpha|beta|preview|pre|a|b|c|rc)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n                (?:[-_\\.]?dev[-_\\.]?[0-9]*)?          # dev release\n            )\n        )\n        "
    _regex = re.compile('^\\s*' + _operator_regex_str + _version_regex_str + '\\s*$', re.VERBOSE | re.IGNORECASE)
    _operators = {
        '~=': 'compatible',
        '==': 'equal',
        '!=': 'not_equal',
        '<=': 'less_than_equal',
        '>=': 'greater_than_equal',
        '<': 'less_than',
        '>': 'greater_than',
        '===': 'arbitrary' }
    
    def __init__(self = None, spec = None, prereleases = None):
        '''Initialize a Specifier instance.

        :param spec:
            The string representation of a specifier which will be parsed and
            normalized before use.
        :param prereleases:
            This tells the specifier if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.
        :raises InvalidSpecifier:
            If the given specifier is invalid (i.e. bad syntax).
        '''
        match = self._regex.search(spec)
        if not match:
            raise InvalidSpecifier(f'''Invalid specifier: {spec!r}''')
        self._spec = (match.group('operator').strip(), match.group('version').strip())
        self._prereleases = prereleases

    prereleases = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    prereleases = (lambda self = None, value = None: self._prereleases = value)()
    operator = (lambda self = None: self._spec[0])()
    version = (lambda self = None: self._spec[1])()
    
    def __repr__(self = None):
        """A representation of the Specifier that shows all internal state.

        >>> Specifier('>=1.0.0')
        <Specifier('>=1.0.0')>
        >>> Specifier('>=1.0.0', prereleases=False)
        <Specifier('>=1.0.0', prereleases=False)>
        >>> Specifier('>=1.0.0', prereleases=True)
        <Specifier('>=1.0.0', prereleases=True)>
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        """A string representation of the Specifier that can be round-tripped.

        >>> str(Specifier('>=1.0.0'))
        '>=1.0.0'
        >>> str(Specifier('>=1.0.0', prereleases=False))
        '>=1.0.0'
        """
        pass
    # WARNING: Decompyle incomplete

    _canonical_spec = (lambda self = None: canonical_version = canonicalize_version(self._spec[1], strip_trailing_zero = self._spec[0] != '~=')(self._spec[0], canonical_version))()
    
    def __hash__(self = None):
        return hash(self._canonical_spec)

    
    def __eq__(self = None, other = None):
        '''Whether or not the two Specifier-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> Specifier("==1.2.3") == Specifier("== 1.2.3.0")
        True
        >>> (Specifier("==1.2.3", prereleases=False) ==
        ...  Specifier("==1.2.3", prereleases=True))
        True
        >>> Specifier("==1.2.3") == "==1.2.3"
        True
        >>> Specifier("==1.2.3") == Specifier("==1.2.4")
        False
        >>> Specifier("==1.2.3") == Specifier("~=1.2.3")
        False
        '''
        if isinstance(other, str):
            
            try:
                other = self.__class__(str(other))
            if not isinstance(other, self.__class__):
                return NotImplemented
            return None._canonical_spec == other._canonical_spec
            except InvalidSpecifier:
                return 


    
    def _get_operator(self = None, op = None):
        operator_callable = getattr(self, f'''_compare_{self._operators[op]}''')
        return operator_callable

    
    def _compare_compatible(self = None, prospective = None, spec = None):
        prefix = _version_join(list(itertools.takewhile(_is_not_suffix, _version_split(spec)))[:-1])
        prefix += '.*'
        if self._get_operator('>=')(prospective, spec):
            self._get_operator('>=')(prospective, spec)
        return self._get_operator('==')(prospective, prefix)

    
    def _compare_equal(self = None, prospective = None, spec = None):
        if spec.endswith('.*'):
            normalized_prospective = canonicalize_version(prospective.public, strip_trailing_zero = False)
            normalized_spec = canonicalize_version(spec[:-2], strip_trailing_zero = False)
            split_spec = _version_split(normalized_spec)
            split_prospective = _version_split(normalized_prospective)
            (padded_prospective, _) = _pad_version(split_prospective, split_spec)
            shortened_prospective = padded_prospective[:len(split_spec)]
            return shortened_prospective == split_spec
        spec_version = None(spec)
        if not spec_version.local:
            prospective = Version(prospective.public)
        return prospective == spec_version

    
    def _compare_not_equal(self = None, prospective = None, spec = None):
        return not self._compare_equal(prospective, spec)

    
    def _compare_less_than_equal(self = None, prospective = None, spec = None):
        return Version(prospective.public) <= Version(spec)

    
    def _compare_greater_than_equal(self = None, prospective = None, spec = None):
        return Version(prospective.public) >= Version(spec)

    
    def _compare_less_than(self = None, prospective = None, spec_str = None):
        spec = Version(spec_str)
        if not prospective < spec:
            return False
        if spec.is_prerelease and prospective.is_prerelease and Version(prospective.base_version) == Version(spec.base_version):
            return False
        return True

    
    def _compare_greater_than(self = None, prospective = None, spec_str = None):
        spec = Version(spec_str)
        if not prospective > spec:
            return False
        if spec.is_postrelease and prospective.is_postrelease and Version(prospective.base_version) == Version(spec.base_version):
            return False
    # WARNING: Decompyle incomplete

    
    def _compare_arbitrary(self = None, prospective = None, spec = None):
        return str(prospective).lower() == str(spec).lower()

    
    def __contains__(self = None, item = None):
        '''Return whether or not the item is contained in this specifier.

        :param item: The item to check for.

        This is used for the ``in`` operator and behaves the same as
        :meth:`contains` with no ``prereleases`` argument passed.

        >>> "1.2.3" in Specifier(">=1.2.3")
        True
        >>> Version("1.2.3") in Specifier(">=1.2.3")
        True
        >>> "1.0.0" in Specifier(">=1.2.3")
        False
        >>> "1.3.0a1" in Specifier(">=1.2.3")
        False
        >>> "1.3.0a1" in Specifier(">=1.2.3", prereleases=True)
        True
        '''
        return self.contains(item)

    
    def contains(self = None, item = None, prereleases = None):
        '''Return whether or not the item is contained in this specifier.

        :param item:
            The item to check for, which can be a version string or a
            :class:`Version` instance.
        :param prereleases:
            Whether or not to match prereleases with this Specifier. If set to
            ``None`` (the default), it uses :attr:`prereleases` to determine
            whether or not prereleases are allowed.

        >>> Specifier(">=1.2.3").contains("1.2.3")
        True
        >>> Specifier(">=1.2.3").contains(Version("1.2.3"))
        True
        >>> Specifier(">=1.2.3").contains("1.0.0")
        False
        >>> Specifier(">=1.2.3").contains("1.3.0a1")
        False
        >>> Specifier(">=1.2.3", prereleases=True).contains("1.3.0a1")
        True
        >>> Specifier(">=1.2.3").contains("1.3.0a1", prereleases=True)
        True
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self = None, iterable = None, prereleases = None):
        '''Filter items in the given iterable, that match the specifier.

        :param iterable:
            An iterable that can contain version strings and :class:`Version` instances.
            The items in the iterable will be filtered according to the specifier.
        :param prereleases:
            Whether or not to allow prereleases in the returned iterator. If set to
            ``None`` (the default), it will be intelligently decide whether to allow
            prereleases or not (based on the :attr:`prereleases` attribute, and
            whether the only versions matching are prereleases).

        This method is smarter than just ``filter(Specifier().contains, [...])``
        because it implements the rule from :pep:`440` that a prerelease item
        SHOULD be accepted if no other versions match the given specifier.

        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.3", "1.5a1"]))
        [\'1.3\']
        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.2.3", "1.3", Version("1.4")]))
        [\'1.2.3\', \'1.3\', <Version(\'1.4\')>]
        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.5a1"]))
        [\'1.5a1\']
        >>> list(Specifier(">=1.2.3").filter(["1.3", "1.5a1"], prereleases=True))
        [\'1.3\', \'1.5a1\']
        >>> list(Specifier(">=1.2.3", prereleases=True).filter(["1.3", "1.5a1"]))
        [\'1.3\', \'1.5a1\']
        '''
        pass
    # WARNING: Decompyle incomplete


_prefix_regex = re.compile('^([0-9]+)((?:a|b|c|rc)[0-9]+)$')

def _version_split(version = None):
    '''Split version into components.

    The split components are intended for version comparison. The logic does
    not attempt to retain the original version string, so joining the
    components back with :func:`_version_join` may not produce the original
    version string.
    '''
    result = []
    (epoch, _, rest) = version.rpartition('!')
    if not epoch:
        epoch
    result.append('0')
    for item in rest.split('.'):
        match = _prefix_regex.search(item)
        if match:
            result.extend(match.groups())
            continue
        result.append(item)
    return result


def _version_join(components = None):
    '''Join split version components into a version string.

    This function assumes the input came from :func:`_version_split`, where the
    first component must be the epoch (either empty or numeric), and all other
    components numeric.
    '''
    pass
# WARNING: Decompyle incomplete


def _is_not_suffix(segment = None):
    pass
# WARNING: Decompyle incomplete


def _pad_version(left = None, right = None):
    right_split = []
    left_split = []
    left_split.append(list(itertools.takewhile((lambda x: x.isdigit()), left)))
    right_split.append(list(itertools.takewhile((lambda x: x.isdigit()), right)))
    left_split.append(left[len(left_split[0]):])
    right_split.append(right[len(right_split[0]):])
    left_split.insert(1, [
        '0'] * max(0, len(right_split[0]) - len(left_split[0])))
    right_split.insert(1, [
        '0'] * max(0, len(left_split[0]) - len(right_split[0])))
    return (list(itertools.chain.from_iterable(left_split)), list(itertools.chain.from_iterable(right_split)))


class SpecifierSet(BaseSpecifier):
    '''This class abstracts handling of a set of version specifiers.

    It can be passed a single specifier (``>=3.0``), a comma-separated list of
    specifiers (``>=3.0,!=3.1``), or no specifier at all.
    '''
    
    def __init__(self = None, specifiers = None, prereleases = None):
        '''Initialize a SpecifierSet instance.

        :param specifiers:
            The string representation of a specifier or a comma-separated list of
            specifiers which will be parsed and normalized before use.
            May also be an iterable of ``Specifier`` instances, which will be used
            as is.
        :param prereleases:
            This tells the SpecifierSet if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.

        :raises InvalidSpecifier:
            If the given ``specifiers`` are not parseable than this exception will be
            raised.
        '''
        pass
    # WARNING: Decompyle incomplete

    prereleases = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    prereleases = (lambda self = None, value = None: self._prereleases = value)()
    
    def __repr__(self = None):
        """A representation of the specifier set that shows all internal state.

        Note that the ordering of the individual specifiers within the set may not
        match the input string.

        >>> SpecifierSet('>=1.0.0,!=2.0.0')
        <SpecifierSet('!=2.0.0,>=1.0.0')>
        >>> SpecifierSet('>=1.0.0,!=2.0.0', prereleases=False)
        <SpecifierSet('!=2.0.0,>=1.0.0', prereleases=False)>
        >>> SpecifierSet('>=1.0.0,!=2.0.0', prereleases=True)
        <SpecifierSet('!=2.0.0,>=1.0.0', prereleases=True)>
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        '''A string representation of the specifier set that can be round-tripped.

        Note that the ordering of the individual specifiers within the set may not
        match the input string.

        >>> str(SpecifierSet(">=1.0.0,!=1.0.1"))
        \'!=1.0.1,>=1.0.0\'
        >>> str(SpecifierSet(">=1.0.0,!=1.0.1", prereleases=False))
        \'!=1.0.1,>=1.0.0\'
        '''
        return sorted((lambda .0: pass# WARNING: Decompyle incomplete
)(self._specs()))

    
    def __hash__(self = None):
        return hash(self._specs)

    
    def __and__(self = None, other = None):
        '''Return a SpecifierSet which is a combination of the two sets.

        :param other: The other object to combine with.

        >>> SpecifierSet(">=1.0.0,!=1.0.1") & \'<=2.0.0,!=2.0.1\'
        <SpecifierSet(\'!=1.0.1,!=2.0.1,<=2.0.0,>=1.0.0\')>
        >>> SpecifierSet(">=1.0.0,!=1.0.1") & SpecifierSet(\'<=2.0.0,!=2.0.1\')
        <SpecifierSet(\'!=1.0.1,!=2.0.1,<=2.0.0,>=1.0.0\')>
        '''
        if isinstance(other, str):
            other = SpecifierSet(other)
        elif not isinstance(other, SpecifierSet):
            return NotImplemented
        specifier = SpecifierSet()
        specifier._specs = frozenset(self._specs | other._specs)
    # WARNING: Decompyle incomplete

    
    def __eq__(self = None, other = None):
        '''Whether or not the two SpecifierSet-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> (SpecifierSet(">=1.0.0,!=1.0.1", prereleases=False) ==
        ...  SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True))
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == ">=1.0.0,!=1.0.1"
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0,!=1.0.2")
        False
        '''
        if isinstance(other, (str, Specifier)):
            other = SpecifierSet(str(other))
        elif not isinstance(other, SpecifierSet):
            return NotImplemented
        return self._specs == other._specs

    
    def __len__(self = None):
        '''Returns the number of specifiers in this specifier set.'''
        return len(self._specs)

    
    def __iter__(self = None):
        '''
        Returns an iterator over all the underlying :class:`Specifier` instances
        in this specifier set.

        >>> sorted(SpecifierSet(">=1.0.0,!=1.0.1"), key=str)
        [<Specifier(\'!=1.0.1\')>, <Specifier(\'>=1.0.0\')>]
        '''
        return iter(self._specs)

    
    def __contains__(self = None, item = None):
        '''Return whether or not the item is contained in this specifier.

        :param item: The item to check for.

        This is used for the ``in`` operator and behaves the same as
        :meth:`contains` with no ``prereleases`` argument passed.

        >>> "1.2.3" in SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> Version("1.2.3") in SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> "1.0.1" in SpecifierSet(">=1.0.0,!=1.0.1")
        False
        >>> "1.3.0a1" in SpecifierSet(">=1.0.0,!=1.0.1")
        False
        >>> "1.3.0a1" in SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True)
        True
        '''
        return self.contains(item)

    
    def contains(self = None, item = None, prereleases = None, installed = (None, None)):
        '''Return whether or not the item is contained in this SpecifierSet.

        :param item:
            The item to check for, which can be a version string or a
            :class:`Version` instance.
        :param prereleases:
            Whether or not to match prereleases with this SpecifierSet. If set to
            ``None`` (the default), it uses :attr:`prereleases` to determine
            whether or not prereleases are allowed.

        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.2.3")
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains(Version("1.2.3"))
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.0.1")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.3.0a1")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True).contains("1.3.0a1")
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.3.0a1", prereleases=True)
        True
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self = None, iterable = None, prereleases = None):
        '''Filter items in the given iterable, that match the specifiers in this set.

        :param iterable:
            An iterable that can contain version strings and :class:`Version` instances.
            The items in the iterable will be filtered according to the specifier.
        :param prereleases:
            Whether or not to allow prereleases in the returned iterator. If set to
            ``None`` (the default), it will be intelligently decide whether to allow
            prereleases or not (based on the :attr:`prereleases` attribute, and
            whether the only versions matching are prereleases).

        This method is smarter than just ``filter(SpecifierSet(...).contains, [...])``
        because it implements the rule from :pep:`440` that a prerelease item
        SHOULD be accepted if no other versions match the given specifier.

        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.3", "1.5a1"]))
        [\'1.3\']
        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.3", Version("1.4")]))
        [\'1.3\', <Version(\'1.4\')>]
        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.5a1"]))
        []
        >>> list(SpecifierSet(">=1.2.3").filter(["1.3", "1.5a1"], prereleases=True))
        [\'1.3\', \'1.5a1\']
        >>> list(SpecifierSet(">=1.2.3", prereleases=True).filter(["1.3", "1.5a1"]))
        [\'1.3\', \'1.5a1\']

        An "empty" SpecifierSet will filter items based on the presence of prerelease
        versions in the set.

        >>> list(SpecifierSet("").filter(["1.3", "1.5a1"]))
        [\'1.3\']
        >>> list(SpecifierSet("").filter(["1.5a1"]))
        [\'1.5a1\']
        >>> list(SpecifierSet("", prereleases=True).filter(["1.3", "1.5a1"]))
        [\'1.3\', \'1.5a1\']
        >>> list(SpecifierSet("").filter(["1.3", "1.5a1"], prereleases=True))
        [\'1.3\', \'1.5a1\']
        '''
        pass
    # WARNING: Decompyle incomplete


