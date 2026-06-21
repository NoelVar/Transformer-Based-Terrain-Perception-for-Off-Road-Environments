# Ref: https://www.geeksforgeeks.org/python/python-os-symlink-method/
# Ref2: https://stackoverflow.com/questions/8299386/modifying-a-symlink-in-python
# IMPORTANT: enable developer mode on windows before running.
import os, errno

# source and destination paths
src = [
    os.path.abspath("data\\RELLIS-3D\\images"), 
    os.path.abspath("data\\processed\\rugd\\images")
]
dst = [
    os.path.abspath("data\\processed\\combined\\rellis\\images"), 
    os.path.abspath("data\\processed\\combined\\rugd\\images")
]

# Create symbolic link
for i in range(len(src)):
    # print(src[i], dst[i])
    try:
        os.symlink(src[i], dst[i], target_is_directory=True)
        print(f"Link created: {dst[i]} -> {src[i]}")
    except OSError as e:
        if e.errno == errno.EEXIST:
            print("Error: Link already exists.")
            os.rmdir(dst[i])
            print("Attempting to remove and recreate link...")
            os.symlink(src[i], dst[i], target_is_directory=True)
            print(f"Link created: {dst[i]} -> {src[i]}")
        else:
            raise e