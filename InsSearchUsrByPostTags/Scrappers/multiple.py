import requests
import os
#first see how many lines are in file
#if there are more than 1, take first two, put them on an array each,
#then take that array.
def repeatedData(firstDataSet,secondDataSet):
    repeated=[];
    for data1 in firstDataSet:
        for data2 in secondDataSet:
            if(data1==data2):
                repeated.append(data1);
    return repeated;

list_of_posts=open("list_of_files.txt", "r")
lines_of_file= list_of_posts.readline()
hastag_files=lines_of_file.split(" ")
hastag_files.pop()


shared_posts= []
posts_to_check=[]
is_first=True
i=1
for list in hastag_files:

    print("This is the x file:"+list)
    posts=open(list, "r")
    if is_first:
        for line in posts:
            line=line.rstrip("\n")
            shared_posts.append(line)
            print("this is the 1st line: " +line+"appended")
        is_first=False
    else:
        del posts_to_check[:]
        for line in posts:
            line=line.rstrip("\n")
            print("this is the "+str(i)+" line: " +line)
            posts_to_check.append(line)
        shared_posts= repeatedData(shared_posts, posts_to_check)
    i= i+1
    print (shared_posts)

list_of_users=open("list_of_users.txt", "w+")
count=1
for i in shared_posts:
    r=requests.get("https://www.instagram.com/p/"+i+"/?__a=1")
    list_of_users.write("https://www.instagram.com/"+r.json()['graphql']['shortcode_media']['owner']['username']+"\n")
    count=count+1
    print(str(count)+" "+i+" "+r.json()['graphql']['shortcode_media']['owner']['username'])
