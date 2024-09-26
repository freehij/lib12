def a()->str:r=__import__("random").randint;return __import__("datetime").datetime.utcfromtimestamp(__import__("time").time()+(r(9999999,999999999)if r(1,5)!=1else r(99999,9999999))).strftime("%Y-%m-%d %H:%M:%S")
def b()->str:a=__import__("random");r=a.randint;return __import__("datetime").datetime.utcfromtimestamp(__import__("time").time()+a.choice([r(99999,9999999),r(9999999,999999999),r(999999999,5999999999)])).strftime("%Y-%m-%d %H:%M:%S")
class CustomDict:
    def __init__(self)->None:self.__i=[];self.__j=[]
    def set(self,key:__import__("typing").Any,value:__import__("typing").Any)->None:
        if key not in self.__i:self.__i.append(key);self.__j.insert(self.__i.index(key),value)
    def get(self,key:__import__("typing").Any)->__import__("typing").Any:return self.__j[self.__i.index(key)]if key in self.__i else None
    def get_by_pos(self, key: int):return self.__j[key]if key in self.__i else None
    def keys(self)->list:return self.__i
    def values(self)->list:return self.__j
    def items(self)->__import__("typing").Generator:
        for i in self.keys():yield i,self.__j[self.__i.index(i)]
