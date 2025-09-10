l1=[i for i in input()]
l2=[i for i in input()]
l3=[i for i in input()]
s1=set();s2=set();s3=set()
for i in l1:
    s1.add(i.lower())
for i in l2:
    s2.add(i.lower())
for i in l3:
    s3.add(i.lower())
s=(s1|s2)|s3
print("Total no of unique attendees:",(s))
print("Attended all three days",s1&s2&s3)
print("Attended day1 and day2",s1&s2)
print("Attended day1 and day3",s1&s3)
print("Attended day2 and day3",s2&s3)
print("Attended exactly one day",s1^s2^s3)
