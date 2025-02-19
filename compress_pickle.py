import pickle
import gzip

# List of .pkl files to compress
files_to_compress = [
    ('MovieRec/smil_lst.pkl', 'MovieRec/smil_lst_compressed.pkl.gz'),
    ('MovieRec/movies_lst.pkl', 'MovieRec/movies_lst_compressed.pkl.gz')
]

# Compress each file
for input_file, output_file in files_to_compress:
    print(f"Loading {input_file} ...")
    with open(input_file, 'rb') as f:
        data = pickle.load(f)
    
    print(f"Compressing {input_file} ...")
    with gzip.open(output_file, 'wb') as f:
        pickle.dump(data, f)
    
    print(f"File compressed and saved as: {output_file}")

print("All files compressed successfully! 🚀")
