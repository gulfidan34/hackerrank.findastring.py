Find a string

def count_substring(string,sub_string):
    count=0
    l=len(sub_string)
    for i in range(len(string)):
        s=string[i:i+l]
        if s==sub_string:
            count=count+1
    return(count)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
