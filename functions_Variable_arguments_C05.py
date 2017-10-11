def test_var_args(my_name, *my_friends):
    print ("first normal arg:", my_name)
    for arg in my_friends:
        print ("another arg through *my_friends :", arg)


test_var_args('Srinivas','Ramu','Vasu','Murali','Teja')
