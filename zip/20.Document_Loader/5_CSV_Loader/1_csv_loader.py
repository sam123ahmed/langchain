from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="./20.Document_Loader/5_CSV_Loader/Social_Network_Ads.csv")

## use lazy_load while deal with large amount of data
docs = loader.load()

print(docs[0])
print(len(docs))