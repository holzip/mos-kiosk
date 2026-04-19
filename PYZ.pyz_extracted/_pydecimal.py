# Source Generated with Decompyle++
# File: _pydecimal.pyc (Python 3.12)

'''Python decimal arithmetic module'''
__all__ = [
    'Decimal',
    'Context',
    'DecimalTuple',
    'DefaultContext',
    'BasicContext',
    'ExtendedContext',
    'DecimalException',
    'Clamped',
    'InvalidOperation',
    'DivisionByZero',
    'Inexact',
    'Rounded',
    'Subnormal',
    'Overflow',
    'Underflow',
    'FloatOperation',
    'DivisionImpossible',
    'InvalidContext',
    'ConversionSyntax',
    'DivisionUndefined',
    'ROUND_DOWN',
    'ROUND_HALF_UP',
    'ROUND_HALF_EVEN',
    'ROUND_CEILING',
    'ROUND_FLOOR',
    'ROUND_UP',
    'ROUND_HALF_DOWN',
    'ROUND_05UP',
    'setcontext',
    'getcontext',
    'localcontext',
    'MAX_PREC',
    'MAX_EMAX',
    'MIN_EMIN',
    'MIN_ETINY',
    'HAVE_THREADS',
    'HAVE_CONTEXTVAR']
__xname__ = __name__
__name__ = 'decimal'
__version__ = '1.70'
__libmpdec_version__ = '2.4.2'
import math as _math
import numbers as _numbers
import sys

try:
    from collections import namedtuple as _namedtuple
    DecimalTuple = _namedtuple('DecimalTuple', 'sign digits exponent', module = 'decimal')
    ROUND_DOWN = 'ROUND_DOWN'
    ROUND_HALF_UP = 'ROUND_HALF_UP'
    ROUND_HALF_EVEN = 'ROUND_HALF_EVEN'
    ROUND_CEILING = 'ROUND_CEILING'
    ROUND_FLOOR = 'ROUND_FLOOR'
    ROUND_UP = 'ROUND_UP'
    ROUND_HALF_DOWN = 'ROUND_HALF_DOWN'
    ROUND_05UP = 'ROUND_05UP'
    HAVE_THREADS = True
    HAVE_CONTEXTVAR = True
    if sys.maxsize == 0x7FFFFFFFFFFFFFFF:
        MAX_PREC = 0xDE0B6B3A763FFFF
        MAX_EMAX = 0xDE0B6B3A763FFFF
        MIN_EMIN = -0xDE0B6B3A763FFFF
    else:
        MAX_PREC = 425000000
        MAX_EMAX = 425000000
        MIN_EMIN = -425000000
    MIN_ETINY = MIN_EMIN - MAX_PREC - 1
    
    class DecimalException(ArithmeticError):
        """Base exception class.

    Used exceptions derive from this.
    If an exception derives from another exception besides this (such as
    Underflow (Inexact, Rounded, Subnormal)) that indicates that it is only
    called if the others are present.  This isn't actually used for
    anything, though.

    handle  -- Called when context._raise_error is called and the
               trap_enabler is not set.  First argument is self, second is the
               context.  More arguments can be given, those being after
               the explanation in _raise_error (For example,
               context._raise_error(NewError, '(-x)!', self._sign) would
               call NewError().handle(context, self._sign).)

    To define a new exception, it should be sufficient to have it derive
    from DecimalException.
    """
        
        def handle(self, context, *args):
            pass


    
    class Clamped(DecimalException):
        '''Exponent of a 0 changed to fit bounds.

    This occurs and signals clamped if the exponent of a result has been
    altered in order to fit the constraints of a specific concrete
    representation.  This may occur when the exponent of a zero result would
    be outside the bounds of a representation, or when a large normal
    number would have an encoded exponent that cannot be represented.  In
    this latter case, the exponent is reduced to fit and the corresponding
    number of zero digits are appended to the coefficient ("fold-down").
    '''
        pass

    
    class InvalidOperation(DecimalException):
        '''An invalid operation was performed.

    Various bad things cause this:

    Something creates a signaling NaN
    -INF + INF
    0 * (+-)INF
    (+-)INF / (+-)INF
    x % 0
    (+-)INF % x
    x._rescale( non-integer )
    sqrt(-x) , x > 0
    0 ** 0
    x ** (non-integer)
    x ** (+-)INF
    An operand is invalid

    The result of the operation after this is a quiet positive NaN,
    except when the cause is a signaling NaN, in which case the result is
    also a quiet NaN, but with the original sign, and an optional
    diagnostic information.
    '''
        
        def handle(self, context, *args):
            if args:
                ans = _dec_from_triple(args[0]._sign, args[0]._int, 'n', True)
                return ans._fix_nan(context)


    
    class ConversionSyntax(InvalidOperation):
        '''Trying to convert badly formed string.

    This occurs and signals invalid-operation if a string is being
    converted to a number and it does not conform to the numeric string
    syntax.  The result is [0,qNaN].
    '''
        
        def handle(self, context, *args):
            return _NaN


    
    class DivisionByZero(ZeroDivisionError, DecimalException):
        '''Division by 0.

    This occurs and signals division-by-zero if division of a finite number
    by zero was attempted (during a divide-integer or divide operation, or a
    power operation with negative right-hand operand), and the dividend was
    not zero.

    The result of the operation is [sign,inf], where sign is the exclusive
    or of the signs of the operands for divide, or is 1 for an odd power of
    -0, for power.
    '''
        
        def handle(self, context, sign, *args):
            return _SignedInfinity[sign]


    
    class DivisionImpossible(InvalidOperation):
        '''Cannot perform the division adequately.

    This occurs and signals invalid-operation if the integer result of a
    divide-integer or remainder operation had too many digits (would be
    longer than precision).  The result is [0,qNaN].
    '''
        
        def handle(self, context, *args):
            return _NaN


    
    class DivisionUndefined(ZeroDivisionError, InvalidOperation):
        '''Undefined result of division.

    This occurs and signals invalid-operation if division by zero was
    attempted (during a divide-integer, divide, or remainder operation), and
    the dividend is also zero.  The result is [0,qNaN].
    '''
        
        def handle(self, context, *args):
            return _NaN


    
    class Inexact(DecimalException):
        '''Had to round, losing information.

    This occurs and signals inexact whenever the result of an operation is
    not exact (that is, it needed to be rounded and any discarded digits
    were non-zero), or if an overflow or underflow condition occurs.  The
    result in all cases is unchanged.

    The inexact signal may be tested (or trapped) to determine if a given
    operation (or sequence of operations) was inexact.
    '''
        pass

    
    class InvalidContext(InvalidOperation):
        '''Invalid context.  Unknown rounding, for example.

    This occurs and signals invalid-operation if an invalid context was
    detected during an operation.  This can occur if contexts are not checked
    on creation and either the precision exceeds the capability of the
    underlying concrete representation or an unknown or unsupported rounding
    was specified.  These aspects of the context need only be checked when
    the values are required to be used.  The result is [0,qNaN].
    '''
        
        def handle(self, context, *args):
            return _NaN


    
    class Rounded(DecimalException):
        '''Number got rounded (not  necessarily changed during rounding).

    This occurs and signals rounded whenever the result of an operation is
    rounded (that is, some zero or non-zero digits were discarded from the
    coefficient), or if an overflow or underflow condition occurs.  The
    result in all cases is unchanged.

    The rounded signal may be tested (or trapped) to determine if a given
    operation (or sequence of operations) caused a loss of precision.
    '''
        pass

    
    class Subnormal(DecimalException):
        '''Exponent < Emin before rounding.

    This occurs and signals subnormal whenever the result of a conversion or
    operation is subnormal (that is, its adjusted exponent is less than
    Emin, before any rounding).  The result in all cases is unchanged.

    The subnormal signal may be tested (or trapped) to determine if a given
    or operation (or sequence of operations) yielded a subnormal result.
    '''
        pass

    
    class Overflow(Rounded, Inexact):
        '''Numerical overflow.

    This occurs and signals overflow if the adjusted exponent of a result
    (from a conversion or from an operation that is not an attempt to divide
    by zero), after rounding, would be greater than the largest value that
    can be handled by the implementation (the value Emax).

    The result depends on the rounding mode:

    For round-half-up and round-half-even (and for round-half-down and
    round-up, if implemented), the result of the operation is [sign,inf],
    where sign is the sign of the intermediate result.  For round-down, the
    result is the largest finite number that can be represented in the
    current precision, with the sign of the intermediate result.  For
    round-ceiling, the result is the same as for round-down if the sign of
    the intermediate result is 1, or is [0,inf] otherwise.  For round-floor,
    the result is the same as for round-down if the sign of the intermediate
    result is 0, or is [1,inf] otherwise.  In all cases, Inexact and Rounded
    will also be raised.
    '''
        
        def handle(self, context, sign, *args):
            if context.rounding in (ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_HALF_DOWN, ROUND_UP):
                return _SignedInfinity[sign]
            if None == 0:
                if context.rounding == ROUND_CEILING:
                    return _SignedInfinity[sign]
                return None(sign, '9' * context.prec, (context.Emax - context.prec) + 1)
            if None == 1:
                if context.rounding == ROUND_FLOOR:
                    return _SignedInfinity[sign]
                return None(sign, '9' * context.prec, (context.Emax - context.prec) + 1)


    
    class Underflow(Subnormal, Rounded, Inexact):
        '''Numerical underflow with result rounded to 0.

    This occurs and signals underflow if a result is inexact and the
    adjusted exponent of the result would be smaller (more negative) than
    the smallest value that can be handled by the implementation (the value
    Emin).  That is, the result is both inexact and subnormal.

    The result after an underflow will be a subnormal number rounded, if
    necessary, so that its exponent is not less than Etiny.  This may result
    in 0 with the sign of the intermediate result and an exponent of Etiny.

    In all cases, Inexact, Rounded, and Subnormal will also be raised.
    '''
        pass

    
    class FloatOperation(TypeError, DecimalException):
        '''Enable stricter semantics for mixing floats and Decimals.

    If the signal is not trapped (default), mixing floats and Decimals is
    permitted in the Decimal() constructor, context.create_decimal() and
    all comparison operators. Both conversion and comparisons are exact.
    Any occurrence of a mixed operation is silently recorded by setting
    FloatOperation in the context flags.  Explicit conversions with
    Decimal.from_float() or context.create_decimal_from_float() do not
    set the flag.

    Otherwise (the signal is trapped), only equality comparisons and explicit
    conversions are silent. All other mixed operations raise FloatOperation.
    '''
        pass

    _signals = [
        Clamped,
        DivisionByZero,
        Inexact,
        Overflow,
        Rounded,
        Underflow,
        InvalidOperation,
        Subnormal,
        FloatOperation]
    _condition_map = {
        InvalidContext: InvalidOperation,
        DivisionUndefined: InvalidOperation,
        DivisionImpossible: InvalidOperation,
        ConversionSyntax: InvalidOperation }
    _rounding_modes = (ROUND_DOWN, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_CEILING, ROUND_FLOOR, ROUND_UP, ROUND_HALF_DOWN, ROUND_05UP)
    import contextvars
    _current_context_var = contextvars.ContextVar('decimal_context')
    _context_attributes = frozenset([
        'prec',
        'Emin',
        'Emax',
        'capitals',
        'clamp',
        'rounding',
        'flags',
        'traps'])
    
    def getcontext():
        """Returns this thread's context.

    If this thread does not yet have a context, returns
    a new context and sets this thread's context.
    New contexts are copies of DefaultContext.
    """
        
        try:
            return _current_context_var.get()
        except LookupError:
            context = Context()
            _current_context_var.set(context)
            return 


    
    def setcontext(context):
        """Set this thread's context to context."""
        if context in (DefaultContext, BasicContext, ExtendedContext):
            context = context.copy()
            context.clear_flags()
        _current_context_var.set(context)

    del contextvars
    
    def localcontext(ctx = (None,), **kwargs):
        '''Return a context manager for a copy of the supplied context

    Uses a copy of the current context if no context is specified
    The returned context manager creates a local decimal context
    in a with statement:
        def sin(x):
             with localcontext() as ctx:
                 ctx.prec += 2
                 # Rest of sin calculation algorithm
                 # uses a precision 2 greater than normal
             return +s  # Convert result to normal precision

         def sin(x):
             with localcontext(ExtendedContext):
                 # Rest of sin calculation algorithm
                 # uses the Extended Context from the
                 # General Decimal Arithmetic Specification
             return +s  # Convert result to normal context

    >>> setcontext(DefaultContext)
    >>> print(getcontext().prec)
    28
    >>> with localcontext():
    ...     ctx = getcontext()
    ...     ctx.prec += 2
    ...     print(ctx.prec)
    ...
    30
    >>> with localcontext(ExtendedContext):
    ...     print(getcontext().prec)
    ...
    9
    >>> print(getcontext().prec)
    28
    '''
        pass
    # WARNING: Decompyle incomplete

    
    class Decimal(object):
        '''Floating-point class for decimal arithmetic.'''
        __slots__ = ('_exp', '_int', '_sign', '_is_special')
        
        def __new__(cls, value, context = ('0', None)):
            """Create a decimal point instance.

        >>> Decimal('3.14')              # string input
        Decimal('3.14')
        >>> Decimal((0, (3, 1, 4), -2))  # tuple (sign, digit_tuple, exponent)
        Decimal('3.14')
        >>> Decimal(314)                 # int
        Decimal('314')
        >>> Decimal(Decimal(314))        # another decimal instance
        Decimal('314')
        >>> Decimal('  3.14  \\n')        # leading and trailing whitespace okay
        Decimal('3.14')
        """
            self = object.__new__(cls)
        # WARNING: Decompyle incomplete

        from_float = (lambda cls, f: if isinstance(f, int):
sign = 0 if f >= 0 else 1k = 0coeff = str(abs(f))elif isinstance(f, float):
if _math.isinf(f) or _math.isnan(f):
cls(repr(f))if None.copysign(1, f) == 1:
sign = 0else:
sign = 1(n, d) = abs(f).as_integer_ratio()k = d.bit_length() - 1coeff = str(n * 5 ** k)else:
raise TypeError('argument must be int or float.')result = _dec_from_triple(sign, coeff, -k)if cls is Decimal:
resultcls(result))()
        
        def _isnan(self):
            '''Returns whether the number is not actually one.

        0 if a number
        1 if NaN
        2 if sNaN
        '''
            if self._is_special:
                exp = self._exp
                if exp == 'n':
                    return 1
                if exp == 'N':
                    return 2
            return 0

        
        def _isinfinity(self):
            '''Returns whether the number is infinite

        0 if finite or not a number
        1 if +INF
        -1 if -INF
        '''
            if self._exp == 'F':
                if self._sign:
                    return -1
                return 1
            return 0

        
        def _check_nans(self, other, context = (None, None)):
            '''Returns whether the number is not actually one.

        if self, other are sNaN, signal
        if self, other are NaN return nan
        return 0

        Done before operations.
        '''
            self_is_nan = self._isnan()
        # WARNING: Decompyle incomplete

        
        def _compare_check_nans(self, other, context):
            '''Version of _check_nans used for the signaling comparisons
        compare_signal, __le__, __lt__, __ge__, __gt__.

        Signal InvalidOperation if either self or other is a (quiet
        or signaling) NaN.  Signaling NaNs take precedence over quiet
        NaNs.

        Return 0 if neither operand is a NaN.

        '''
            pass
        # WARNING: Decompyle incomplete

        
        def __bool__(self):
            '''Return True if self is nonzero; otherwise return False.

        NaNs and infinities are considered nonzero.
        '''
            if not self._is_special:
                self._is_special
            return self._int != '0'

        
        def _cmp(self, other):
            '''Compare the two non-NaN decimal instances self and other.

        Returns -1 if self < other, 0 if self == other and 1
        if self > other.  This routine is for internal use only.'''
            if self._is_special or other._is_special:
                self_inf = self._isinfinity()
                other_inf = other._isinfinity()
                if self_inf == other_inf:
                    return 0
                if self_inf < other_inf:
                    return -1
                return 1
            if not self:
                if not other:
                    return 0
                return --1 ** other._sign
            if not None:
                return -1 ** self._sign
            if None._sign < self._sign:
                return -1
            if self._sign < other._sign:
                return 1
            self_adjusted = self.adjusted()
            other_adjusted = other.adjusted()
            if self_adjusted == other_adjusted:
                self_padded = self._int + '0' * (self._exp - other._exp)
                other_padded = other._int + '0' * (other._exp - self._exp)
                if self_padded == other_padded:
                    return 0
                if self_padded < other_padded:
                    return --1 ** self._sign
                return None ** self._sign
            if None > other_adjusted:
                return -1 ** self._sign
            return -None ** self._sign

        
        def __eq__(self, other, context = (None,)):
            (self, other) = _convert_for_comparison(self, other, equality_op = True)
            if other is NotImplemented:
                return other
            if None._check_nans(other, context):
                return False
            return self._cmp(other) == 0

        
        def __lt__(self, other, context = (None,)):
            (self, other) = _convert_for_comparison(self, other)
            if other is NotImplemented:
                return other
            ans = None._compare_check_nans(other, context)
            if ans:
                return False
            return self._cmp(other) < 0

        
        def __le__(self, other, context = (None,)):
            (self, other) = _convert_for_comparison(self, other)
            if other is NotImplemented:
                return other
            ans = None._compare_check_nans(other, context)
            if ans:
                return False
            return self._cmp(other) <= 0

        
        def __gt__(self, other, context = (None,)):
            (self, other) = _convert_for_comparison(self, other)
            if other is NotImplemented:
                return other
            ans = None._compare_check_nans(other, context)
            if ans:
                return False
            return self._cmp(other) > 0

        
        def __ge__(self, other, context = (None,)):
            (self, other) = _convert_for_comparison(self, other)
            if other is NotImplemented:
                return other
            ans = None._compare_check_nans(other, context)
            if ans:
                return False
            return self._cmp(other) >= 0

        
        def compare(self, other, context = (None,)):
