# if you want to read any txt files you can read like below
# with Open() function




name = input("Enter your name:")
my_File_write = open('demo','w')
my_File_write.write(name)
my_File_write.close()



my_File= open('demo','r')
file_contents = my_File.read()
print(file_contents)






