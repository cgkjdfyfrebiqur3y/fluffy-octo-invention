from __data__ import disabled, disabletype, version
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from others.errors.errordevfile import (
    ImportDisabledError, 
    ImportDisabledWarning,
    VersionIsIndevError,
    VersionIsIndevWarning
)

# Check if the group is disabled
if disabled:
    match disabletype.lower():
        case 'error' | 'raiseerror':
            raise ImportDisabledError("The future group is disabled")
        case 'warning' | 'raisewarning':
            raise ImportDisabledWarning("The future group is disabled")
        case 'block':
            raise ImportDisabledError("The future group is blocked")
        case _:
            raise ImportDisabledError(f"The future group is disabled (mode: {disabletype})")

# Version status checks
match version.lower():
    case 'indev':
        if disabletype.lower() in ('error', 'raiseerror', 'block'):
            raise VersionIsIndevError("This group is in development and not ready for production use")
        else:
            raise VersionIsIndevWarning("Warning: This group is in development stage")
    case 'beta':
        raise ImportDisabledWarning("This group is in beta testing")
    case 'stable':
        pass  # Stable version, no warnings needed
    case _:
        raise ImportDisabledError(f"Unknown version status: {version}")
