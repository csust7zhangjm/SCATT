import os
ep_id = [1117, 1118, 1119, 1120, 1121]

"""for i in range(1192, 1197):
    print("==> test {}th epoch".format(i))
    name = "scatt"+str(i)
    os.system("python -u pysot_toolkit/test_all_ep_1.py --name {0} --epnum {1}".format(name, i))"""
for i in range(len(ep_id)):
    print("==> test {}th epoch".format(ep_id[i]))
    name = "scatt"+str(ep_id[i])
    os.system("python -u pysot_toolkit/test_all_ep_1.py --name {0} --epnum {1}".format(name, ep_id[i]))
