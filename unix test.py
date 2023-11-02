import os, random

folder_path = "cookie"
folder_path_proxy1 = "proxy"
files_p = os.listdir(folder_path_proxy1)
files_c = os.listdir(folder_path)

proxy_arr = []
for file_p in files_p:
        file_path_proxy = os.path.join(folder_path_proxy1, file_p)
        with open(file_path_proxy, "r", encoding="UTF-8") as proxyFile:
            proxy = proxyFile.readlines()
            proxy_arr.extend(proxy)

proxy_df = random.randint(0,len(proxy_arr) - 1)
print(proxy_arr[proxy_df])
