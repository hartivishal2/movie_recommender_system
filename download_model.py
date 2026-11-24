
import gdown
import os

file_id = "1XwhMTYQNPCy5rMqbZWathY95XCeP-ein"

output = "similarity.pkl"

if not os.path.exists(output):
    print("Downloading similarity matrix...")

    gdown.download(
        id=file_id,
        output=output,
        quiet=False
    )

if os.path.exists(output):
    print("Similarity matrix downloaded successfully!")
else:
    raise FileNotFoundError("Failed to download similarity.pkl")
