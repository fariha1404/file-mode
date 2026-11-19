# open the file in read mode
file_read = open('Codingal.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal.txt', 'w')
# write in the file
file_write.write(" File in write mode ...")
file_write.write("Hi! I am Fariha. I am 11 yr. old")
file_write.close()

# open the file in append mode
file_append = open