import mimetypes
import re

content_types = sorted(set(mimetypes.types_map.values()))

for content_type in content_types:
    module, subtype = content_type.split("/")
    constant = re.sub(r"[-+\.]", "_", subtype).upper()
    with open(f"src/content_types/{module}.py", "a") as f:
        f.write(f'{constant} = "{content_type}"\n')
