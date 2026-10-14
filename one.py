import os
B=r'E:/fenta/Downloads/The Anticloud/ANTICLOUD_REPOS'
p=os.path.join(B,'CAMERAS')
print('CAMERAS one-level:')
for e in sorted(os.listdir(p)):
    full=os.path.join(p,e)
    print(' ',repr(e),os.path.isdir(full))
