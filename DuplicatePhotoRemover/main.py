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
def recursive_subdir(target_dir_path=None, counter_neighbour=None, counter_sub=None):

    if counter_neighbour is None:
        counter_neighbour = 0
    if counter_sub is None:
        counter_sub = 0

    if target_dir_path is not None:

        # for n in gen_neighbour_subs:
        #     print('neighbour1:', n)
        #

        # for sub in gen_subs:
        #     print('sub1:', sub)

        if not (has_sub_dirs(target_dir_path) and has_sub_dirs(target_dir_path)):
            print(target_dir_path, 'has no neighbours or subs')

        if has_neighbour_dirs(target_dir_path):
            print(target_dir_path, 'has neighbours')

            try:
                gen_neighbour_subs = (sub for sub in pathlib.Path(target_dir_path).parent.iterdir() if sub.is_dir())
                neighbour = list(gen_neighbour_subs)[counter_neighbour]

                print('printing neighbour', neighbour)
                return recursive_subdir(target_dir_path=neighbour, counter_neighbour=counter_neighbour+1, counter_sub=counter_sub)

            except IndexError:
                counter_neighbour = 0
                print(target_dir_path, 'has no more neighbours')

        # todo: i have to nest the has_sub_dirs inside the neighbour conditional, otherwise it does not go into it unless neighbour counter is depleted
        if has_sub_dirs(target_dir_path):
            print(target_dir_path, 'has subs')

            try:
                gen_subs = (sub for sub in pathlib.Path(target_dir_path).iterdir() if sub.is_dir())
                sub = list(gen_subs)[counter_sub]
                print('printing sub', sub)
                return recursive_subdir(target_dir_path=sub, counter_neighbour=counter_neighbour, counter_sub=counter_sub+1)


            except IndexError:
                print(target_dir_path, 'has no more subs')
                counter_sub = 0
    else:
        raise ValueError('Target path not specified')


if __name__ == "__main__":


    target_dir = 'C:/tayfur/Foto PC/'

    # print(has_neighbour_dirs(target_dir))
    # print(has_sub_dirs(target_dir))
    recursive_subdir(target_dir)