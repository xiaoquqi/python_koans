try:
  None.no_method()
except Exception as ex:
  print ex.__class__.__name__
  print ex.args[0]
