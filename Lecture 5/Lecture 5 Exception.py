# >>> Exception Handling
# When an error occurs, or exception as we call it, 
# Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

try:
  print(x)
except:
  print("An exception occurred") 


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 


try:
    raise NotImplementedError("No error")
except Exception as e:
    exc=str(e)
    print(exc)



import sys, os

try:
    raise NotImplementedError("No error")
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
