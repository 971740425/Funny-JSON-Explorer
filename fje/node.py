from abc import ABC, abstractmethod
from typing import List, Callable, Union
import json
import os
from .exception import FJEException

id = 0

class JSONNode(ABC):
    def __init__(self, name: str, level: int):
        global id 
        self._name = name
        self._level = level
        self._id = id
        id += 1

    @abstractmethod
    def is_leaf(self) -> bool:
        pass

    @abstractmethod
    def traverse(self, fn: Callable[['JSONNode'], None]):
        pass

    def is_root(self) -> bool:
        return self._level == 0

    def get_name(self) -> str:
        return self._name
    
    def get_id(self) -> int:
        return self._id
    
    def get_level(self) -> int:
        return self._level
    
class JSONComposite(JSONNode):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.children: List[JSONNode] = []
    
    def is_leaf(self) -> bool:
        return False

    def traverse(self, fn: Callable[['JSONNode'], None]):
        fn(self)
        for child in self.children:
            child.traverse(fn)

    def add_child(self, child: JSONNode):
        self.children.append(child)
    
    def get_children(self) -> List[JSONNode]:
        return self.children

    def __iter__(self):
        return iter(self.children)
    
class JSONLeaf(JSONNode):
    def __init__(self, name, level, value: Union[str, None]):
        super().__init__(name, level)
        self._value = value

    def is_leaf(self) -> bool:
        return True

    def traverse(self, fn: Callable[['JSONNode'], None]):
        fn(self)

    def get_value(self) -> Union[str, None]:
        return self._value
    
class JSONNodeFactory:
    def __init__(self, filepath: str):
        if os.path.isfile(filepath) == False:
            raise FJEException(f'文件{filepath}不存在')
        with open(filepath, 'r', encoding='utf-8') as f:
            self.json_data = json.load(f)
        if not isinstance(self.json_data, (dict, list)):
            raise FJEException(f'JSON根节点必须是字典或列表')
    
    def create(self) -> JSONNode:
        return self._create('', 0, self.json_data)

    def _create(self, name: str, level: int, obj) -> JSONNode:
        if isinstance(obj, list):
            return self._create_composite_from_list(name, level, obj)
        elif isinstance(obj, dict):
            return self._create_composite_from_dict(name, level, obj)
        else:
            return self._create_leaf(name, level, obj)

    def _create_composite_from_list(self, name: str, level: int, obj) -> JSONComposite:
        composite = JSONComposite(name, level)
        for idx, item in enumerate(obj):
            child = self._create(f'Array[{idx}]', level + 1, item)
            composite.add_child(child)
        return composite

    def _create_composite_from_dict(self, name: str, level: int, obj) -> JSONComposite:
        composite = JSONComposite(name, level)
        for key, value in obj.items():
            child = self._create(key, level + 1, value)
            composite.add_child(child)
        return composite
    
    def _create_leaf(self, name: str, level: int, obj) -> JSONLeaf:
        if obj is None:
            return JSONLeaf(name, level, None)
        else:
            return JSONLeaf(name, level, str(obj))