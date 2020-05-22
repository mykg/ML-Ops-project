# taking last all lines of output.txt and converting into list

listoflines = list()
with open('output.txt','r') as myfile:
    for line in myfile:
        listoflines.append(line.strip())

# converting list into string 

model_history = listoflines[-1:]
str1 = ""
for element in model_history:
    str1 = element
#print(str1)

#converting string into float
accuracy = str1[80:87]
print(accuracy)
accuracy_f = float(accuracy)
val_accuracy = str1[122:129]
print(val_accuracy)
val_accuracy_f = float(val_accuracy)

# saving variable into seperate files
acc_file=open("accuracy.txt","w")
acc_file.write('%f' % accuracy_f)
acc_file.close()
val_acc_file=open("val_accuracy.txt","w")
val_acc_file.write('%f' % val_accuracy_f)
val_acc_file.close()

print("accuracy:",accuracy_f,"\nvalidation accuracy:",val_accuracy_f)
import os
if (accuracy_f < 0.80 or val_accuracy_f < 0.80):
    
    print("altering model")
    
    reading_file=open("model.py",'r')
    new_file_content=""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("#addlayerhere","top_model = Dense(100, activation='relu')(top_model)")
        new_file_content += new_line + "\n"
    reading_file.close()
    writing_file = open("model.py",'w')
    writing_file.write(new_file_content)
    writing_file.close()
    
    os.system("sed -ie 's/lr_x=0.001/lr_x=print(round(random.uniform(0.001,0.1),4))/g' /root/MLops/model/model.py")
else:
    print("best model has already been created")
