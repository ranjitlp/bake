import glob


class bread() :
   def __init__(self,bake) :
      self.dummy = 0
      self.bake = bake
 
   def run(self) :
      #   for y in glob.glob("a*.gz") :
      for y in (["abc.gz"]) :
         #self.bake.fdf("unzip:none","abc:"+y,"gunzip "+y)
         self.bake.fdf("unzip:none","abc:"+y,"sleep 10")

      self.bake.fdf("move:copy","xyz:def","cp def xyz")
      self.bake.fdf("copy:unzip","def:abc","cp abc def")
      
      print ("hello world")
      
