def swapFiles():
    file1 = input('file1:')
    file2 = input('file2:')
    
    fileValues = [open(file1).read(),open(file2).read()]
    
    open(file1,'w').write(fileValues[1])
    open(file2,'w').write(fileValues[0])
    print('{0} = "{1}",{2} = "{3}"'.format(file1,open(file1).read(),file2,open(file2).read()))

while True:
    swapFiles()