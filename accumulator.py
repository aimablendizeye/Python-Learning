
 

total = 0
passed = 0
failed = 0
count = 0


def analysis (scores):
    global total,count,passed,failed
    for score in scores:
        total = total + score
        count = count + 1      
        if(score >=50):
            passed = passed +1            
        elif (score < 50):
            failed = failed + 1                        

scores = [78,89,30,60,47,90,40]   

analysis(scores)  

print(f"total marks: {total}")
print(f"Number of student: {count}")
print(f"Passed student: {passed}")
print(f"Failed: {failed}") 






