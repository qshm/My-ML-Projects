import pathlib
import math

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

def recursive_subdir(target_dir_path=None, counter=None, searchfor=None):

    if counter is None:
        counter = 0

    if target_dir_path is not None:

        target_name = pathlib.Path(target_dir_path).name

        # todo: i have to nest the has_sub_dirs inside the neighbour conditional, otherwise it does not go into it unless neighbour counter is depleted
        if has_sub_dirs(target_dir_path):

            indent = "|  "*counter + f"{counter}. "

            filesize = sum(f.stat().st_size for f in pathlib.Path(target_dir_path).glob('**/*') if f.is_file())


            print(f'{indent}{target_name} - {convert_size(filesize)}')

            counter += 1

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
                    subs_container.append(recursive_subdir(target_dir_path=sub_path, counter=counter, searchfor=searchfor))

            return subs_container

        else:
            indent = "|  "*counter + f"{counter}. "

            filesize = sum(f.stat().st_size for f in pathlib.Path(target_dir_path).glob('**/*') if f.is_file())

            print(f'{indent}{target_name} - {convert_size(filesize)}')



            # todo: if target has no subs, search does not stop even when found. (if has subs, stops properly, look at above logic)
            if target_name == searchfor:
                print(f'{searchfor} found in {target_dir_path}, terminating...')
                return

            else:
                pass

    else:
        raise ValueError('Target path not specified')


if __name__ == "__main__":
    target_dir = 'D:/pictures'

    # todo: make get file size an optional argument that can be turned on/off
    # todo: write exception handling for access denied

    recursive_subdir(target_dir)
