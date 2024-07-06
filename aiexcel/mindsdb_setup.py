from mindsdb_sdk import MindsDB

# Initialize MindsDB
mindsdb = MindsDB()

# Create model for Excel knowledge
mindsdb.create_model(
    name='excel_knowledge_model',
    from_table='excel_knowledge'
)