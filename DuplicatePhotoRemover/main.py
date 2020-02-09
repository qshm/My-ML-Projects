import pathlib
import math
from collections import Counter
import itertools


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



def add_duplicates(new_duplicates):
    duplicates = []
    while True:
        yield duplicates
        duplicates = duplicates + new_duplicates


# todo: put recursive_subdir in a class and hide implementation, user should be able to pass path only
#  and newid or glob_duplicates should be class variables
#  Also get total size of all duplicates and possibly move them to a directory called duplicates
#  another step: get metadata from pictures, currently only checking filename and size to decide if duplicate

newid = itertools.count()
glob_duplicates = []

def recursive_subdir(target_dir_path=None, iter_count=None, searchfor=None):


    if iter_count is None:
        iter_count = 0


    if target_dir_path is not None:

        target_name = pathlib.Path(target_dir_path).name


        if has_sub_dirs(target_dir_path):

            indent = "|  "*iter_count + f"{iter_count}. "

            # newid is a counter that increments every time it's called, unlike iter_count, which is set to 0 beginning of each function call
            print('else: subfolder no', next(newid))

            # use glob('**/*') if need to iterate over all sub directories
            filesize = sum(f.stat().st_size for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())
            filenum = sum(1 for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())


            print(f'{indent}{target_name} - {convert_size(filesize)} - {filenum} files')

            new = [(f.name, convert_size(f.stat().st_size)) for f in pathlib.Path(target_dir_path).glob('*') if (f.is_file())]

            glob_duplicates.extend(new)

            # turned off printing counter here, bec I actually only need to print when there are no more subfolders (in else below)
            # dup_count = Counter(duplicates)
            # print(len(duplicates))
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
                    subs_container.append(recursive_subdir(target_dir_path=sub_path, iter_count=iter_count, searchfor=searchfor))

            return subs_container

        else:
            indent = "|  "*iter_count + f"{iter_count}. "

            # newid is a counter that increments every time it's called, unlike iter_count, which is set to 0 beginning of each function call
            print('else: subfolder no', next(newid))

            filesize = sum(f.stat().st_size for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())
            filenum = sum(1 for f in pathlib.Path(target_dir_path).glob('*') if f.is_file())

            new = [(f.name, convert_size(f.stat().st_size)) for f in pathlib.Path(target_dir_path).glob('*') if (f.is_file())]
            # temp = glob_duplicates + new
            glob_duplicates.extend(new)


            print(f'{indent}{target_name} - {convert_size(filesize)} - {filenum} files')

            #
            dup_count = Counter(glob_duplicates)
            #
            # print('printing else:',len(glob_duplicates))
            # print(glob_duplicates)
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
    target_dir = 'C:/tayfur/Foto PC'





    recursive_subdir(target_dir)
