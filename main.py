from report import *
from counter import *
from page import *

# COUNTER
# people = {
#     'dolly': Counter(),
#     'eva': Counter(),
#     'miguel': Counter()
# }

# people['dolly'].increment()
# people['dolly'].increment()
# people['eva'].increment()
# people['dolly'].increment()
# people['dolly'].increment()
# people['eva'].increment()
# people['dolly'].increment()


# people['dolly'].show()
# people['eva'].show()
# people['miguel'].show()


# PAGE
person = {
    'name': 'Richard',
    'city': 'Dublin'
}
home = HTMLPage("<h1>Hello #name#, how is the weather in #city#?</h1>", person)
print(home.render())
home.save("home.html")

