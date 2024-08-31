import os
print("Access all environment variables:")
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
print("Access a particular environment variable:")
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
print('Value of the environment variable key:')
print(os.getenv('JAVA_HOME'))
print(os.getenv('PYTHONPATH'))