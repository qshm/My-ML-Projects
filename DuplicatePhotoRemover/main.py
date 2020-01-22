import pathlib


def has_sub_dirs(target_dir_path=None):
    if target_dir_path is not None:
        gen_subs = (sub for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())

        try:
            first = next(gen_subs)
            return True
        except StopIteration:
            return False

    else:
        raise ValueError('Target path not specified')


def has_neighbour_dirs(target_dir_path=None):
    upper_dir = pathlib.Path(target_dir_path).parent

    if target_dir_path is not None:
        gen_neighbour_subs = (sub for sub in upper_dir.iterdir() if sub.is_dir())

        try:
            next(gen_neighbour_subs)
            second = next(gen_neighbour_subs)
            return True
        except StopIteration:
            return False

    else:
        raise ValueError('Target path not specified')


# def get_all_subdirs(target_dir_path=None):
#     if target_dir_path is not None:
#         search_path = target_dir_path
#
#         while True:
#             # print(len(list(sub for sub in search_path.iterdir() if sub.is_dir())))
#             # print(search_path)
#
#             subdirs_print = (sub for sub in search_path.iterdir() if sub.is_dir())
#             subdirs = (sub for sub in search_path.iterdir() if sub.is_dir())
#             for sub in subdirs_print:
#                 print(sub)
#
#             try:
#                 search_path = next(subdirs)
#                 print('Now searching: ', search_path)
#
#             except StopIteration:
#                 print('Stop Iteration received')
#                 search_path_str = os.path.dirname(search_path)
#                 search_path = pathlib.Path(search_path_str)
#
#                 print(search_path)
#
#
#     else:
#         raise ValueError
#
def recursive_subdir(target_dir_path=None):


    if target_dir_path is not None:

        # if not (has_sub_dirs(target_dir_path) and has_sub_dirs(target_dir_path)):
        #     print(target_dir_path, 'has no neighbours or subs')

        #
        # if has_neighbour_dirs(target_dir_path):
        #     print(target_dir_path, 'has neighbours')
        #
        #     try:
        #         gen_neighbour_subs = (sub for sub in pathlib.Path(target_dir_path).parent.iterdir() if sub.is_dir())
        #         neighbour = list(gen_neighbour_subs)[counter_neighbour]
        #
        #         print('printing neighbour', neighbour)
        #         return recursive_subdir(target_dir_path=neighbour, counter_neighbour=counter_neighbour+1, counter_sub=counter_sub)
        #
        #     except IndexError:
        #         counter_neighbour = 0
        #         print(target_dir_path, 'has no more neighbours')

        # todo: i have to nest the has_sub_dirs inside the neighbour conditional, otherwise it does not go into it unless neighbour counter is depleted
        if has_sub_dirs(target_dir_path):
            # print(target_dir_path, 'has subs')

            gen_subs_name = list(sub.name for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())
            # print('_-=*0*=-_-=*0*=-_-=*0*=-_-=*0*=-_-=*0*=-_-=*0*=-_-=*0*=-')
            print(f'__________________ Subs of {target_dir_path}')
            print(*gen_subs_name, sep='\n')

            gen_subs_path = list(sub for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())

            subs_container = []

            for sub_name, sub_path in zip(gen_subs_name, gen_subs_path):
                # print(sub_name, sep='\n')
                # print('----------------------------------------')

                subs_container.append(recursive_subdir(target_dir_path=sub_path))

            print(f'----------------------------------------------------------------returning sub_container for: {target_dir_path}')
            return subs_container

        else:
            # print(target_dir_path, 'does not have any subs, function does not return anything')
            # print('----------------------00000000000000000000------------------')
            pass
    else:
        raise ValueError('Target path not specified')


if __name__ == "__main__":
    target_dir = 'H:/'

    # print(has_neighbour_dirs(target_dir))
    # print(has_sub_dirs(target_dir))
    recursive_subdir(target_dir)
