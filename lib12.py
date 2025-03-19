def a()->str:r=__import__("random").randint;return __import__("datetime").datetime.utcfromtimestamp(__import__("time").time()+(r(9999999,999999999)if r(1,5)!=1 else r(99999,9999999))).strftime("%Y-%m-%d %H:%M:%S")
def b()->str:a=__import__("random");r=a.randint;return __import__("datetime").datetime.utcfromtimestamp(__import__("time").time()+a.choice([r(99999,9999999),r(9999999,999999999),r(999999999,5999999999)])).strftime("%Y-%m-%d %H:%M:%S")
from typing import Generator, Any
class CustomDict:
    def __init__(self)->None:self.__i=[];self.__j=[]
    def set(self,key:Any,value:Any)->None:self.__i.append(key)if key not in self.__i else None;self.__j.insert(self.__i.index(key),value)
    def remove(self,key:Any)->None:self.__j.remove(self.__i.index(key));self.__i.remove(key)
    def get(self,key:Any)->Any:return self.__j[self.__i.index(key)]if key in self.__i else None
    def get_by_pos(self, key: int)->Any:return self.__j[key]if key in self.__i else None
    def keys(self)->list:return self.__i
    def values(self)->list:return self.__j
    def items(self)->Generator:yield from((i,self.__j[self.__i.index(i)])for i in self.__i)
    def clear(self)->None:self.__init__()
    def __getitem__(self,key:Any)->Any:return self.get(key)
    def __getattr__(self,key:str)->Any:return self.get(key)
    def __setitem__(self,key:Any,value:Any)->None:self.set(key,value)
    def __setattr__(self,key:str,value:Any)->None:super().__setattr__(key,value)if key.startswith("_")else self.set(key,value)
__all__=["a", "b", "CustomDict"]
