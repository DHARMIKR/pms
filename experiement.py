import pymongo

def database_connection():
    # Replace the connection string with your MongoDB connection string
    # You can get this from your MongoDB Atlas dashboard or set up your local connection
    mongo_uri = "mongodb+srv://dharmikpatel08:RoeDKw9EC5T4p4dQ@pms.kzqukrf.mongodb.net/?retryWrites=true&w=majority"
    
    # Add tlsAllowInvalidCertificates option to ignore SSL certificate validation
    client = pymongo.MongoClient(mongo_uri, tlsAllowInvalidCertificates=True)
    print("MongoDB Client:", client)

    # Access a specific database
    db = client["pms"]
    print("Database:", db)

    # Access the collection
    collection = db["pms"]

    # Query all documents in the collection
    cursor = collection.find()

    # Iterate through the documents and print them
    print("All Documents in the Collection:")
    for document in cursor:
        print(document['username'], document['password'])

database_connection()


#mongodb+srv://dharmikpatel08:RoeDKw9EC5T4p4dQ@pms.kzqukrf.mongodb.net/