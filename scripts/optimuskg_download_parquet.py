from pathlib import Path
import sys

# In this monorepo, the published client package lives under
# packages/optimuskg/src/optimuskg, while the pipeline package also uses the
# name "optimuskg" at the repo root. Prepend the client src directory so this
# script imports the Dataverse client, not the pipeline package.
REPO_ROOT = Path(__file__).resolve().parents[1]
CLIENT_SRC = REPO_ROOT / "packages" / "optimuskg" / "src"
sys.path.insert(0, str(CLIENT_SRC))

import optimuskg

nodes_path = optimuskg.get_file("nodes.parquet")
edges_path = optimuskg.get_file("edges.parquet")

print(nodes_path)
print(edges_path)
# output:
# /Users/robin/Library/Caches/optimuskg/doi_10_7910_DVN_IYNGEV/2.0/nodes.parquet
# /Users/robin/Library/Caches/optimuskg/doi_10_7910_DVN_IYNGEV/2.0/edges.parquet