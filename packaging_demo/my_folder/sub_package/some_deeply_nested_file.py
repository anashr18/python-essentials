from packaging.my_other_file import CONSTANT_FOR_NESTED_file

# here we try to fetch assets from parents
print(CONSTANT_FOR_NESTED_file)

# this will work without installing the package
print("this is me from deeply nested files")
