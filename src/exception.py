import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    ''''
    Parameters:
    - error: represents the exception that occurred
    - error_detail: an instance of sys module
    Returns:(str) 
    - information about the error such as 
    the filename, line number, and the error message 
    using the traceback (exc_tb) obtained from the error_detail.
    '''
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
#inheriting from the built-in Exception class.
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        #calling the constructor of the base class (Exception), by passing the error_message argument to it.
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    #overriding the '__str__' method to return the error message
    def __str__(self):
        return self.error_message