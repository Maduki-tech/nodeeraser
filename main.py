import os
import shutil

folders = ['~/work', '~/personal']

def delete_node_modules(folders):
    for folder in folders:
        folder_path = os.path.expanduser(folder)
        
        for root, dirs, files in os.walk(folder_path, topdown=False): # topdown=False to delete from child to parent
            if 'node_modules' in dirs:
                node_modules_path = os.path.join(root, 'node_modules')
                print(f"Deleting {node_modules_path}")
                shutil.rmtree(node_modules_path)

if __name__ == "__main__":
    delete_node_modules(folders)

