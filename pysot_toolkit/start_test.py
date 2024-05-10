import os
ep_id = [1111, 1112, 1114, 1115, 1116]
"""for i in range(1161, 1181):
    print("==> test {}th epoch".format(i))
    name = "scatt"+str(i)
    os.system("python -u pysot_toolkit/test_all_ep.py --name {0} --epnum {1}".format(name, i))"""
for i in range(len(ep_id)):
    print("==> test {}th epoch".format(ep_id[i]))
    name = "scatt"+str(ep_id[i])
    os.system("python -u pysot_toolkit/test_all_ep.py --name {0} --epnum {1}".format(name, ep_id[i]))

