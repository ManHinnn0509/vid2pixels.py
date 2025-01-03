import os
import json

def read_json_file(path: str, encoding: str="utf-8"):
    """
        Reads a json file as dict() and return it \n
        None will be returned if any Exception is raised
    """
    try:
        with open(path, "r", encoding=encoding) as f:
            s = f.read()
            
        return json.loads(s)
    except Exception as e:
        # print(e)
        return None

def write_json_file(path: str, data, encoding: str="utf-8", mkdir: bool=False):
    try:
        if (mkdir):
            parts = path.split("/")
            filename = parts.pop(-1)
            mkdirs('/'.join(parts))
        
        with open(path, 'w+', encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def mkdirs(dir_name: str):
    """
        Creates directories recursively
    """
    try:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        return True
    
    except Exception as e:
        # print(e)
        return False