from py262.abstract_ops.value import type_of
from py262.completion import NormalCompletion, ThrowCompletion
from py262.environment import AbstractEnvironment
from py262.reference import Reference, SuperReference
from py262.value import Value, value


def get_base(ref):
    return ref.base


def get_referenced_name(ref):
    return ref.referenced_name


def is_strict_reference(ref):
    return ref.is_strict


def has_primitive_base(ref):
    return value(isinstance(ref.base, Value) and ref.base.is_primitive())


def is_property_reference(ref):
    return NormalCompletion(
        value(
            type_of(ref.base) == 'object'
            or has_primitive_base(ref) is Value.true))


def is_unresolvable_reference(ref):
    return value(ref.base is Value.undefined)


def is_super_reference(ref):
    return value(isinstance(ref, SuperReference))


def get_value(v_completion):
    if v_completion.is_abrupt():
        return v_completion
    v = v_completion.value

    if not isinstance(v, Reference):
        return NormalCompletion(v)

    base = get_base(v)

    if is_unresolvable_reference(v) is Value.true:
        return ThrowCompletion(value('new TypeError'))  # FIXME
    if is_property_reference(v) is Value.true:
        if has_primitive_base(v) is Value.true:
            assert type_of(v.base) not in ('null', 'undefined')
            # https://tc39.es/ecma262/#sec-getvalue
            raise NotImplementedError()
        raise NotImplementedError()
    assert isinstance(base, AbstractEnvironment)
    return base.get_binding_value(get_referenced_name(v),
                                  is_strict_reference(v))


def put_value(v_completion, w_completion):
    if v_completion.is_abrupt():
        return v_completion
    v = v_completion.value
    if w_completion.is_abrupt():
        return w_completion
    w = w_completion.value

    if not isinstance(v, Reference):
        return ThrowCompletion(value('new ReferenceError'))  # FIXME

    base = get_base(v)

    if is_unresolvable_reference(v) is Value.true:
        if is_strict_reference(v) is Value.true:
            return ThrowCompletion(value('new ReferenceError'))  # FIXME
        # https://tc39.es/ecma262/#sec-putvalue
        raise NotImplementedError()
    if is_property_reference(v) is Value.true:
        if has_primitive_base(v) is Value.true:
            assert type_of(get_base(v)) not in ('undefined', 'null')
            # https://tc39.es/ecma262/#sec-putvalue
            raise NotImplementedError()
        # https://tc39.es/ecma262/#sec-putvalue
        raise NotImplementedError()
    assert isinstance(v, AbstractEnvironment)
    return base.set_mutable_binding(get_referenced_name(v), w,
                                    is_strict_reference(v))


def get_this_value(v):
    assert is_property_reference(v) is Value.true
    if isinstance(v, SuperReference):
        return v.this_value
    base = get_base(v)
    assert isinstance(base, Value)  # FIXME is this assumption correct?
    return base


def initialize_referenced_binding(v_completion, w_completion):
    if v_completion.is_abrupt():
        return v_completion
    v = v_completion.value
    if w_completion.is_abrupt():
        return w_completion
    w = w_completion.value
    assert isinstance(w, Value)

    assert isinstance(v, Reference)
    assert not is_unresolvable_reference(v)

    base = get_base(v)

    assert isinstance(base, AbstractEnvironment)

    return base.initialize_binding(get_referenced_name(v), w)
