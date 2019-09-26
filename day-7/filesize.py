import os
filename = 'test.txt'
stats = os.stat(filename)
print('the file size of {} is {} bytes'.format(filename,stats.st_size))