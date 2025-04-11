class UserMainCode(object):
    @classmethod
    def rebound(cls,input1,input2,input3):
        e=input2/input3
        res=input1*(e**2)
        return int(res)