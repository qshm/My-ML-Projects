import os
import pathlib

cwd = os.getcwd()

target_dir = 'C:/tayfur/Foto PC'

target_dir_path = pathlib.Path(target_dir)

# for entry in target_dir_path.iterdir():
#     print(entry.name,'-', entry.parts)

dirs = (entry for entry in target_dir_path.iterdir() if entry.is_dir())

def has_sub_dirs(target_dir_path=None):

    if target_dir_path is not None:
        gen_subs = (sub for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())

        try:
            first = next(gen_subs)
            return True
        except StopIteration:
            return False

    else:
        raise ValueError

# for dir in dirs:
#     print(f'{dir} has a sub-directory: ', has_sub_dirs(dir))



def get_all_subdirs(target_dir_path=None):
    if target_dir_path is not None:
        search_path = target_dir_path

        while True:
            # print(len(list(sub for sub in search_path.iterdir() if sub.is_dir())))
            # print(search_path)

            subdirs_print = (sub for sub in search_path.iterdir() if sub.is_dir())
            subdirs = (sub for sub in search_path.iterdir() if sub.is_dir())
            for sub in subdirs_print:
                print(sub)

            try:
                search_path = next(subdirs)
                print('Now searching: ', search_path)

            except StopIteration:
                print('Stop Iteration received')
                search_path_str = os.path.dirname(search_path)
                search_path = pathlib.Path(search_path_str)

                print(search_path)


    else:
        raise ValueError

# print(target_dir_path)
get_all_subdirs(target_dir_path)