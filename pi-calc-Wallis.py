def wallis(pairs):
   acc = 1
   num = 2
   for apair in range(pairs):
       leftterm = num/(num-1)
       rightterm = num/(num+1)
       
       acc = acc * leftterm * rightterm

       num = num + 2

   pi = acc * 2
   return pi


myPI =  wallis(2000)

print( myPI)
