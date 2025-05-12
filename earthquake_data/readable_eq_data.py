from pathlib import Path
import json

#Convert json object into python object using json.loads()
path = Path('D:\python\data_visualization_with_python\earthquake_data\eq_data_1_day_m1.geojson')
content = path.read_text(encoding='utf-8')
all_eq__data = json.loads(content)

#Convert python object into json object using json.loads(), write and save it as a file
path = Path('D:/python/data_visualization_with_python/earthquake_data/readable_eq_data.geojson')
readable_content = json.dumps(all_eq__data, indent = 4)
path.write_text(readable_content, encoding='utf-8')