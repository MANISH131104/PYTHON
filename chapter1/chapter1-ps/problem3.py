import pprint

def print_dict_contents(d):
    """
    Pretty print the dictionary contents using pprint module.
    
    :param d: dictionary to print
    """
    pprint.pprint(d, indent=4, width=80, sort_dicts=True)

if __name__ == "__main__":
    my_dict = {
        'name': 'Alice',
        'age': 30,
        'languages': ['English', 'Spanish', 'Japanese'],
        'education': {
            'undergrad': 'Computer Science',
            'postgrad': None
        },
        'hobbies': ('reading', 'hiking', 'coding')
    }
    
    print("Dictionary contents:")
    print_dict_contents(my_dict)
