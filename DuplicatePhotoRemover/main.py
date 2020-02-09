import pathlib
import math
from collections import Counter

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


def has_sub_dirs(target_dir_path=None):
    if target_dir_path is not None:
        gen_subs = (sub for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())

        try:
            next(gen_subs)
            return True
        except StopIteration:
            return False

    else:
        raise ValueError('Target path not specified')

# todo: put recursive_subdir in a class and hide implementation, user should be able to pass path only

def recursive_subdir(target_dir_path=None, iter_count=None, searchfor=None, duplicates=None):

    if duplicates is None:
        duplicates = []

    if iter_count is None:
        iter_count = 0

    if target_dir_path is not None:

        target_name = pathlib.Path(target_dir_path).name

        # todo: i have to nest the has_sub_dirs inside the neighbour conditional, otherwise it does not go into it unless neighbour iter_count is depleted
        if has_sub_dirs(target_dir_path):

            indent = "|  "*iter_count + f"{iter_count}. "

            # use glob('**/*') if need to iterate over all sub directories
            filesize = sum(f.stat().st_size for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())
            filenum = sum(1 for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())

            new = [(f.name, convert_size(f.stat().st_size)) for f in pathlib.Path(target_dir_path).glob('*') if (f.is_file())]
            duplicates = duplicates + new

            print(f'{indent}{target_name} - {convert_size(filesize)} - {filenum} files')

            # turned off printing counter here, bec I actually only need to print when there are no more subfolders (in else below)
            dup_count = Counter(duplicates)
            print(len(duplicates))
            # print(Counter(el for el in dup_count.elements() if dup_count[el] > 1))



            iter_count += 1

            gen_subs_name = list(sub.name for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())
            gen_subs_path = list(sub for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())

            subs_container = []

            for sub_name, sub_path in zip(gen_subs_name, gen_subs_path):
                # print(sub_name, searchfor)
                # print('----------------------------------------')

                # print(sub_name, searchfor)
                if sub_name == searchfor:
                    print(f'{searchfor} found in {sub_path}, terminating...')
                    return
                else:
                    subs_container.append(recursive_subdir(target_dir_path=sub_path, iter_count=iter_count, duplicates=duplicates,searchfor=searchfor))

            return subs_container

        else:
            indent = "|  "*iter_count + f"{iter_count}. "

            filesize = sum(f.stat().st_size for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())
            filenum = sum(1 for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())

            new = [(f.name, convert_size(f.stat().st_size)) for f in pathlib.Path(target_dir_path).glob('*') if (f.is_file())]
            duplicates = duplicates + new

            # todo: updated value of duplicates not passed to global duplicates when this else terminates with "pass"
            # todo: so when no more subs, duplicate count reverts back. need a way to update global duplicates (maybe with generator?)

            print(f'{indent}{target_name} - {convert_size(filesize)} - {filenum} files')

            dup_count = Counter(duplicates)

            print('printing else:',len(duplicates))
            print(Counter(el for el in dup_count.elements() if dup_count[el] > 1))


            # todo: if target has no subs, search does not stop even when found. (if has subs, stops properly, look at above logic)
            if target_name == searchfor:
                print(f'{searchfor} found in {target_dir_path}, terminating...')
                return

            else:
                pass

    else:
        raise ValueError('Target path not specified')


if __name__ == "__main__":
    target_dir = 'C:/tayfur/Foto PC/'

    # todo: counter goes into sub folder and re_counts files and adds to counter object
    # todo: make get file size an optional argument that can be turned on/off
    # todo: write exception handling for access denied

    recursive_subdir(target_dir)
