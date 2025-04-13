def add_three_copies(data_list, data):

    data_list.append(data)
    data_list.append(data)
    data_list.append(data)

message = "Hello, World!"
message_list = []
    
add_three_copies(message_list, message)

print(message_list)

if __name__ == "__main__":
    main()
    
