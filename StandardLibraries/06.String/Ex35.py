
from string import Template

names = ['John', 'Paul', 'Lisa', 'Michael']

template = Template("""Hello $name,

Thank you for visiting our website.
Team, XYZ""")


# print emails
for i in names:
    email = template.substitute(name=i)

    print(email)
    print("-"*35)