#Display name
class Entity():
    __ID = None
    __displayName = None
    __category = None
    __protocol = None
    __hostname = None
    __port = None
    __username = None
    __password = None
    
    __isCPURequired = False
    __isRAMRequired = False
    __isHDDRequired = False
    
    __isPolicyCountRequired = False
    __isEntityCountRequired = False
    
    def __init__(self):
        print("Entity Created")
        
    #ID
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self,param):
        self.__ID = param
    
    #CATEGORY
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self,param):
        self.__category = param
        
    #displayName
    @property
    def displayName(self):
        return self.__displayName
    @displayName.setter
    def displayName(self,param):
        self.__displayName = param
    
    #protocol
    @property
    def protocol(self):
        return self.__protocol
    @protocol.setter
    def protocol(self,param):
        self.__protocol = param    
    
    #hostname
    @property
    def hostname(self):
        return self.__hostname
    @hostname.setter
    def hostname(self,param):
        self.__hostname = param
        
    #port
    @property
    def port(self):
        return self.__port
    @port.setter
    def port(self,param):
        self.__port = param
        
    #username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,param):
        self.__username = param
        
    #password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,param):
        self.__password = param
    
    
class Firewall(Entity):
    def __init__(self):
        self.__category = 'Firewall'
        self.__isCPURequired = True
        self.__isRAMRequired = True
        self.__isHDDRequired = True
        
    #TEST
    def __str__(self):
        print("Firewall")
        print("Category : "+str(self.category()))
        print("Display Name"+str(self.displayName()))
        # print(self.hostname())
        # print(self.password())
        # print(self.port())
        # print(self.protocol())
        # print(self.username())