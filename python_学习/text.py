import pysnooper

# @pysnooper.snoop('/text_log.log')
def division(start,end):
    for i in range(start,end,-1):
        with pysnooper.snoop():
            num1=i
            num2=i-1
            result=num1/num2
        print(result)
if __name__=='__main__':
    division(10,0)

