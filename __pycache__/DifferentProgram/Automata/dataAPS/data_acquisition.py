#SSH
import paramiko

class SSH():
    #생성자
    def __init__(self,hostname,username,password,port=22,**kwargs):
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        
        self.__connection = None
        
    #호스트네임
    #게터 Getter
    @property
    def hostname(self):
        return self.__hostname
    #세터 Setter
    @hostname.setter
    def hostname(self, param):
        self.__hostname = param
    
    #포트
    #게터 Getter
    @property
    def port(self):
        return self.__port
    #세터 Setter
    @port.setter
    def port(self, param):
        if(type(param)=='int'):
            self.__port = param
        else:
            raise TypeError
    
    #유저이름
    #게터 Getter
    @property
    def username(self):
        return self.__username
    #세터 Setter
    @username.setter
    def username(self, param):
        self.__username = param
        
        
    #비밀번호

    #게터 Getter
    @property
    def password(self):
        if(len(self.__password)>0):
            return True
        else:
            return False

    @password.setter
    def password(self, param):
        self.__password = param
    
        
    
    #연결
    def connect(self):
        obj = paramiko.SSHClient()
        obj.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        obj.connect(self.__hostname,self.__port,self.__username,self.__password)
        self.__connection = obj
        
    #연결 해제
    def disconnect(self):
        self.__connection.close()
    
    #명령
    def query(self,param : str):
        result = self.__connection.exec_command(param)
        return result