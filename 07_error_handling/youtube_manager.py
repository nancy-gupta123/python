import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            test= json.load(file)
            print(type(test))
            return test
        
    except FileNotFoundError:
        return []    
    

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)  



def list_all_youtube_videos(videos):
    print("\n")
    print("*"*69)
    for index, videos in enumerate(videos,start=1):
        print(f"{index}. {videos['name']}, Duration: {videos['time']}")
    
    print("*"*69)


def add_videos(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name': name ,'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_youtube_videos(videos)
    index=int(input("Enter the new video number to update: "))
    if 1<=index<=len(videos):
        name=input("Enter the new video name: ")
        time=input("Enter the new video time: ")
        videos[index-1]={'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")




def delete_videos(videos):
    list_all_youtube_videos(videos)
    index=int(input("Enter the video number to be deleted: "))

    if(1<=index<=len(videos)):
        del videos[index-1]
        save_data_helper(videos)

    else:
        print("Invalid video index selected")    

    


 
def main():
    videos=load_data()
    while True:
        print("\n Toutube Manager | choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice=input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_youtube_videos(videos)

            case '2':
                add_videos(videos)

            case '3':
                update_videos(videos)

            case '4':
                delete_videos(videos)

            case '5':
                break    

            case '_':
                print("Invalid Choice")

if __name__=="__main__":
    main()



