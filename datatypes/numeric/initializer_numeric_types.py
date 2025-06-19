from __data__ import disabled, disabletype
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from others.errors.errordevfile import ImportDisabledError, ImportDisabledWarning

if disabled:
    match disabletype.lower():
        case 'error' | 'raiseerror':
            raise ImportDisabledError("This type group is disabled")
        case 'warning' | 'raisewarning':
            raise ImportDisabledWarning("This type group is disabled")
        case 'block':
            raise ImportDisabledError("This type group is blocked")
        case _:
            raise ImportDisabledError(f"This type group is disabled (mode: {disabletype})")
