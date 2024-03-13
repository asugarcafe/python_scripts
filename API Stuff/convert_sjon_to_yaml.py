# -*- coding: utf-8 -*-

import json
import yaml

# JSON string (replace this with your actual JSON data)
json_data = '{"key": "value", "array": [1, 2, 3]}'

# Convert JSON to Python data (dictionary)
python_data = json.loads(json_data)

# Convert Python data to YAML
yaml_data = yaml.dump(python_data, default_flow_style=False)

print(yaml_data)