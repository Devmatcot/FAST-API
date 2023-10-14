from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes='bcrypt')

class Hash():
    #this function is use to hash the password
    def bcrypt(password:str):
        return pwd_ctx.hash(password)
    def verify(hash_password, plain_password):
        return pwd_ctx.verify(plain_password, hash_password)
        
