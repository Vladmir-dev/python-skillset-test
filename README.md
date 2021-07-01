python skill test
#server
i created a socket and then binded the port number and the address of the client and then listened for connection wth client
i then created a function threaded client to represent and perform the actions of a single connected client so that i can allow multiple clients to connect on different threads
in threaded_client i import a file and then send it to the client and then i close that thread after the transfer and i call the function in a while loop where i accept the connection to the client and increase the number of threads for each client that gets connected

#client
i create a socket and the connect to the server using the address and port number
i then get the recieved data and store it in the variable data after which i copy the data onto another file received_data and then i close the file when there is no data transfer
