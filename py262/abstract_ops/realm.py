from typing import Dict

from py262.realm import RealmRecord
from py262.value import Value

from .lexical_environment import new_global_environment
from .value import type_of


def create_realm() -> RealmRecord:
    realm_rec = RealmRecord()
    create_intrinsics(realm_rec)
    realm_rec.global_object = Value.undefined
    realm_rec.global_env = None
    realm_rec.template_map = []
    return realm_rec


def create_intrinsics(realm_rec: RealmRecord):
    intrinsics: Dict[str, Value] = {}
    realm_rec.intrinsics = intrinsics
    # TODO: populate intrinsics record and
    # add_restricted_function_properties(
    #     intrinsics['%Function.prototype%'],
    #     realm_rec,
    # )
    return intrinsics


def set_realm_global_object(realm_rec: RealmRecord, global_obj: Value,
                            this_value: Value):
    if global_obj is Value.undefined:
        pass
        # intrinsics = realm_rec.intrinsics
        # FIXME
        # global_obj = ordinary_object_create(intrinsics['%Object.prototype%'])
    assert type_of(global_obj) == 'object'
    if this_value is Value.undefined:
        this_value = global_obj
    realm_rec.global_object = global_obj
    new_global_env = new_global_environment(global_obj, this_value)
    realm_rec.global_env = new_global_env
    return realm_rec


def set_default_global_bindings(realm_rec: RealmRecord):
    global_ = realm_rec.global_object
    # TODO: clause 18?
    return global_
