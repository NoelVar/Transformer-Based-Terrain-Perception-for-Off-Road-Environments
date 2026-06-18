from pathlib import Path

def combine_files(split_path):
    # Ref: https://www.geeksforgeeks.org/python/python-program-to-merge-two-files-into-a-third-file/
    with open(f'../../data/processed/combined/{split_path}.txt', "w") as outfile:
        for filename in [f'../../data/processed/rugd/split_for_combination/{split_path}.txt', f'../../data/processed/rellis/{split_path}.lst']:
            with open(filename, 'r') as infile:
                for line in infile:
                    for url in line.strip().split(' '):
                        if Path(filename).suffix == '.txt':
                            content = f"rugd/{url} "
                        else:
                            if Path(url).suffix == ".jpg":
                                content = f"rellis/images/{url} "
                            else:
                                content = f"rellis/annotations/{url} "
                        outfile.write(content)
                    outfile.write('\n')

combine_files("train")
combine_files("test")
combine_files("val")