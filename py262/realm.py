from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple

from py262.environment import LexicalEnvironment
from py262.value import Value

if TYPE_CHECKING:
    ParseNode = Any  # FIXME


class RealmRecord:
    intrinsics: Dict[str, Value]
    global_object: Value
    global_env: Optional[LexicalEnvironment]
    template_map: List[Tuple['ParseNode', Value]]
    host_defined: Optional[Any]
