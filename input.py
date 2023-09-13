import os,subprocess

files=[file for file in os.listdir('.\\') if file.endswith('.py') or file.endswith('.PY') ]

#subprocess.call(['git','mv','.\\'+files[0],'.\\python\\'+files[0]])

print(files[1])
